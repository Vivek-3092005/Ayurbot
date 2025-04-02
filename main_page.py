import streamlit as st
import brain
import random

home = False

if "count" not in st.session_state:
    st.session_state.count=0
    st.session_state.a = 0
    st.session_state.b = 0
    st.session_state.c = 0
    st.session_state.messages = []
    st.session_state.questions = brain.questions

def ayurbot():
    page_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image:     ;
    background-size: cover;
    }        
    </style>
    """
    st.markdown(
        page_bg,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h2 style="text-align: center; color: #D3D3D3; font-family: 'Times New Roman';">AYURBOT</h1>
        """,
        unsafe_allow_html=True
    )
    st.subheader('', divider='rainbow')
    #st.markdown(
    #    """
    #     <h5 style="color: #D3D3D3,font-weight: normal;">Hi there! I am Chatbot specific to determine the Prakriti of an individual. So now lets determine your Prakriti!</h5>
    #    """,
    #    unsafe_allow_html=True
    #)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Send a message"):
        st.session_state.messages.append({"role":"USER","content": prompt})
        with st.chat_message("USER"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            bot_response=""
            prompt = prompt.lower()

            if prompt in brain.c_hi:
                bot_response = brain.bot_intro

            elif st.session_state.count < len(st.session_state.questions):
                bot_response = st.session_state.questions[st.session_state.count]
                logic(prompt)
                st.session_state.count += 1
            else:
                bot_response = result()
                reset_state()

        message_placeholder.markdown(bot_response)
        st.session_state.messages.append({"role": "assistant","content": bot_response})

def result():
    if st.session_state.a > st.session_state.b and st.session_state.a > st.session_state.c:
        return brain.vata
    elif st.session_state.b > st.session_state.c and st.session_state.b > st.session_state.a:
        return brain.pitta
    else:
        return brain.kapha

def logic(user_input):
    if user_input in brain.ans_1:
        st.session_state.a += 1
    elif user_input in brain.ans_2:
        st.session_state.b += 1
    elif user_input in brain.ans_3:
        st.session_state.c += 1


def reset_state():
    st.session_state.count = 0
    st.session_state.a = 0
    st.session_state.b = 0
    st.session_state.c = 0
    st.session_state.messages = []

def main():
    page_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url(https://images.pexels.com/photos/66997/pexels-photo-66997.jpeg?cs=srgb&dl=pexels-no-name-66997.jpg&fm=jpg);
    height = 50%;
    background-position: center;
    background-size: cover;
    }        
    </style>
    """
    st.markdown(
        page_bg,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h1 style="text-align: center; color: black; font-family: 'Times New Roman', Times, serif;">PRAKRITI</h1>
        """,
        unsafe_allow_html=True
    )
    st.subheader('', divider='rainbow')
    st.markdown(
        """
        <h5 style="color: black;">It is a term used in traditional Indian philosophy, particularly in Ayurveda, to describe the inherent constitution or nature of an individual.</h5>
        <h5 style="color: black;">In Ayurveda, it is believed that every person has a unique combination of three fundamental energies or doshas known as VATA, PITTA and KAPHA, which make up their Prakriti.</h5>
        <h5 style="color: black;">These doshas represent different combinationof five elements (Earth, Water, Fire, Air and Ether) and play physical and physcological characteristics as well as their susceptibility to certain health issues.</h5>
        
        """,
        unsafe_allow_html=True
    )
   
col1,col2,col3 = st.columns([1,2,5])
with col1:
    if st.button("HOME"):
        st.session_state.page = 'home'
with col2:
    if st.button("AYURBOT"):
        st.session_state.page = 'ayurbot'
    
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if st.session_state.page == 'home':
    main()

if st.session_state.page == 'ayurbot':
    home = True
    ayurbot()
