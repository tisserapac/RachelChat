import json
import random

# Get reason message
def get_recent_messages():
    # Define the file name and lear instructions
    file_name = "stored_data.json"

    learn_instructions = {
        "role": "system",
        "content": "You are interviewing the user for a job as a retail assistant. Ask short questions that are relevant to the junior possition. Your name is Rachel. The user is called Anjana. Keep your answers under 30 words."
    }

    # Initialize the messages
    messages = []

    # Add a random element
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instructions["content"] = learn_instructions["content"] + " Your response will include some dry humor" 
    else:
        learn_instructions["content"] = learn_instructions["content"] + " Your response will not include a rather challenging question"

    # Appent inst. to messages
    messages.append(learn_instructions)

    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append last 5 items of data
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)       
    except Exception as e:
        print(e)
        pass

    return messages