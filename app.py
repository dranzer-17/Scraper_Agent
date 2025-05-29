import streamlit as st
import os
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Streamlit app title
st.title("AI Web Scraper with Free Gemini API 🕵️‍♂️")
st.caption("Simple and reliable web scraping using BeautifulSoup + Gemini AI")

# Input fields
default_api_key = os.getenv("GEMINI_API_KEY", "")
api_key = st.text_input("Enter your Gemini API key:", 
                       type="password", 
                       value=default_api_key,
                       help="Get your free API key from: https://makersuite.google.com/app/apikey")

prompt = st.text_input("Enter the information you want to extract:", 
                      placeholder="e.g., Extract all product names and prices")

source_url = st.text_input("Enter the source URL:", 
                          placeholder="https://example.com")

# Model selection
model_choice = st.selectbox(
    "Select Gemini Model:",
    ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"],
    index=0,
    help="gemini-1.5-flash is fastest and completely free"
)

# Advanced options
with st.expander("⚙️ Advanced Options"):
    max_chars = st.slider("Maximum characters to process:", 1000, 10000, 5000,
                         help="Longer text = more comprehensive but slower processing")
    
    include_links = st.checkbox("Include links in extraction", value=False)
    
    temperature = st.slider("AI Creativity (Temperature):", 0.0, 1.0, 0.1,
                           help="Lower = more focused, Higher = more creative")

def scrape_website(url):
    """Scrape website content using requests and BeautifulSoup"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "header", "footer"]):
            script.decompose()
        
        # Get text content
        text_content = soup.get_text()
        
        # Clean up text
        lines = (line.strip() for line in text_content.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text_content = ' '.join(chunk for chunk in chunks if chunk)
        
        # Get links if requested
        links = []
        if include_links:
            for link in soup.find_all('a', href=True):
                link_text = link.get_text().strip()
                link_url = link['href']
                if link_text and link_url:
                    links.append(f"{link_text}: {link_url}")
        
        return text_content, links, None
        
    except requests.exceptions.RequestException as e:
        return None, [], f"Failed to fetch webpage: {str(e)}"
    except Exception as e:
        return None, [], f"Error parsing webpage: {str(e)}"

def extract_with_gemini(text_content, links, user_prompt, api_key, model, temp):
    """Extract information using Gemini AI"""
    try:
        # Configure Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model)
        
        # Prepare content
        content_to_analyze = text_content[:max_chars]
        
        if links and include_links:
            links_text = "\n".join(links[:20])  # Limit to 20 links
            content_to_analyze += f"\n\nLinks found:\n{links_text}"
        
        # Create extraction prompt
        extraction_prompt = f"""
Please extract the following information from the webpage content below:

EXTRACTION REQUEST: {user_prompt}

WEBPAGE CONTENT:
{content_to_analyze}

Please provide a clear, structured response with the requested information. 
If the information is not available, please state that clearly.
"""
        
        # Generate response
        response = model.generate_content(
            extraction_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=temp,
                max_output_tokens=2048,
            )
        )
        
        return response.text, None
        
    except Exception as e:
        return None, f"Gemini API error: {str(e)}"

# Main scraping button
if st.button("🚀 Start Scraping"):
    if not all([prompt, source_url, api_key]):
        missing = []
        if not prompt: missing.append("extraction prompt")
        if not source_url: missing.append("source URL") 
        if not api_key: missing.append("API key")
        st.error(f"❌ Please provide: {', '.join(missing)}")
    else:
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Step 1: Scrape website
        status_text.text("📡 Fetching webpage...")
        progress_bar.progress(25)
        
        text_content, links, scrape_error = scrape_website(source_url)
        
        if scrape_error:
            st.error(f"❌ {scrape_error}")
        else:
            # Step 2: Process with Gemini
            status_text.text("🤖 Processing with Gemini AI...")
            progress_bar.progress(75)
            
            result, gemini_error = extract_with_gemini(
                text_content, links, prompt, api_key, model_choice, temperature
            )
            
            progress_bar.progress(100)
            status_text.text("✅ Complete!")
            
            if gemini_error:
                st.error(f"❌ {gemini_error}")
                
                # Show helpful error messages
                if "api" in gemini_error.lower() and "key" in gemini_error.lower():
                    st.info("💡 Please check that your Gemini API key is correct and active.")
                elif "quota" in gemini_error.lower():
                    st.info("💡 You may have exceeded your API quota. Try again later or check your API limits.")
            else:
                # Success! Show results
                st.success("✅ Scraping completed successfully!")
                
                # Display results
                st.subheader("🎯 Extracted Information:")
                st.write(result)
                
                # Show additional info
                with st.expander("📊 Scraping Details"):
                    st.write(f"**Characters processed:** {len(text_content):,}")
                    st.write(f"**Links found:** {len(links)}")
                    st.write(f"**Model used:** {model_choice}")
                    if links and include_links:
                        st.write("**Links included in analysis**")
                
                # Option to download results
                st.download_button(
                    "💾 Download Results",
                    data=result,
                    file_name=f"scraped_data_{int(time.time())}.txt",
                    mime="text/plain"
                )
        
        # Clean up progress indicators
        time.sleep(1)
        status_text.empty()
        progress_bar.empty()

# Instructions and Setup
st.markdown("---")
st.subheader("📋 Setup Instructions")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 1. Get Free Gemini API Key")
    st.markdown("Visit: [Google AI Studio](https://makersuite.google.com/app/apikey)")
    
    st.markdown("### 2. Create .env File (Optional)")
    st.code("GEMINI_API_KEY=your_api_key_here")

with col2:
    st.markdown("### 3. Install Simple Dependencies")
    st.code("""
pip install streamlit python-dotenv
pip install google-generativeai
pip install requests beautifulsoup4
    """)

# Tips and Troubleshooting
st.subheader("💡 Tips for Better Results")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Extraction Prompts:**
    - "Extract all product names and prices"
    - "Get contact information and addresses"
    - "Find all headings and main topics"
    - "Extract table data in structured format"
    """)

with col2:
    st.markdown("""
    **Best Practices:**
    - Test with simple, public websites first
    - Be specific about what you want
    - Use lower character limits for faster processing
    - Check that URLs are accessible
    """)

st.subheader("🔧 Troubleshooting")

with st.expander("❌ Common Issues and Solutions"):
    st.markdown("""
    **"Failed to fetch webpage":**
    - Check if URL is correct and accessible
    - Some sites block automated requests
    - Try adding 'https://' if missing
    
    **"Gemini API error":**
    - Verify your Gemini API key is correct
    - Check if you have API quota remaining
    - Make sure the key has proper permissions
    
    **"No useful content extracted":**
    - The website might be JavaScript-heavy
    - Try a different website for testing
    - Increase character limit in advanced options
    
    **Empty or minimal results:**
    - Be more specific in your extraction prompt
    - The content might not contain what you're looking for
    - Try including links in the analysis
    """)

# Status indicators
st.markdown("---")
if default_api_key:
    st.success("✅ API key successfully loaded from .env file")
else:
    st.info("💡 Enter your API key above or create a .env file")

st.caption("🚀 Powered by Google Gemini AI - Reliable & Simple Web Scraping")
st.caption("⚡ No complex dependencies - just requests + BeautifulSoup + Gemini!")