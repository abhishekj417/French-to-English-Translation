# Deployment Checklist ✓

## Before Tomorrow's Call

### Essential Steps (Must Do)

- [ ] Get OpenAI API key from https://platform.openai.com/api-keys
- [ ] Test microphone works in your browser
- [ ] Choose deployment method (Local or Cloud)

### Option A: Local Deployment (Fastest - 10 minutes)

- [ ] Download all project files to a folder
- [ ] Open terminal in that folder
- [ ] Run: `pip install -r requirements.txt`
- [ ] Create `.streamlit/secrets.toml` with your API key
- [ ] Run: `streamlit run app.py`
- [ ] Test with sample French speech
- [ ] Bookmark the local URL (http://localhost:8501)
- [ ] Plan to share your screen during call

### Option B: Cloud Deployment (For team - 20 minutes)

- [ ] Create GitHub account (if needed)
- [ ] Create new repository on GitHub
- [ ] Upload all project files
- [ ] Go to share.streamlit.io
- [ ] Connect GitHub repository
- [ ] Add API key in secrets section
- [ ] Wait for deployment (2-5 minutes)
- [ ] Test the live URL
- [ ] Share URL with team members
- [ ] Ask team to bookmark the URL

## During Setup - Testing

- [ ] Record a test message in French
- [ ] Verify French transcription is accurate
- [ ] Verify English translation appears
- [ ] Check translation history works
- [ ] Test clear history button
- [ ] Verify multiple recordings work

## Final Pre-Call Check (Morning of Call)

- [ ] Open the app 30 minutes before call
- [ ] Test microphone access granted
- [ ] Do one test recording
- [ ] Check internet connection is stable
- [ ] Have backup plan (Google Translate app)
- [ ] Share app link with non-French speakers

## During the Call - Best Practices

- [ ] Position microphone close to French speaker
- [ ] Record in 10-20 second chunks
- [ ] Allow 3-5 seconds for translation
- [ ] Read translations aloud if needed
- [ ] Keep history open for reference
- [ ] Have notepad ready for important translations

## Emergency Backup

If app fails during call:
1. Use phone's Google Translate app (voice mode)
2. Have someone type French → English on google.com/translate
3. Ask French speaker to speak slower
4. Record call and translate after

## Cost Check

- [ ] Verify OpenAI account has credits ($5+ recommended)
- [ ] Expected cost: $0.006/minute (~$0.36 for 1 hour)

---

**Remember: Test everything BEFORE the call!**
