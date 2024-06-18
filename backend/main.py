# uvicorn main:app --reload

# Main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

# Custom function imports
from functions.openai_request import convert_audio_to_text, get_chat_response
from functions.database import store_message, reset_messages
from functions.text_to_speech import convert_text_to_speech


# Initialting the App
app = FastAPI()

# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]

# CORS - middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check health
@app.get("/health")
async def check_health():
    return {"message": "Healthy"}

# Reset messages
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "Conversation reset!"}

# Post bot response
# Note: Not playing in browser when using post request
# @app.post("/post_audio/")
# async def post_audio(File: UploadFile = File(...)):
#     print("hello")

@app.post("/post_audio/")
async def post_audio(file: UploadFile = File(...)):
    # Get audio file
    #audio_input = open("voice.mp3", "rb")

    # Save file from frontend
    with open(file.filname, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filname, "rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)

    # Gaurd: Ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode the audio!")
    
    # Get chat response
    chat_response = get_chat_response(message_decoded)

    # Gaurd: Ensure message decoded
    if not chat_response:
        return HTTPException(status_code=400, detail="Failed to get chat response!")

    # Store the message
    store_message(message_decoded, chat_response)

    # Convert chat response to audio
    audio_output = convert_text_to_speech(chat_response)

    # Gaurd: Ensure message decoded
    if not audio_output:
        return HTTPException(status_code=400, detail="Failed to get ElevenLabs audio response!")
    
    # Create a generator that yields chunks of data
    def iterfile():
        yield audio_output

    # Return the audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream")