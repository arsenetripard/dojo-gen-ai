from pathlib import Path
import streamlit as st
from audio_recorder_streamlit import audio_recorder

st.header("AI Note Taker 🤖")
st.write("Welcome to the AI Note Taker! 🎉")

AUDIO_PATH = Path("audio.wav")

audio_bytes = audio_recorder(pause_threshold=5)
if audio_bytes:
    with open(AUDIO_PATH, mode="wb") as f:
        f.write(audio_bytes)
    st.audio(audio_bytes, format="audio/wav")
