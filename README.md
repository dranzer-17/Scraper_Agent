# AI Web Scraper with Free Gemini API 🕵️‍♂️

A simple, reliable web scraper built with Streamlit that uses Google's free Gemini AI to extract structured information from websites. No complex dependencies, no headaches - just clean, working code.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.20+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🤖 **Free Gemini AI Integration** - Uses Google's free Gemini API (no paid subscriptions needed)
- 🎯 **Smart Content Extraction** - Extracts specific information based on your prompts
- 🚀 **Simple & Reliable** - No complex dependencies or browser automation
- 📊 **Progress Tracking** - Real-time progress updates during scraping
- ⚙️ **Customizable Options** - Adjust character limits, temperature, and more
- 💾 **Export Results** - Download extracted data as text files
- 🔐 **Environment Variables** - Secure API key management
- 🎨 **User-Friendly Interface** - Clean Streamlit web interface

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-web-scraper.git
cd ai-web-scraper
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Your Free Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key (completely free)
3. Copy your API key

### 4. Set Up Environment Variables (Recommended)
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📋 Requirements

Create a `requirements.txt` file with these dependencies:
```
streamlit>=1.20.0
google-generativeai>=0.3.0
requests>=2.25.0
beautifulsoup4>=4.9.0
python-dotenv>=0.19.0
```

## 🎯 How to Use

1. **Enter your Gemini API key** (or set it in `.env` file)
2. **Specify what to extract** - Be specific about the information you want
   - Example: "Extract all product names and prices"
   - Example: "Get contact information and email addresses"
3. **Enter the target URL** - The website you want to scrape
4. **Choose your model** - `gemini-1.5-flash` is fastest and free
5. **Click "Start Scraping"** - Wait for the AI to process the content
6. **View and download results** - Get structured data extracted by AI

## 💡 Example Use Cases

- **E-commerce**: Extract product names, prices, and descriptions
- **Research**: Gather contact information from business directories
- **Content Analysis**: Extract headings, topics, and key information
- **Data Collection**: Structure unorganized web content
- **Competitive Analysis**: Monitor competitor websites

## ⚙️ Advanced Options

- **Character Limit**: Control how much content to process (1,000-10,000 chars)
- **Include Links**: Optionally include webpage links in the analysis
- **AI Temperature**: Adjust creativity vs. focus (0.0 = focused, 1.0 = creative)

## 🔧 Troubleshooting

### Common Issues and Solutions

**"Failed to fetch webpage":**
- Verify the URL is correct and starts with `http://` or `https://`
- Some websites block automated requests
- Try the website in your browser first to ensure it's accessible

**"Gemini API error":**
- Check that your API key is correct and active
- Verify you haven't exceeded your free quota
- Make sure the API key has proper permissions

**Empty or minimal results:**
- Be more specific in your extraction prompt
- Try increasing the character limit in advanced options
- The website might not contain the information you're looking for

**Slow performance:**
- Reduce the character limit for faster processing
- Use `gemini-1.5-flash` model (fastest)
- Process smaller websites first

## 🏗️ Project Structure

```
ai-web-scraper/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Report bugs** - Open an issue if you find any problems
2. **Suggest features** - Have ideas for improvements?
3. **Submit pull requests** - Fix bugs or add new features
4. **Improve documentation** - Help make the README clearer

### Development Setup
```bash
# Fork the repository and clone your fork
git clone https://github.com/yourusername/ai-web-scraper.git
cd ai-web-scraper

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Make your changes and test them
streamlit run app.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google AI** - For providing the free Gemini API
- **Streamlit** - For the amazing web app framework
- **BeautifulSoup** - For reliable HTML parsing
- **Community** - For feedback and contributions

## 🔗 Links

- **Google AI Studio**: https://makersuite.google.com/app/apikey
- **Streamlit Documentation**: https://docs.streamlit.io
- **Gemini API Documentation**: https://ai.google.dev/docs

## ⭐ Star This Project

If you find this project helpful, please consider giving it a star on GitHub! It helps others discover the project and motivates continued development.

---

**Built with ❤️ using Streamlit and Google Gemini AI**

*No complex dependencies, no browser automation headaches, just simple and reliable web scraping powered by AI.*