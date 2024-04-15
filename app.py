import streamlit as st
import pandas as pd
import numpy as np
import base64
from time import sleep

st.set_page_config(
    page_icon = "🤖",
    page_title = "test",
    layout = "wide",
)

st.header("Music : work on homepage")
st.subheader("sssss")
st.video('./CoopernautIntro.mp4')

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


st.write("# Auto-playing Audio!")
autoplay_audio("/test.mp3")

#audio_file = open('/Users/eden/Downloads/test.mp3', 'rb')
#st.audio(audio_file.read(), format='audio/mp3')
