import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from graph import invoke_our_graph
from st_callable_util import get_streamlit_cb  # Utility function to get a Streamlit callback handler with context

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(page_title="Azza Man", page_icon="azaman7.png", layout="centered")  # Use logo as page icon

# Custom CSS for dark theme and enhanced styling
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;  /* Black background */
        color: white;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
    }
    .stTextInput>div>input, .stTextArea>div>textarea {
        background-color: #2e2e2e;
        color: white;
    }
    .stMarkdown {
        color: lightgray;
    }
    .header {
        text-align: center;
        padding: 20px;
    }
    .logo {
        width: 50%;
        max-width: 600px;
    }
    .intro-text {
        font-size: 16px;
        color: lightgray;
        text-align: center;
        margin: 20px 0;
    }
    .title {
        color: red;  /* Red title */
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Landing Page
# Landing Page
def landing_page():
    st.markdown("<h1 style='color: red; font-weight: bold;'>Azza Man</h1>", unsafe_allow_html=True)  # Bold and red title
    st.markdown("##### Personal Financial Assistant :dollar::credit_card::chart:")
    st.image('azaman7.png', width=600)  # Logo image

    # Introduction text
    st.markdown("""
        <p class='intro-text'>
        Managing finances can be overwhelming, but with <span style='color: red; font-weight: bold;'>Azza Man</span>'s dynamic AI-driven workflow, the process becomes stress-free. 
        Here’s how <span style='color: red;'>Azza Man</span> can assist you to stay on top of your finances like never before:
        </p>
        <ul class='intro-list'>
            <li><strong><span style='color: yellow;'>Effortless Budgeting</span>:</strong> Create your monthly budget with ease.</li>
            <li><strong><span style='color: yellow;'>Expense Tracking</span>:</strong> Keep track of your expenses seamlessly.</li>
            <li><strong><span style='color: yellow;'>Valuable Insights</span>:</strong> Gain invaluable insights into your financial landscape.</li>
            <li><strong><span style='color: yellow;'>AI-Powered Assistance</span>:</strong> Benefit from the power of artificial intelligence to simplify your financial journey.</li>
        </ul>
        <p class='intro-text'>
            Connect with the creator: <a href="https://www.linkedin.com/in/chinonsoodiaka/" style="color: #00ff00; text-decoration: none;">🅱🅻🅰🆀</a>.
        </p>
    """, unsafe_allow_html=True)



    # API Key Setup
    if not os.getenv('GROQ_API_KEY'):
        st.sidebar.header("API Key Setup")
        api_key = st.sidebar.text_input(label="API Key", type="password", label_visibility="collapsed")
        os.environ["GROQ_API_KEY"] = api_key
        if not api_key:
            st.info("Please enter your GROQ API Key in the sidebar.")
            st.stop()

# Chat Page
def chat_page():
    if "messages" not in st.session_state:
        st.session_state["messages"] = [AIMessage(content="Country person, what would you like to do?")]

    # Loop through all messages in the session state and render them as a chat
    for msg in st.session_state.messages:
        if isinstance(msg, AIMessage):
            st.chat_message("assistant").markdown(f"<div style='color: #00ff00;'>{msg.content}</div>", unsafe_allow_html=True)
        elif isinstance(msg, HumanMessage):
            st.chat_message("user").markdown(f"<div style='color: #ffcc00;'>{msg.content}</div>", unsafe_allow_html=True)

    # Takes new input in chat box from user and invokes the graph
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to session state
        st.session_state.messages.append(HumanMessage(content=prompt))
        
        # Display user message
        st.chat_message("user").markdown(f"<div style='color: #ffcc00;'>{prompt}</div>", unsafe_allow_html=True)

        # Process the AI's response and handle graph events using the callback mechanism
        st_callback = get_streamlit_cb(st.container())
        response = invoke_our_graph(st.session_state.messages, [])

        # Debug: Ensure the response contains expected content
        print("Graph response:", response)

        # Ensure the last AI message is properly appended to the session state
        final_message = response["messages"][-1].content  # Access the last message content
        st.session_state.messages.append(AIMessage(content=final_message))
        
        # Display the final AI message
        st.chat_message("assistant").markdown(f"<div style='color: #00ff00;'>{final_message}</div>", unsafe_allow_html=True)  # Display the final AI message explicitly

# Main application logic
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page:", ["Landing Page", "Chat"], label_visibility= "visible")

    if page == "Landing Page":
        landing_page()
    elif page == "Chat":
        chat_page()

if __name__ == "__main__":
    main()
