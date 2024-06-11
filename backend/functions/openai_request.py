import openai
from decouple import config

# Custom imports
from functions.database import get_recent_messages

openai.api_key = config("OPEN_AI_KEY")
openai.organization = config("OPEN_AI_ORG")


# Open AI - Wispher
# Conver audio to text
def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript["text"]
        return message_text
    except Exception as e:
        print(e)
        return
    
# Open AI - ChatGPT
# Get response for our messages
def get_chat_response(message_input):
    messages = get_recent_messages()
    user_mesage = {"role": "user", "content": message_input}
    messages.append(user_mesage)
    print(messages)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            # temperature=0.7,
            # max_tokens=100,
            # top_p=1,
            # frequency_penalty=0,
            # presence_penalty=0,
        )
        print(response)
        message_text =  response["choices"][0]["message"]["content"]
        return message_text 
    except Exception as e:
        print(e)
        return
