import streamlit as st
import google.generativeai as genai

# -------------------------------
# ✅ 1. Gemini API Configuration
# -------------------------------
API_KEY = "AIzaSyANazzuCzpuxWsmV8ojZtayjEuqSSwYK38"  # 🔴 Replace with your Gemini API Key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-pro")

# -------------------------------
# ✅ 2. Streamlit UI
# -------------------------------
st.set_page_config(page_title="YouTube Channel Insights (Gemini)", page_icon="📊", layout="wide")
st.title("📊 Advanced YouTube Channel Insights")
st.write("Enter a YouTube Channel URL to get detailed analytics powered by **Gemini AI**.")

channel_url = st.text_input("🔗 Enter YouTube Channel URL:", placeholder="https://www.youtube.com/@Google")

# -------------------------------
# ✅ 3. Function to Generate Insights via Gemini
# -------------------------------
def analyze_channel_with_gemini(channel_url):
    prompt = f"""
    You are an advanced YouTube analytics expert.
    Analyze the YouTube channel at {channel_url} and provide detailed insights in a **well-structured, user-friendly report**.
    DO NOT return JSON or code. Write as a human-readable report with headings and bullet points.

    Include:
    1. **Channel Overview** – name, description, niche, estimated popularity and subscriber count and owner name is known
    2. **Video Performance** – estimated average views, engagement level, and possible earnings range.
    3. **Audience Insights** – probable age group, location trends, and interests.
    4. **Growth Trends** – subscriber and view count growth pattern (historical trend if possible).
    5. **Top Content** – list 5 most popular videos or playlists with short descriptions.

    Use publicly available assumptions and general trends if exact data is unavailable.
    Make it visually appealing with markdown styling.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating insights: {e}"

# -------------------------------
# ✅ 4. Run Analysis
# -------------------------------
if st.button("Analyze"):
    if not channel_url:
        st.warning("⚠️ Please enter a valid YouTube channel URL.")
    else:
        with st.spinner("Generating insights with Gemini..."):
            insights = analyze_channel_with_gemini(channel_url)
            st.markdown(insights)
