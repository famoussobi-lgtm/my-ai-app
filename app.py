import google.generativeai as genai
import streamlit as st

st.set_page_config(page_title="Mera Apna AI", page_icon="🤖")
st.title("🤖 Mera Apna Personal AI")

# Yahan apni API Key daalein
genai.configure(api_key=st.secrets["AQ.Ab8RN6JsJvP8SnmEOJ0UYx-3uE6W0n37K5ACOTRcKde3_D3iFg"])
model = genai.GenerativeModel("gemini-1.5-flash")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Koyi bhi sawal pucho..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append(
            {"role": "assistant", "content": response.text}
        )
