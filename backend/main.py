# uvicorn main:app --reload

# Main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

# Custom function imports
from functions.openai_request import convert_audio_to_text, get_chat_response
from functions.database import store_message, reset_messages


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

@app.get("/post_audio_get/")
async def get_audio():
    # Get audio file
    audio_input = open("voice.mp3", "rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)

    # Gaurd: Ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode the audio!")
    
    # Get chat response
    chat_response = get_chat_response(message_decoded)

    # Store the message
    store_message(message_decoded, chat_response)

    return chat_response

    return "Done"