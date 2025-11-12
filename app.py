import streamlit as st
import os
from openai import OpenAI
import tempfile
from audio_recorder_streamlit import audio_recorder
import time

# Page configuration
st.set_page_config(
    page_title="French to English Voice Translator",
    page_icon="🎙️",
    layout="wide"
)

# Initialize OpenAI client
@st.cache_resource
def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", "")
    if not api_key:
        st.error("⚠️ OpenAI API key not found. Please add it to Streamlit secrets.")
        st.stop()
    return OpenAI(api_key=api_key)

client = get_openai_client()

# Title and instructions
st.title("🎙️ French to English Voice Translator")
st.markdown("**Real-time translation for your meeting**")
st.markdown("---")

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🇫🇷 French Audio Input")
    st.markdown("Click the microphone to record French speech")

with col2:
    st.subheader("🇬🇧 English Translation Output")
    st.markdown("Translation will appear here")

# Initialize session state for translation history
if 'translations' not in st.session_state:
    st.session_state.translations = []

# Audio recorder
with col1:
    audio_bytes = audio_recorder(
        text="Click to record",
        recording_color="#e74c3c",
        neutral_color="#3498db",
        icon_name="microphone",
        icon_size="3x"
    )

# Process audio when recorded
if audio_bytes:
    with col1:
        st.audio(audio_bytes, format="audio/wav")

        with st.spinner("🔄 Transcribing and translating..."):
            try:
                # Save audio bytes to temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                    tmp_file.write(audio_bytes)
                    tmp_file_path = tmp_file.name

                # Transcribe French audio
                with open(tmp_file_path, "rb") as audio_file:
                    transcript = client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file,
                        language="fr"
                    )

                french_text = transcript.text

                # Translate French audio to English
                with open(tmp_file_path, "rb") as audio_file:
                    translation = client.audio.translations.create(
                        model="whisper-1",
                        file=audio_file
                    )

                english_text = translation.text

                # Clean up temp file
                os.unlink(tmp_file_path)

                # Store in session state
                timestamp = time.strftime("%H:%M:%S")
                st.session_state.translations.append({
                    'time': timestamp,
                    'french': french_text,
                    'english': english_text
                })

                # Display latest translation
                with col2:
                    st.success("✅ Translation complete!")
                    st.markdown(f"**French:** {french_text}")
                    st.markdown(f"**English:** {english_text}")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                if 'tmp_file_path' in locals():
                    try:
                        os.unlink(tmp_file_path)
                    except:
                        pass

# Display translation history
if st.session_state.translations:
    st.markdown("---")
    st.subheader("📝 Translation History")

    # Reverse to show newest first
    for i, trans in enumerate(reversed(st.session_state.translations)):
        with st.expander(f"🕐 {trans['time']} - Translation {len(st.session_state.translations) - i}"):
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("**🇫🇷 French:**")
                st.info(trans['french'])
            with col_b:
                st.markdown("**🇬🇧 English:**")
                st.success(trans['english'])

    # Clear history button
    if st.button("🗑️ Clear History"):
        st.session_state.translations = []
        st.rerun()

# Sidebar with instructions
with st.sidebar:
    st.header("📖 How to Use")
    st.markdown("""
    1. **Click the microphone** button to start recording
    2. **Speak in French** clearly into your microphone
    3. **Click again** to stop recording
    4. **Wait** for transcription and translation
    5. **View results** in the right column

    ### Tips for Best Results:
    - Speak clearly and at a moderate pace
    - Minimize background noise
    - Keep recordings under 30 seconds for faster processing
    - Use headphones to avoid feedback

    ### Troubleshooting:
    - Make sure your browser allows microphone access
    - Check your internet connection
    - Refresh the page if issues persist
    """)

    st.markdown("---")
    st.markdown("**Powered by OpenAI Whisper API**")
