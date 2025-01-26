# app.py
import os
from dotenv import load_dotenv
import streamlit as st
from uuid import uuid4
from langchain_core.messages import AIMessage, HumanMessage
from graph import invoke_our_graph
from st_callable_util import get_streamlit_cb

# Load environment variables
load_dotenv()

# Set page configuration with dark theme
st.set_page_config(
    page_title="Azza Man",
    page_icon="azaman7.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark theme with red accents
st.markdown("""
    <style>
    :root {
        --primary-red: #FF0000;
        --dark-bg: #0A0A0A;
        --card-bg: #1A1A1A;
    }
    
    .stApp {
        background-color: var(--dark-bg);
        color: white;
    }
    
    .stChatInput input {
        background-color: var(--card-bg) !important;
        color: white !important;
        border: 1px solid var(--primary-red) !important;
    }
    
    .stButton>button {
        background-color: var(--primary-red) !important;
        color: white !important;
        border: none;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        opacity: 0.8;
        transform: scale(1.05);
    }
    
    .header {
        text-align: center;
        padding: 20px;
        border-bottom: 2px solid var(--primary-red);
    }
    
    .assistant-message {
        background: var(--card-bg);
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid var(--primary-red);
        margin: 1rem 0;
    }
    
    .user-message {
        background: #2A2A2A;
        padding: 1rem;
        border-radius: 10px;
        border-right: 4px solid #FFFFFF;
        margin: 1rem 0;
    }
    
    .sidebar .sidebar-content {
        background: var(--dark-bg) !important;
        border-right: 1px solid var(--primary-red);
    }
    
    .intro-text {
        font-size: 1.1rem;
        color: #CCCCCC;
        line-height: 1.6;
    }
    
    .feature-list li {
        margin: 1rem 0;
        padding: 1rem;
        background: var(--card-bg);
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

def landing_page():
    st.markdown("<h1 style='color: #FF0000; text-align: center; font-family: Arial;'>AZZA MAN</h1>", unsafe_allow_html=True)
    st.markdown("#### <div style='text-align: center; color: #FFFFFF; margin-bottom: 2rem;'>AI-Powered Financial Guardian</div>", 
                unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image('azaman7.png', use_container_width=True)  # Updated here

    st.markdown("""
        <div class="intro-text">
        <p>Welcome to your personal financial command center.</p>
        """, unsafe_allow_html=True)

    if not os.getenv('GROQ_API_KEY'):
        with st.sidebar:
            st.markdown("### 🔑 Access Control")
            api_key = st.text_input("Enter GROQ API Key:", type="password")
            if api_key:
                os.environ["GROQ_API_KEY"] = api_key
                st.success("Authentication successful!")
            else:
                st.error("Authorization required for deployment")
                st.stop()

    st.markdown("""
        
        <div class="feature-list">
        <ul>
            <li>🔥 <span style="color: var(--primary-red);">Budget Warfare:</span> Strategic allocation of financial resources</li>
            <li>💸 <span style="color: var(--primary-red);">Expense Recon:</span> Real-time tracking and analysis</li>
            <li>📈 <span style="color: var(--primary-red);">Wealth Ops:</span> Advanced financial forecasting</li>
        </ul>
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <small>Developed by </small>
            <a href="https://www.linkedin.com/in/chinonsoodiaka/" 
               style="color: var(--primary-red); text-decoration: none; font-weight: bold;">
               🅱🅻🅰🆀
            </a>
        </div>
        </div>
    """, unsafe_allow_html=True)

    if not os.getenv('GROQ_API_KEY'):
        with st.sidebar:
            st.markdown("### 🔑 Access Control")
            api_key = st.text_input("Enter GROQ API Key:", type="password")
            if api_key:
                os.environ["GROQ_API_KEY"] = api_key
                st.success("Authentication successful!")
            else:
                st.error("Authorization required for deployment")
                st.stop()

def chat_interface():
    # Initialize session state
    if "user_id" not in st.session_state:
        st.session_state.user_id = str(uuid4())
        st.session_state.messages = [
            AIMessage(content="**SYSTEM ONLINE**. How can I assist you today?")
        ]

    # Chat container
    chat_container = st.container()
    with chat_container:
        # Display message history
        for msg in st.session_state.messages:
            if isinstance(msg, AIMessage):
                st.markdown(f"""
                    <div class="assistant-message">
                        <div style="color: var(--primary-red); font-weight: bold;">AZZA:</div>
                        {msg.content}
                    </div>
                """, unsafe_allow_html=True)
            elif isinstance(msg, HumanMessage):
                st.markdown(f"""
                    <div class="user-message">
                        <div style="color: white; font-weight: bold;">YOU:</div>
                        {msg.content}
                    </div>
                """, unsafe_allow_html=True)

    # Input and processing
    if prompt := st.chat_input("Send secure message..."):
        # Add user message
        st.session_state.messages.append(HumanMessage(content=prompt))
        
        try:
            # Process through LangGraph
            with st.spinner("**ENCRYPTING TRANSMISSION**"):
                st_callback = get_streamlit_cb(chat_container)
                response = invoke_our_graph(
                        st_messages=st.session_state.messages,  
                        callables=[st_callback]
                    )


            # Update state
            if "messages" in response:
                st.session_state.messages = response["messages"]
                st.rerun()

        except Exception as e:
            st.error(f"🔴 SYSTEM ERROR: {str(e)}")
            st.stop()

def main():
    # Navigation
    if "page" not in st.session_state:
        st.session_state.page = "landing"

    if st.session_state.page == "landing":
        landing_page()
        if st.button("**INITIALIZE SYSTEM**", use_container_width=True):
            st.session_state.page = "chat"
            st.rerun()
            
    elif st.session_state.page == "chat":
        chat_interface()
        if st.sidebar.button("◀ RETURN TO BASE", type="secondary"):
            st.session_state.page = "landing"
            st.rerun()

if __name__ == "__main__":
    main()