import streamlit as st
import sqlite3
from pages.dependencias.utils import init_database

# Initialize session state variable
if "message" not in st.session_state:
    st.session_state["message"] = ""

st.write("Hello")

init_database()