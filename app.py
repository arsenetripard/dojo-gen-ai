from pathlib import Path
import streamlit as st
from audio_recorder_streamlit import audio_recorder

from src.utils.get_transcription import get_transcription
from src.utils.get_answer import get_answer

st.header("AI Note Taker 🤖")
st.write("Welcome to the AI Note Taker! 🎉")

AUDIO_PATH = Path("audio.wav")

audio_bytes = audio_recorder(pause_threshold=5)
if audio_bytes:
    with open(AUDIO_PATH, mode="wb") as f:
        f.write(audio_bytes)
    st.audio(audio_bytes, format="audio/wav")

    st.write("Transcription:")
    transcription = get_transcription(AUDIO_PATH)
    st.write(transcription)

    question = st.text_input(label="Question", placeholder="Enter a question please")
    if question:
        message = f"""
        Context: {transcription},
        Question: {question}
        Answer:
        """
        answer = get_answer(message)
        st.write(answer)
