import streamlit as st

correct_username: str = "user"
correct_password: str = "pass"

st.set_page_config(page_title="Sign Up Page", page_icon="🔒", layout="centered")
st.markdown("""
    <style>
        .stTextInput > div > div > input {
            background-color: #ecf0f1;
            color: #2c3e50;
        }
        .stButton > button {
            background-color: #27ae60;
            color: #ecf0f1;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #94e0c0;'>Login</h2>", unsafe_allow_html=True)

username = st.text_input("Username", key="username")
password = st.text_input("Password", type="password", key="password")

if st.button("Sign Up"):
    if username == correct_username and password == correct_password:
        st.success(f"Thank you, {username}!, You are now registered.")
    else:
        st.error("Invalid username or password.")
