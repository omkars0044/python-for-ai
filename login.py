import streamlit as st

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Login")
st.write("Welcome back! Please log in to continue.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("Login successful!")
    else:
        st.error("Invalid username or password.")

st.divider()

st.write("Don't have an account?")
st.button("Create Account")