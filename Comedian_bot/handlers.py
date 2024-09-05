# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 12:07:39 2024

@author: Balachandar
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:26:40 2024

@author: Balachandar
"""

import sys
import openai
import tiktoken
from colorama import Fore


client = openai.OpenAI()
PERSONA = "You are a skilled stand-up comedian with great skills to make people laugh."
# Set up Language Model
LANGUAGE_MODEL = "gpt-3.5-turbo"
SYSTEM_MESSAGE = "You are a skilled stand-up comedian with a knack for telling 1-2 sentence funny stories"
messages = [{"role":"system", "content":SYSTEM_MESSAGE}]



def to_dict(obj):
    return {
        "role": obj.role,
        "content": obj.content
    }


def print_messages(messages):
    messages = [message for message in messages if message["role"] != "system"]
    for message in messages:
        role = "Bot" if message["role"] == "assistant" else "You"
        print(Fore.BLUE + role + ": " + message["role"])
    return messages


def generate_chat_completion(user_input=""):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(model= LANGUAGE_MODEL,
                                              messages= messages, 
                                              temperature=0.7,
                                              max_tokens=100)
    message = response.choices[0].message
    messages.append(to_dict(message))
    print(response)
    return message.content