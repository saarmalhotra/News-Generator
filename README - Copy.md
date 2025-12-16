# 📰 Daily News Briefing Generator

AI-powered news briefing application using Tavily Search API and Claude AI.

## 📋 What This App Does

- Searches the web for latest news using Tavily API
- Uses Claude AI to curate and summarize news articles
- Provides personalized news briefings based on your interests
- Displays 5-7 top headlines with summaries
- Shows source articles with direct links

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8 or higher installed
- Internet connection
- VS Code (or any text editor)

### Step-by-Step Installation

1. **Create a new folder for your project**
```bash
   mkdir news-briefing-app
   cd news-briefing-app
```

2. **Create all 4 files** (app.py, requirements.txt, .gitignore, README.md)

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Run the application**
```bash
   streamlit run app.py
```

5. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to that URL

## 📁 Required Files

Create these 4 files in your project folder:

1. **app.py** - Main application code
2. **requirements.txt** - Python dependencies
3. **.gitignore** - Files to ignore in Git
4. **README.md** - This documentation file

## 🎯 How to Use the App

1. Open the app in your browser
2. In the sidebar:
   - Your Tavily API key is pre-filled
   - Enter topics (e.g., "AI, technology, sports")
   - Select reading time (5/10/15 minutes)
   - Choose region preference
3. Click "Generate News Briefing"
4. Wait for results (usually 10-20 seconds)
5. Read your personalized news digest!

## 🌐 Deploy to the Internet (FREE)

### Option 1: Streamlit Cloud (Recommended)

1. **Create GitHub account** (if you don't have one)
   - Go to github.com
   - Sign up for free

2. **Install Git**
```bash
   git --version
```

3. **Initialize Git in your project**
```bash
   cd news-briefing-app
   git init
   git add .
   git commit -m "Initial commit"
```

4. **Create a new repository on GitHub**
   - Go to github.com
   - Click "+" → "New repository"
   - Name it: `news-briefing-app`
   - Click "Create repository"

5. **Push your code to GitHub**
```bash
   git remote add origin https://github.com/YOUR_USERNAME/news-briefing-app.git
   git branch -M main
   git push -u origin main
```

6. **Deploy on Streamlit Cloud**
   - Go to share.streamlit.io
   - Click "Sign in with GitHub"
   - Click "New app"
   - Select your repository: `news-briefing-app`
   - Main file path: `app.py`
   - Click "Deploy"!

7. **Your app is live!**
   - URL will be: `https://YOUR_USERNAME-news-briefing-app.streamlit.app`

## 🔑 API Keys

### Tavily API Key
- Already included in the code
- Free tier: 1,000 searches per month

### Claude API
- No API key needed when running in claude.ai
- Built-in authentication handled automatically

## ⚙️ Customization

### Change Topics
Edit the sidebar input to add your favorite news topics

### Adjust Search Results
In `app.py`, line 120, change `"max_results": 7` to any number (1-10)

### Modify Reading Time
In `app.py`, line 78, add more options to the selectbox

## 🐛 Troubleshooting

### App won't start
```bash
pip install --upgrade streamlit requests
```

### "Module not found" error
```bash
pip install -r requirements.txt
```

### Tavily API error
- Check your internet connection
- Verify you haven't exceeded monthly limit

## 📊 Features

✅ Real-time news search  
✅ AI-powered curation  
✅ Customizable topics  
✅ Multiple time options  
✅ Region filtering  
✅ Source article links  
✅ Beautiful UI  
✅ Mobile responsive  

## 🎉 Enjoy!

You now have a fully functional AI-powered news briefing app!

Made with ❤️ by Saar Malhotra