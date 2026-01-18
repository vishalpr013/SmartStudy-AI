# 📚 SmartStudy-AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)
![Google Gemini](https://img.shields.io/badge/Google-Gemini%20AI-4285F4.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**An AI-Powered Study Material Generator using Google Gemini AI**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Deployment](#-deployment) • [Tech Stack](#-tech-stack)

</div>

---

## 🌟 Overview

**SmartStudy-AI** is an intelligent study material generator that leverages Google's Gemini AI to transform any text or PDF document into comprehensive, structured study materials. Whether you're a student preparing for exams or an educator creating learning resources, SmartStudy-AI automatically generates summaries, notes, MCQs, flashcards, and practice questions.

## ✨ Features

- 📄 **PDF Upload Support** - Extract and process text from PDF documents
- ✍️ **Text Input** - Paste any text content directly
- 📝 **Comprehensive Study Material Generation**:
  - Concise Summary (150-200 words)
  - Structured Notes with headings and bullet points
  - 10 Multiple Choice Questions (MCQs) with answers
  - 10 Flashcards (Question-Answer format)
  - 10 Short Answer Questions
- 🤖 **Powered by Google Gemini AI** - Latest generative AI technology
- 🎨 **User-Friendly Interface** - Built with Streamlit
- ⚡ **Fast Processing** - Quick content generation
- 🔒 **Secure API Management** - Environment-based secret management

## 🎬 Demo

### How It Works:

1. **Choose Input Method**: Upload a PDF or paste text
2. **Submit Content**: Click "Generate Study Material"
3. **Get Results**: Receive structured study materials instantly

### Sample Output Structure:

```
✅ CONCISE SUMMARY
A comprehensive paragraph summarizing the key concepts...

✅ STRUCTURED NOTES
├── Main Topic 1
│   ├── Subtopic A
│   └── Subtopic B
└── Main Topic 2

✅ MULTIPLE CHOICE QUESTIONS (10)
Q1. What is...?
A) Option 1
B) Option 2
C) Option 3
D) Option 4
Correct Answer: B

✅ FLASHCARDS (10)
Q: What is the definition of...?
A: A brief, precise answer...

✅ SHORT ANSWER QUESTIONS (10)
1. Explain the concept of...
2. Describe the relationship between...
```

## 🛠️ Tech Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core Programming Language | 3.9+ |
| **Streamlit** | Web Framework for UI | Latest |
| **Google Generative AI** | AI Model (Gemini Flash) | 0.8.6 |
| **PyPDF2** | PDF Text Extraction | Latest |
| **google-auth** | API Authentication | 2.47.0 |
| **httplib2** | HTTP Client | 0.31.1 |

### Additional Dependencies:
- `google-api-python-client` - Google API interactions
- `google-ai-generativelanguage` - Gemini AI language models
- `grpcio` - gRPC framework
- `certifi`, `charset-normalizer`, `idna` - HTTP/SSL support
- `packaging`, `jsonschema` - Utilities

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.9 or higher** installed
- **Google Gemini API Key** (Get it from [Google AI Studio](https://makersuite.google.com/app/apikey))
- **pip** package manager
- **Virtual environment** (recommended)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SmartStudy-AI.git
cd SmartStudy-AI
```

### 2. Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python -m venv myenv
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.streamlit` folder and `secrets.toml` file:

**Windows (PowerShell):**
```powershell
mkdir .streamlit
New-Item -Path .streamlit\secrets.toml -ItemType File
```

**Add your API key to `.streamlit/secrets.toml`:**
```toml
GEMINI_API_KEY = "your-google-gemini-api-key-here"
```

⚠️ **Important**: Never commit `secrets.toml` to version control. Add it to `.gitignore`:
```
.streamlit/secrets.toml
```

## 💻 Usage

### Running Locally

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Using the Application

1. **Select Input Type**: Choose between "Upload PDF" or "Paste Text"
2. **Provide Content**:
   - For PDF: Click "Browse files" and select your PDF
   - For Text: Paste your study material in the text area
3. **Generate**: Click the "Generate Study Material" button
4. **Review**: View your generated study materials

## 📁 Project Structure

```
SmartStudy-AI/
├── app.py                      # Main Streamlit application
├── check_models.py             # Utility to check available Gemini models
├── requirements.txt            # Python dependencies
├── myenv/                      # Virtual environment (not in git)
├── .streamlit/
│   └── secrets.toml           # API keys (not in git)
├── .gitignore                 # Git ignore file
└── README.md                  # This file
```

## 🔧 Configuration

### Model Selection

The app uses `gemini-flash-latest` model by default. To change the model, edit `app.py`:

```python
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
```

Check available models:
```bash
python check_models.py
```

### Customizing Study Material Format

Edit the `system_prompt` in `app.py` to customize:
- Number of questions (default: 10)
- Summary length (default: 150-200 words)
- Output sections and formatting

## 📊 Use Cases

- 📖 **Students**: Generate study guides from lecture notes or textbooks
- 👨‍🏫 **Teachers**: Create quiz materials and flashcards
- 📚 **Researchers**: Summarize research papers
- 💼 **Professionals**: Create training materials
- 🎓 **Self-learners**: Generate practice questions from any content

## 🔐 Security

- Never commit API keys to version control
- Use environment variables or secrets management
- Keep `secrets.toml` in `.gitignore`
- Rotate API keys regularly
- Use read-only API keys when possible

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** - For the powerful generative AI model
- **Streamlit** - For the amazing web framework
- **PyPDF2** - For PDF processing capabilities

## 📧 Contact

**Vishal** - Project Developer

- GitHub: [@vishalpr013](https://github.com/vishalpr013)
- Project Link: [https://github.com/vishalpr013/SmartStudy-AI](https://github.com/vishalpr013/SmartStudy-AI)

---

<div align="center">

**⭐ If you find this project helpful, please give it a star! ⭐**

Made with ❤️ using Streamlit and Google Gemini AI

</div>
