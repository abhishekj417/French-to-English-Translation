# Quick Start Guide - French to English Voice Translator

## For Tomorrow's Call - Fast Setup

### Step 1: Get OpenAI API Key (5 minutes)
1. Go to https://platform.openai.com/api-keys
2. Sign in or create account
3. Click "Create new secret key"
4. Copy the key (starts with sk-...)

### Step 2A: Run Locally (Recommended for immediate use)

1. Download all files to a folder
2. Open terminal/command prompt in that folder
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create `.streamlit/secrets.toml` file with:
   ```
   OPENAI_API_KEY = "your-key-here"
   ```
5. Run the app:
   ```
   streamlit run app.py
   ```
6. Share your screen during the call!

### Step 2B: Deploy to Streamlit Cloud (For team access)

1. Create GitHub repository
2. Upload all files (drag and drop)
3. Go to https://share.streamlit.io
4. Click "New app"
5. Connect your GitHub repo
6. In "Advanced settings" → "Secrets", add:
   ```
   OPENAI_API_KEY = "your-key-here"
   ```
7. Click "Deploy"
8. Share the URL with team members!

## During the Call

1. Open the app in your browser
2. Allow microphone access
3. When someone speaks French:
   - Click the microphone button
   - Let them speak (10-20 seconds)
   - Click button again to stop
   - English translation appears in 3-5 seconds
4. All translations are saved in the history below

## Troubleshooting

**Microphone not working?**
- Refresh the page
- Check browser permissions
- Try Chrome or Edge browser

**Slow processing?**
- Keep recordings under 20 seconds
- Check internet connection
- OpenAI API might be busy (wait 10 seconds)

**API Error?**
- Verify API key is correct
- Check OpenAI account has credits
- Refresh the page

## Cost
- ~$0.006 per minute of audio
- 1 hour call = ~$0.36
- Very affordable!

## Tips for Best Results
- Use headphones to avoid feedback
- Minimize background noise
- Speak clearly toward microphone
- Pause between speakers
- Keep each recording 10-20 seconds

---

**Need help? All instructions are in README.md**

**Test it before the call to ensure everything works!**
