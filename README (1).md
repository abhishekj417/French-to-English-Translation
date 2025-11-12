# French to English Voice Translator 🎙️

Real-time voice translation tool for converting French speech to English text during meetings and calls.

## Features

- 🎤 **Real-time audio recording** via browser microphone
- 🗣️ **French speech transcription** using OpenAI Whisper
- 🌐 **Automatic translation** to English
- 📝 **Translation history** for the entire session
- 💻 **User-friendly interface** with Streamlit

## Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Microphone-enabled device

### 2. Installation

Clone or download this repository:

```bash
git clone <your-repo-url>
cd french-to-english-translator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

**Option A: Using Streamlit Secrets (Recommended for deployment)**

Create `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "your-api-key-here"
```

**Option B: Using Environment Variable (Local development)**

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or on Windows:
```cmd
set OPENAI_API_KEY=your-api-key-here
```

### 4. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Deployment on Streamlit Cloud

### Step 1: Push to GitHub

1. Create a new repository on GitHub
2. Upload all files (app.py, requirements.txt, README.md)
3. Push your code

### Step 2: Deploy on Streamlit

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Connect your GitHub repository
4. Select the repository and branch
5. Set main file path: `app.py`
6. Click "Advanced settings" → "Secrets"
7. Add your OpenAI API key:
   ```
   OPENAI_API_KEY = "your-api-key-here"
   ```
8. Click "Deploy"

Your app will be live in minutes!

## How to Use

1. **Allow microphone access** when prompted by your browser
2. **Click the microphone button** to start recording
3. **Speak in French** clearly into your microphone
4. **Click the button again** to stop recording
5. **Wait a few seconds** for transcription and translation
6. **View the English translation** in the right column
7. **Check history** below for all translations in the session

## Tips for Best Results

- Speak clearly and at a moderate pace
- Minimize background noise during recording
- Use headphones to avoid audio feedback
- Keep recordings under 30 seconds for faster processing
- Ensure stable internet connection

## Troubleshooting

### Microphone not working
- Check browser permissions for microphone access
- Try refreshing the page
- Test microphone in browser settings

### API errors
- Verify your OpenAI API key is correct
- Check you have sufficient credits in your OpenAI account
- Ensure internet connection is stable

### Slow processing
- Keep audio clips shorter (10-20 seconds)
- Check your internet speed
- OpenAI API processing time varies by load

## Cost Information

This app uses OpenAI's Whisper API:
- **Pricing:** $0.006 per minute of audio
- **Example:** 1 hour of translation = ~$0.36

[Check current pricing](https://openai.com/pricing)

## Technical Stack

- **Frontend:** Streamlit
- **Audio Recording:** audio-recorder-streamlit
- **Speech Recognition:** OpenAI Whisper API
- **Translation:** OpenAI Whisper API (built-in translation)

## Project Structure

```
french-to-english-translator/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
└── .streamlit/
    └── secrets.toml      # API keys (not committed)
```

## Support

For issues or questions:
- Check the troubleshooting section above
- Review OpenAI Whisper documentation
- Verify Streamlit deployment logs

## License

MIT License - feel free to use and modify for your needs.

---

**Built for reliable real-time French-to-English translation during meetings and calls.**
