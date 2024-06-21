import streamlit as st
from pages import main_page, second_page
from messages import messages
import random

# Main app logic
if 'page' not in st.session_state:
    st.session_state.page = "main_page"
if 'message_index' not in st.session_state:
    st.session_state.message_index = random.randint(0, len(messages) - 1)
if 'show_hint' not in st.session_state:
    st.session_state.show_hint = False

if st.session_state.page == "main_page":
    main_page()
elif st.session_state.page == "second_page":
    second_page()
