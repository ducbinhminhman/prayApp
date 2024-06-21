import streamlit as st
import random

# Function to display the main page
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

# Function to display the second page
def second_page():
    st.header("DAILY SOUL CONNECT")

    # Retrieve the selected message
    selected_message = messages[st.session_state.message_index]

    # Display the selected message
    st.write(f"Here is the message for you today: {selected_message['message']}")
    st.image(selected_message['image'], use_column_width=True)
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

# Message data with updated image paths
messages = [
    {
        "message": "Desire",
        "practice": "Dear friend, today could you set a clear direction for yourself, short-term or long-term?",
        "example": "For example, try something new you've always wanted to try, like a new recipe or hobby.",
        "image": "message_image/Desire.webp"
    },
    {
        "message": "Faith",
        "practice": "Dear friend, believe in yourself today and know that you are capable of achieving great things?",
        "example": "For instance, remind yourself of a past achievement whenever self-doubt creeps in.",
        "image": "message_image/Faith.webp"
    },
    {
        "message": "Autosuggestion",
        "practice": "Dear friend, repeat positive affirmations today to remind yourself of your potential?",
        "example": "For example, start your day by saying, 'I am confident and capable.'",
        "image": "message_image/Autosuggestion.webp"
    },
    {
        "message": "Knowledge",
        "practice": "Dear friend, take some time today to learn something new that excites you?",
        "example": "For instance, watch a documentary or read an article on a topic that interests you.",
        "image": "message_image/Knowledge.webp"
    },
    {
        "message": "Imagination",
        "practice": "Dear friend, visualize your success today and imagine the steps to get there?",
        "example": "For example, picture yourself achieving a goal and think about the actions that will lead you there.",
        "image": "message_image/Imagination.webp"
    },
    {
        "message": "Planning",
        "practice": "Dear friend, create a detailed plan today for achieving one of your goals?",
        "example": "For example, break down a project into smaller tasks and set deadlines for each.",
        "image": "message_image/Planning.webp"
    },
    {
        "message": "Decision",
        "practice": "Dear friend, make a prompt and firm decision today on something you've been contemplating?",
        "example": "For instance, decide what book to read next or which hobby to start.",
        "image": "message_image/Decision.webp"
    },
    {
        "message": "Persistence",
        "practice": "Dear friend, keep pushing forward today, even if you face obstacles?",
        "example": "For example, if you're learning a new skill, practice a little every day, even if it’s challenging.",
        "image": "message_image/Persistence.webp"
    },
    {
        "message": "Mastermind",
        "practice": "Dear friend, collaborate with someone today to brainstorm new ideas and solutions?",
        "example": "For example, have a coffee chat with a friend to discuss and exchange ideas on a common interest.",
        "image": "message_image/Mastermind.webp"
    },
    {
        "message": "Sex Transmutation",
        "practice": "Dear friend, channel your energy into a creative or productive activity today?",
        "example": "For example, if you feel restless, use that energy to start a new project or workout.",
        "image": "message_image/Sex_transmutation.webp"
    },
    {
        "message": "Subconscious",
        "practice": "Dear friend, trust your instincts and intuition today; they will guide you?",
        "example": "For example, if something feels right or wrong, take a moment to listen to that feeling.",
        "image": "message_image/Subconscious.webp"
    },
    {
        "message": "Brain",
        "practice": "Dear friend, take some time today to think deeply and reflect on your thoughts?",
        "example": "For example, spend a few minutes journaling your thoughts and feelings.",
        "image": "message_image/Brain.webp"
    },
    {
        "message": "Sixth Sense",
        "practice": "Dear friend, listen to your inner voice and intuition today for guidance?",
        "example": "For instance, if you have a gut feeling about a decision, give it consideration.",
        "image": "message_image/Sixth_sense.webp"
    },
    {
        "message": "Outwit Fear",
        "practice": "Dear friend, face one of your fears boldly today and take a step towards overcoming it?",
        "example": "For example, if you're afraid of public speaking, try speaking up in a small group setting.",
        "image": "message_image/Outwit_fear.webp"
    },
    {
        "message": "Power",
        "practice": "Dear friend, leverage your strengths today and focus on what you do best?",
        "example": "For example, if you're great at organizing, plan out your week ahead.",
        "image": "message_image/Power.webp"
    },
    {
        "message": "Connecting Link",
        "practice": "Dear friend, stay mindful and present today, and appreciate the moments as they come?",
        "example": "For example, take a walk outside and notice the beauty around you.",
        "image": "message_image/Connecting_link.webp"
    }
]

# Main app logic
if 'page' not in st.session_state:
    st.session_state.page = "main_page"

if st.session_state.page == "main_page":
    main_page()
elif st.session_state.page == "second_page":
    second_page()