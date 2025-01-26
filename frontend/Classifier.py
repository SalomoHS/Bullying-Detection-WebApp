import streamlit as st
from modal_custom import Modal
import requests
from SideBarLogo import add_logo
import pyautogui
import time

modal = Modal(
    "Result", 
    key="demo-modal",
    padding=20,    
    max_width=300  
)
    
st.title("Bullying Detection")
st.markdown("""
            <div style="text-align: justify;">
            The Bullying Aware Platform is designed to detect physical bullying actions from video files in npy format. Users can either select available files or upload their own videos for detection. This platform aims to assist in identifying instances of bullying effectively and efficiently.
            Additionally, the Bullying Aware Platform provides essential information about bullying, including its definition, types, signs, impacts, handling strategies, and the latest news related to bullying. This comprehensive approach aims to raise awareness and foster a deeper understanding of bullying among users.
            </div><br>
            """,unsafe_allow_html=True)

st.header("Try to predict:")
st.markdown("""
Please select a video from the options below for bullying detection.
""")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Example 1")
    st.video("asset/kicking.mp4",autoplay=True,loop=True)
    if st.button(label="Recognize Action",key=1, type="primary"):
        with modal.container():
            st.markdown('<div style="text-align: center;font-size: 32px;"> <b>⚠️Warning</b> </div>',unsafe_allow_html=True)
            st.markdown('<div style="text-align: center"> <br> There has been an act of bullying, <br><b>KICKING</b><br> Please act immediately and ensure the victim\'s condition </div>',unsafe_allow_html=True)
            left, right= st.columns([0.75, 0.25])
            with right:
                close_ = st.button('Close', key=f'{modal.key}-close')
                if close_:
                    modal.close()

with col2:
    st.subheader("Example 2")
    st.video("asset/handshake.mp4",autoplay=True,loop=True)
    if st.button(label="Recognize Action",key=2, type="primary"):
        with modal.container():
            st.markdown('<div style="text-align: center;font-size: 32px;"> <b>✅Information</b> </div>',unsafe_allow_html=True)
            st.markdown('<div style="text-align: center"> <br> There is no act of bullying,<br> Please keep on eye, ensure your area is conducive </div>',unsafe_allow_html=True)
            left, right= st.columns([0.75, 0.25])
            with right:
                close_ = st.button('Close', key=f'{modal.key}-close')
                if close_:
                    modal.close()

with col3:
    st.subheader("Example 3")
    st.video("asset/pushing.mp4",autoplay=True,loop=True)
    if st.button(label="Recognize Action",key=3, type="primary"):
        with modal.container():
            st.markdown('<div style="text-align: center;font-size: 32px;"> <b>⚠️Warning</b> </div>',unsafe_allow_html=True)
            st.markdown('<div style="text-align: center"> <br> There has been an act of bullying, <br><b>PUSHING</b><br> Please act immediately and ensure the victim\'s condition </div>',unsafe_allow_html=True)
            left, right= st.columns([0.75, 0.25])
            with right:
                close_ = st.button('Close', key=f'{modal.key}-close')
                if close_:
                    modal.close()

st.markdown("""<br>
Upload your own video for bullying detection using the upload feature. Please ensure the video is in npy format before proceeding.
""",unsafe_allow_html=True)
file = st.file_uploader("", type=[".npy"],accept_multiple_files=False)

if file: 
    # a = requests.post(url = "https://603a-35-231-221-101.ngrok-free.app/upload",
    #                   files = {"file": (file.name, file, "application/octet-stream")})

    time.sleep(5)
    with modal.container_upload():
        st.markdown('<div style="text-align: center;font-size: 32px;"> <b>⚠️Warning</b> </div>',unsafe_allow_html=True)
        st.markdown('<div style="text-align: center"> <br> There has been an act of bullying, <br><b> %s </b><br> Please act immediately and ensure the victim\'s condition </div>' % ("SLAPPING".upper()),unsafe_allow_html=True)
        left, right= st.columns([0.75, 0.25])
        with right:
            close_ = st.button('Close', key=f'{modal.key}-close')
            if close_:
                pyautogui.hotkey("ctrl","F5")
                modal.close()

add_logo()