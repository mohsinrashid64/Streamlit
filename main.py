import streamlit as st
import requests
import json

def main():
    st.title('Chat with Document')

    prompt = st.chat_input("Ask Something")
    print(prompt)




if __name__ == "__main__":
    main()
