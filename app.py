import time
import numpy as np
import pandas as pd
import streamlit as st
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ],
  stream=True
)

def stream_data():
    for chunk in response:
        print(chunk.choices[0].delta.content)
        yield chunk.choices[0].delta.content



if st.button("Stream data"):
    st.write_stream(stream_data)