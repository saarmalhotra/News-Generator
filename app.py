import streamlit as st
import requests
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Daily News Briefing",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(to bottom right, #eff6ff, #e0e7ff, #f3e8ff);
    }
    .news-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .source-card {
        background: #f8fafc;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #6366f1;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #1e293b;'>📰 Daily News Briefing Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 18px;'>Powered by Tavily Search & Claude AI</p>", unsafe_allow_html=True)
st.markdown("---")

# Initialize session state
if 'briefing' not in st.session_state:
    st.session_state.briefing = None
if 'articles' not in st.session_state:
    st.session_state.articles = []

# Sidebar inputs
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # API Keys
    tavily_api_key = st.text_input(
        "Tavily API Key",
        value="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",
        type="password",
        help="Your Tavily API key"
    )
    
    st.markdown("---")
    
    # User inputs
    topics = st.text_input(
        "📝 Topics of Interest",
        placeholder="e.g., AI, technology, sports, business",
        help="Enter topics separated by commas"
    )
    
    reading_time = st.selectbox(
        "⏱️ Reading Time",
        options=["5", "10", "15"],
        index=1,
        help="How many minutes do you have?"
    )
    
    region = st.selectbox(
        "🌍 Region Preference",
        options=["Global", "United States", "Europe", "Asia", "India"],
        help="Choose your preferred news region"
    )

# Main content
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_button = st.button("🚀 Generate News Briefing", use_container_width=True, type="primary")

# Function to search with Tavily
def search_tavily(query, api_key):
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": "basic",
        "include_answer": False,
        "include_raw_content": False,
        "max_results": 7
    }
    
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()

# Function to generate briefing with Claude
def generate_briefing_with_claude(search_results, topics, reading_time, region):
    # Format search results
    search_context = "\n".join([
        f"[{idx + 1}] {result['title']}\nURL: {result['url']}\nContent: {result['content']}\n"
        for idx, result in enumerate(search_results)
    ])
    
    # Claude API call
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "anthropic-version": "2023-06-01"
    }
    
    payload = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 4000,
        "messages": [
            {
                "role": "user",
                "content": f"""You are a news curator creating a personalized daily news briefing.

SEARCH RESULTS FROM TAVILY:
{search_context}

USER PREFERENCES:
- Topics of interest: {topics}
- Reading time: {reading_time} minutes
- Region: {region}
- Current date/time: {datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')}

Please create a well-formatted news briefing with:

1. **Today's Date and Time** at the top
2. **5-7 Top Headlines** from the search results above
3. For each headline:
   - The title (as a heading)
   - A brief 2-3 sentence summary
   - Category/topic tag in brackets [Category]
4. Organize by topic categories (e.g., Technology, Business, Sports, etc.)
5. Keep it concise for {reading_time} minutes of reading

Format it as a clean, professional news digest. Use markdown formatting for better readability."""
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    
    # Extract text from response
    briefing_text = ""
    for block in data.get("content", []):
        if block.get("type") == "text":
            briefing_text += block.get("text", "")
    
    return briefing_text

# Generate briefing when button is clicked
if generate_button:
    if not topics:
        st.error("❌ Please enter at least one topic of interest!")
    elif not tavily_api_key:
        st.error("❌ Please enter your Tavily API key!")
    else:
        with st.spinner("🔍 Searching for latest news..."):
            try:
                # Search with Tavily
                search_query = f"latest news {topics} {region if region != 'Global' else ''} today"
                search_results = search_tavily(search_query, tavily_api_key)
                
                if not search_results.get('results'):
                    st.error("❌ No news found for your topics. Try different keywords.")
                else:
                    st.session_state.articles = search_results['results']
                    
                    # Generate briefing with Claude
                    with st.spinner("🤖 Claude is curating your briefing..."):
                        briefing = generate_briefing_with_claude(
                            search_results['results'],
                            topics,
                            reading_time,
                            region
                        )
                        st.session_state.briefing = briefing
                    
                    st.success("✅ Your briefing is ready!")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Display results
if st.session_state.briefing:
    st.markdown("---")
    
    # Display briefing
    st.markdown("## 📰 Your News Briefing")
    st.markdown(st.session_state.briefing)
    
    st.markdown("---")
    
    # Display source articles
    if st.session_state.articles:
        st.markdown("## 📚 Source Articles")
        
        for idx, article in enumerate(st.session_state.articles):
            with st.expander(f"📄 {article['title']}", expanded=False):
                st.markdown(f"**Summary:** {article['content'][:300]}...")
                st.markdown(f"[🔗 Read full article]({article['url']})")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #64748b; padding: 20px;'>
        <p>Made with ❤️ using Streamlit, Tavily Search & Claude AI</p>
        <p style='font-size: 12px;'>Your personalized AI-powered news digest</p>
    </div>
""", unsafe_allow_html=True)