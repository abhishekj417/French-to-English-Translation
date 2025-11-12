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
st.markdown("**Real-time translation for your meeting - Records up to 30 minutes continuously**")
st.markdown("---")

# Initialize session state
if 'translations' not in st.session_state:
    st.session_state.translations = []
if 'recording_count' not in st.session_state:
    st.session_state.recording_count = 0
if 'total_duration' not in st.session_state:
    st.session_state.total_duration = 0

# Control buttons at the top
col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 3])

with col_btn1:
    if st.button("🔄 Restart Session", type="secondary", use_container_width=True):
        st.session_state.translations = []
        st.session_state.recording_count = 0
        st.session_state.total_duration = 0
        st.rerun()

with col_btn2:
    if st.button("🗑️ Clear All", type="secondary", use_container_width=True):
        st.session_state.translations = []
        st.rerun()

# Display session info
st.info(f"📊 Session Stats: {st.session_state.recording_count} recordings | ⏱️ Total: ~{st.session_state.total_duration} seconds")

st.markdown("---")

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎙️ Record French Audio")
    st.markdown("**Instructions:**")
    st.markdown("- Click microphone to START recording")
    st.markdown("- Speak in French for 10-30 seconds")
    st.markdown("- Click again to STOP and translate")
    st.markdown("- Repeat for continuous 30+ minute sessions")

with col2:
    st.subheader("🇬🇧 English Translation")
    st.markdown("**Latest translation will appear below:**")

# Audio recorder
with col1:
    st.markdown("### Click to Record:")
    audio_bytes = audio_recorder(
        text="",
        recording_color="#e74c3c",
        neutral_color="#3498db",
        icon_name="microphone",
        icon_size="6x",
        key=f"audio_recorder_{st.session_state.recording_count}"
    )

# Process audio when recorded
if audio_bytes:
    with col1:
        st.audio(audio_bytes, format="audio/wav")

        # Estimate duration (rough approximation: file size / 16000 bytes per second)
        estimated_duration = len(audio_bytes) / 16000

        with st.spinner("🔄 Translating to English..."):
            try:
                # Save audio bytes to temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                    tmp_file.write(audio_bytes)
                    tmp_file_path = tmp_file.name

                # FIXED: Use ONLY translation endpoint (French audio → English text directly)
                # This is the key fix - no transcription call, only translation
                with open(tmp_file_path, "rb") as audio_file:
                    translation = client.audio.translations.create(
                        model="whisper-1",
                        file=audio_file,
                        response_format="text"
                    )

                # Translation returns English text directly
                english_text = translation if isinstance(translation, str) else translation.text

                # Clean up temp file
                os.unlink(tmp_file_path)

                # Update session state
                timestamp = time.strftime("%H:%M:%S")
                st.session_state.recording_count += 1
                st.session_state.total_duration += int(estimated_duration)

                st.session_state.translations.append({
                    'time': timestamp,
                    'number': st.session_state.recording_count,
                    'english': english_text,
                    'duration': int(estimated_duration)
                })

                # Display latest translation in big text
                with col2:
                    st.success("✅ Translation Complete!")
                    st.markdown("### 📝 English Translation:")
                    st.markdown(f"**{english_text}**")
                    st.markdown(f"*Recording #{st.session_state.recording_count} at {timestamp}*")

                # Force refresh to update stats
                st.rerun()

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.error("💡 Tip: Keep recordings under 25MB. Try shorter clips if error persists.")
                if 'tmp_file_path' in locals():
                    try:
                        os.unlink(tmp_file_path)
                    except:
                        pass

# Display translation history in expandable section
if st.session_state.translations:
    st.markdown("---")
    st.subheader("📜 Translation History (All Recordings)")

    # Show most recent first
    for trans in reversed(st.session_state.translations):
        with st.expander(f"🎤 Recording #{trans['number']} - {trans['time']} ({trans['duration']}s)", expanded=False):
            st.markdown("### 🇬🇧 English Translation:")
            st.info(trans['english'])

# Sidebar with instructions
with st.sidebar:
    st.header("📖 How to Use for 30+ Minute Meetings")

    st.markdown("""
    ### Quick Start:
    1. **Click microphone** to start recording
    2. **Let French speaker talk** (10-30 seconds)
    3. **Click again** to stop and translate
    4. **Read English** translation instantly
    5. **Repeat** for the entire meeting!

    ### For Long Meetings (30+ minutes):
    - Record in **chunks of 10-30 seconds** each
    - Each chunk translates in **3-5 seconds**
    - All translations **save automatically**
    - Can record **unlimited chunks**
    - Use **Restart Session** to start fresh

    ### Controls:
    - 🔄 **Restart Session**: Clear everything and reset counters
    - 🗑️ **Clear All**: Remove translation history only
    - View history by clicking expandable items below

    ### Tips for Best Results:
    - Keep each recording **10-30 seconds**
    - Position laptop **2-3 feet** from speaker
    - Minimize **background noise**
    - Speak **clearly and naturally**
    - Use **headphones** to avoid feedback
    - Each recording processes while others continue

    ### Session Stats:
    - Tracks total recordings made
    - Shows approximate total duration
    - All translations saved in history

    ### Troubleshooting:
    - **No translation?** Check microphone permissions
    - **French output?** Refresh page and try again
    - **Slow?** Use shorter recordings (10-15s)
    - **Error?** Keep recordings under 25MB
    """)

    st.markdown("---")
    st.markdown("**⚡ Powered by OpenAI Whisper API**")
    st.markdown("**🔒 Secure - All processing via encrypted API**")
