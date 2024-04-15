import streamlit as st
import pandas as pd
import numpy as np
import base64
from time import sleep

st.set_page_config(
    page_icon = "🤖",
    page_title = "Eden's In-vehicle",
    layout = "wide",
)

st.header("Music : In-vehicle music and video player")
st.subheader("Let's start")
st.video('./video/CoopernautIntro.mp4')

# def autoplay_audio(file_path: str, is_auto = True):
#     with open(file_path, "rb") as f:
#         data = f.read()
#         b64 = base64.b64encode(data).decode()
#         if is_auto:
#             md = f"""
#                 <audio controls autoplay="true">
#                 <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
#                 </audio>
#                 <script>
#                      window.onload = function() {{
#                      var audio = document.getElementById('audio');
#                      audio.play(controls=False);
#                  }};
#                  </script>
#                 """
#         else:
#             md = f"""
#                 <audio controls autoplay="false">
#                 <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
#                 </audio>
#                 """

#     return md

# def autoplay_video(video_file, is_auto = True):
#     with open(video_file, "rb") as f:
#         data = f.read()
#         b64 = base64.b64encode(data).decode()
#         if is_auto:
#             md = f"""
#                 <video controls width=320 height=240 autoplay>
#                 <source src="data:video/mp4;base64,{b64}">
#                 </video>
#                 """
#         else:
#             md = f"""
#                 <video controls width=320 height=240 autoplay muted>
#                 <source src="data:video/mp4;base64,{b64}">
#                 </video>
#                 """
#     return md


def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_html = f"""
            <audio id="audio" controls autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                Your browser does not support the audio element.
            </audio>
            <script>
                window.onload = function() {{
                    var audio = document.getElementById('audio');
                    audio.play(controls=False);
                }};
            </script>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

        # md = f"""
        #     <audio controls autoplay="true">
        #     <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        #     </audio>
        #     """
        # st.markdown(
        #     md,
        #     unsafe_allow_html=True,
        # )


st.write("# Audio Playing List!")
autoplay_audio("./music/classic.mp3")

#audio_file = open('/Users/eden/Downloads/test.mp3', 'rb')
#st.audio(audio_file.read(), format='audio/mp3')
