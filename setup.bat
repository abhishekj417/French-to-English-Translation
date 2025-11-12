@echo off
echo ========================================
echo French to English Voice Translator
echo Setup Script
echo ========================================
echo.

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo NEXT STEPS:
echo 1. Create .streamlit folder (if not exists)
echo 2. Copy secrets.toml.example to .streamlit/secrets.toml
echo 3. Edit .streamlit/secrets.toml with your OpenAI API key
echo 4. Run: streamlit run app.py
echo.
echo Press any key to exit...
pause > nul
