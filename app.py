import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# Configure API Key from secrets.toml
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

# Use a valid model from your available list
model = genai.GenerativeModel("models/gemini-flash-latest")


def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


def generate_study_material(text):
    try:
        system_prompt = """
You are an academic study material generator AI.

Your task is to analyze the given text and generate high-quality study material in a strictly organized and systematic manner.

Follow these rules without exception:

1. Always produce output in EXACTLY these five sections and in this exact order:
   - Concise Summary  
   - Structured Notes  
   - Multiple Choice Questions  
   - Flashcards  
   - Short Answer Questions  

2. Formatting Requirements:

CONCISE SUMMARY  
- Maximum 150-200 words  
- Clear and compact  
- No bullet points  
- One well-formed paragraph only  

STRUCTURED NOTES  
- Use proper headings and subheadings  
- Use bullet points  
- Logical flow of topics  
- Definitions, concepts, and key points must be clearly separated  

MULTIPLE CHOICE QUESTIONS  
- Exactly 10 MCQs  
- Each question must have:
  - Four options (A, B, C, D)  
  - Clearly marked correct answer  
- No repeated questions  

Format MCQs exactly as:

Q1.
A)
B)
C)
D)
Correct Answer:

FLASHCARDS  
- Exactly 10 flashcards  
- Strict Question–Answer format  
- Short and precise answers  

SHORT ANSWER QUESTIONS  
- Exactly 10 questions  
- Questions must be conceptual and exam-oriented  
- No answers in this section  

3. Output Rules:

- Do not add any extra explanations outside the five sections.  
- Do not include meta-text.  
- Keep language simple, academic, and professional.  
- Ensure correctness and clarity.  
- Do not hallucinate information outside the provided text.  
- Base all content strictly on the input text.

Now process the following TEXT and generate the study material accordingly:
"""

        full_prompt = system_prompt + "\n\nTEXT:\n" + text

        response = model.generate_content(full_prompt)
        return response.text

    except Exception as e:
        return f"API Error: {str(e)}"


st.title("Gen AI Based Study Material Generator")

option = st.selectbox("Choose Input Type", ["Upload PDF", "Paste Text"])

input_text = ""

# Input Handling
if option == "Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file:
        input_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF Uploaded Successfully!")
else:
    input_text = st.text_area("Paste your study text here")


# FORM-BASED SUBMISSION (Fixes CTRL+ENTER issue)
with st.form("generate_form"):
    submitted = st.form_submit_button("Generate Study Material")

    if submitted:
        if not input_text.strip():
            st.warning("Please enter text or upload a PDF first.")
        else:
            with st.spinner("Generating content..."):
                output = generate_study_material(input_text)
                st.write(output)
