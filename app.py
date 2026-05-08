import streamlit as st
from PIL import Image
import io
import os
import time
from dotenv import load_dotenv

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import azure.cognitiveservices.speech as speechsdk


# ================= CONFIG =================
load_dotenv()

VISION_KEY = os.getenv("VISION_KEY")
VISION_ENDPOINT = os.getenv("VISION_ENDPOINT")
SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION")

st.set_page_config(page_title="Readify AI", page_icon="🎧", layout="wide")


# ================= STYLE =================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Title */
.title {
    text-align: center;
    font-size: 2.7rem;
    font-weight: 800;
    background: linear-gradient(90deg,#06b6d4,#3b82f6,#a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg,#06b6d4,#3b82f6);
    color: white;
    border-radius: 10px;
    font-weight: bold;
    width: 100%;
}

/* Metrics */
.metric {
    font-size: 1.2rem;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# ================= FUNCTIONS =================

def extract_text(img_bytes):
    client = ComputerVisionClient(
        VISION_ENDPOINT,
        CognitiveServicesCredentials(VISION_KEY)
    )

    stream = io.BytesIO(img_bytes)
    res = client.read_in_stream(stream, raw=True)
    op_id = res.headers["Operation-Location"].split("/")[-1]

    while True:
        result = client.get_read_result(op_id)
        if result.status not in ["notStarted", "running"]:
            break
        time.sleep(1)

    text = ""
    if result.status == "succeeded":
        for page in result.analyze_result.read_results:
            for line in page.lines:
                text += line.text + "\n"

    return text


def text_to_speech(text):
    config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    synthesizer = speechsdk.SpeechSynthesizer(config, None)
    result = synthesizer.speak_text_async(text).get()
    return result.audio_data


# ================= UI =================

st.markdown("<div class='title'>🎧 Readify AI</div>", unsafe_allow_html=True)
st.markdown("<center>Upload → Extract → Listen</center>", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

# Upload
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    uploaded = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])
    run = st.button("✨ Process")
    clear = st.button("🧹 Clear")
    st.markdown("</div>", unsafe_allow_html=True)

# Preview
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    if uploaded:
        st.image(uploaded, use_container_width=True)
    else:
        st.info("Image preview will appear here")
    st.markdown("</div>", unsafe_allow_html=True)


# Clear
if clear:
    st.session_state.clear()


# Process
if run and uploaded:
    with st.spinner("Processing..."):
        try:
            text = extract_text(uploaded.getvalue())

            if not text.strip():
                st.warning("No text detected")
            else:
                audio = text_to_speech(text)

                tab1, tab2 = st.tabs(["📄 Text", "🔊 Audio"])

                with tab1:
                    st.markdown("<div class='card'>", unsafe_allow_html=True)

                    st.text_area("Extracted Text", text, height=250)

                    colA, colB = st.columns(2)
                    colA.metric("Words", len(text.split()))
                    colB.metric("Characters", len(text))

                    st.code(text)  # copy-friendly

                    st.markdown("</div>", unsafe_allow_html=True)

                with tab2:
                    st.markdown("<div class='card'>", unsafe_allow_html=True)

                    st.audio(audio, format="audio/wav")

                    st.download_button(
                        "⬇ Download Audio",
                        data=audio,
                        file_name="readify.wav",
                        mime="audio/wav"
                    )

                    st.markdown("</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")