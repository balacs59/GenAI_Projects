# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:02:47 2024

@author: bavenka
"""

import streamlit as st
from handlers import generate_chat_completion

# Streamlite UI
st.title("Welcome to AI comedian chatbot 😂")


#Get user input
with st.form("user_form", clear_on_submit=True):
    user_input = st.text_input("Type any topic to generate a joke for you ")
    submit_button = st.form_submit_button(label="Send")
    

if submit_button:
    #with st.spinner("Coming up with a joke..."):
    completion = generate_chat_completion(user_input)
    st.write(completion)
