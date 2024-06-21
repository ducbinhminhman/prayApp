import streamlit as st
from messages import messages
import random

def main_page():
    st.header("DAILY SOUL CONNECT")

    # Display the image
    st.image("image/cover_page.webp", use_column_width=True)

    st.write("Open your daily message of hope. Click 'Pray' to see what awaits you today.")

    # Create a button for navigation
    if st.button("Pray"):
        # Set a session state variable to switch pages and store the message index
        st.session_state.page = "second_page"
        st.session_state.message_index = random.randint(0, len(messages) - 1)
        st.session_state.show_hint = False
        st.experimental_rerun()  # Ensure the page switches immediately

def second_page():
    st.header("DAILY SOUL CONNECT")

    # Retrieve the selected message
    selected_message = messages[st.session_state.message_index]

    # Display the selected message
    st.image(selected_message['image'], use_column_width=True)
    st.write(f"Here is the message for you today: {selected_message['message']}")
    #st.write(f"Example: {selected_message['example']}")
    st.write(f"{selected_message['practice']}")
    # Show the practice message if "Show Hint" is clicked
    if st.button("Show Hint"):
        st.session_state.show_hint = True

    if st.session_state.show_hint:
        #st.write(f"Practice: {selected_message['practice']}")
        st.write(f"{selected_message['example']}")
    # Create a button to go back to the main page
    if st.button("Back to Main"):
        st.session_state.page = "main_page"
        st.experimental_rerun()  # Ensure the page switches immediately
