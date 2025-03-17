import streamlit as st
import google.generativeai as genai

# Set up Gemini API key
API_KEY = "hhfruambr93m5h8aj435u8ka"  # Replace with your Gemini API Key
genai.configure(api_key=API_KEY)

# Streamlit UI
st.title("🤖 AI Chatbot")
st.write("Chat with AI!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generate AI response
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Using Google Gemini-Pro model
        response = model.generate_content(user_input)
        ai_response = response.text.strip()

        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        with st.chat_message("assistant"):
            st.write(ai_response)

    except Exception as e:
        st.error(f"Error: {e}")
