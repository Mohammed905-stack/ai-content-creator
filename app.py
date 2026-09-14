import streamlit as st
import google.generativeai as genai

# 1. Configure Gemini API Credentials
# Replace YOUR_API_KEY with your actual Gemini API key, or use st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 2. Initialize Gemini 3.6 Flash model
model = genai.GenerativeModel("gemini-3.6-flash")

# 3. Application User Interface
st.title("AI Content Generator")
st.write("Generate high-quality copy for different platforms with a single click.")

topic = st.text_input("Enter Topic", placeholder="e.g., World evolving with AI")

content_type = st.selectbox(
    "Content Type",
    [
        "LinkedIn Post",
        "Instagram Caption",
        "Twitter Post",
        "Professional Email",
        "Blog Outline"
    ]
)

# Project Challenge: Tone Selector
tone = st.selectbox(
    "Select Tone",
    ["Professional", "Funny", "Formal", "Friendly"]
)

# 4. Generate Content on Button Click
if st.button("Generate"):
    if topic:
        prompt = f"""You are a professional content writer.
Create a {content_type} in a {tone} tone.
Topic: {topic}"""
        with st.spinner("Generating content..."):
            response = model.generate_content(prompt)
            st.markdown("### Generated Content:")
            st.write(response.text)
    else:
        st.warning("Please enter a topic first.")
