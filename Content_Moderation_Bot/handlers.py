# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 12:07:39 2024

@author: bavenka
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:26:40 2024

@author: bavenka
"""

import sys
import openai
import tiktoken
from colorama import Fore


client = openai.OpenAI()
PERSONA = "You are a skilled chatbot to filter out inappropriate content."
# Set up Language Model
LANGUAGE_MODEL = "gpt-3.5-turbo"
SYSTEM_MESSAGE = "You are a skilled stand-up comedian with a knack for telling 1-2 sentence funny stories"
messages = [{"role":"system", "content":SYSTEM_MESSAGE}]



def moderate_input(user_input):
    response = client.moderations.create(input=user_input)
    return response.results[0].flagged
    

def generate_chat_completion(user_input, messages):
    # try to add exception handling
    try:
        flagged = moderate_input(user_input)
        print(f"Flagged: {flagged}")
        if flagged:
            return ":red[Your comment has been flagged as inappropriate. Sorry Cannot provide a response !]"
        response = client.chat.completions.create(model= LANGUAGE_MODEL,
                                              messages= messages, 
                                              temperature=0.7,
                                              max_tokens=100)
        message = response.choices[0].message
        return message.content
    except Exception:
        return "Error occurred while generating a response. We will fix it soon"