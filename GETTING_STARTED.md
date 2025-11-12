# Getting Started - French to English Voice Translator

## 🚀 Two Ways to Deploy for Tomorrow's Call

### Method 1: Run Locally (10 minutes) - RECOMMENDED FOR SPEED

**Best for:** Quick setup, sharing your screen during the call

1. **Download all files** from this conversation
2. **Create folder structure:**
   ```
   french-to-english-translator/
   ├── app.py
   ├── requirements.txt
   ├── .gitignore
   └── .streamlit/
       ├── config.toml
       └── secrets.toml
   ```

3. **Get OpenAI API Key:**
   - Go to https://platform.openai.com/api-keys
   - Sign in (or create account)
   - Click "Create new secret key"
   - Copy the key (starts with `sk-...`)
   - Add $5-10 credit if new account

4. **Install dependencies:**

   **Windows:**
   ```cmd
   pip install -r requirements.txt
   ```

   **Mac/Linux:**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Configure API Key:**
   - Create `.streamlit` folder
   - Copy `secrets.toml.example` to `.streamlit/secrets.toml`
   - Edit `.streamlit/secrets.toml`:
     ```toml
     OPENAI_API_KEY = "sk-your-actual-key-here"
     ```

6. **Run the app:**
   ```bash
   streamlit run app.py
   ```

7. **Test it:**
   - Browser opens to http://localhost:8501
   - Click microphone button
   - Say something in French
   - See English translation

8. **For the call:**
   - Keep app running
   - Share your screen
   - Everyone can see translations

---

### Method 2: Deploy to Cloud (20 minutes) - BEST FOR TEAM ACCESS

**Best for:** Multiple team members accessing independently

1. **Prepare files:**
   - Download all files
   - Keep folder structure intact

2. **Create GitHub repository:**
   - Go to https://github.com
   - Click "New repository"
   - Name it: `french-english-translator`
   - Set to Public or Private
   - Don't initialize with README

3. **Upload files:**

   **Option A: Via GitHub website (easiest)**
   - Click "uploading an existing file"
   - Drag all files (EXCEPT secrets.toml if you created it)
   - Create `.streamlit` folder by:
     - Click "Create new file"
     - Type `.streamlit/config.toml`
     - Paste config.toml contents
     - Commit
   - Repeat for secrets.toml.example
   - Commit files

   **Option B: Via Git command line**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/french-english-translator.git
   git push -u origin main
   ```

4. **Deploy on Streamlit Cloud:**
   - Go to https://share.streamlit.io
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Main file: `app.py`
   - Click "Advanced settings"
   - In "Secrets" section, paste:
     ```toml
     OPENAI_API_KEY = "sk-your-actual-key-here"
     ```
   - Click "Deploy"

5. **Share with team:**
   - Wait 2-5 minutes for deployment
   - Copy the URL (e.g., `yourapp.streamlit.app`)
   - Send to team members
   - Everyone can access independently

---

## 📋 Pre-Call Testing (IMPORTANT!)

Test 30 minutes before your call:

1. ✅ Open the app
2. ✅ Click microphone (allow browser access)
3. ✅ Record French test message
4. ✅ Verify English translation appears
5. ✅ Check translation history works
6. ✅ Test multiple recordings
7. ✅ Verify internet connection stable

---

## 💡 Usage During the Call

### Best Practices:

1. **Position microphone** near French speaker
2. **Record in chunks:** 10-20 seconds each
3. **Click to start** → speaker talks → **click to stop**
4. **Wait 3-5 seconds** for translation
5. **Read translation** to non-French speakers
6. **History is saved** - scroll down to review

### Tips:

- Use **headphones** to avoid feedback
- **Minimize background noise**
- **Speak clearly** toward microphone
- **Pause between speakers** for separate recordings
- **Keep recordings short** for faster processing

### Troubleshooting Live:

**Microphone not working?**
→ Refresh page, check browser permissions

**Slow translation?**
→ Keep recordings under 15 seconds, check internet

**API Error?**
→ Verify API key, check OpenAI credits, refresh page

---

## 💰 Cost Breakdown

- **OpenAI Whisper API:** $0.006 per minute
- **1-hour call:** ~$0.36
- **Very affordable!**

Add $5-10 to OpenAI account before the call.

---

## 🆘 Backup Plan

If app fails during call:

1. **Google Translate app** (phone voice mode)
2. **Google Translate website** (type French → English)
3. **Record call** and translate later
4. **Ask speaker to slow down**

---

## 📞 Tomorrow's Call Checklist

**Morning of call:**
- [ ] Open app 30 min early
- [ ] Test one recording
- [ ] Check OpenAI credits
- [ ] Have backup (Google Translate) ready
- [ ] Share link with team

**During call:**
- [ ] Keep app open
- [ ] Record 10-20 sec chunks
- [ ] Allow time for translation
- [ ] Save important translations (screenshot)

---

## 📁 File Download Summary

**Essential Files (must have):**
1. app.py
2. requirements.txt
3. config.toml (put in .streamlit folder)

**Setup Guides (highly recommended):**
4. QUICKSTART.md
5. DEPLOYMENT_CHECKLIST.md
6. This file (GETTING_STARTED.md)

**Optional but useful:**
7. README.md (full docs)
8. .gitignore (for Git)
9. setup.bat / setup.sh (auto-install scripts)

---

## ✅ You're Ready!

Choose your deployment method, follow the steps, test thoroughly, and you'll be ready for tomorrow's call!

**Questions?** Check QUICKSTART.md or README.md for detailed answers.

**Good luck with your call! 🎉**
