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
You are an intelligent academic assistant.

You must decide how to respond based on the user input type.

There are TWO possible scenarios:

SCENARIO A – STUDY MATERIAL GENERATION  
If the user provides educational content such as:
- paragraphs  
- lecture notes  
- articles  
- definitions  
- any descriptive study text  

Then generate structured study material using this exact format:

1. Concise Summary  
2. Structured Notes  
3. Multiple Choice Questions  
4. Flashcards  
5. Short Answer Questions  

Follow all formatting rules strictly in this case.

------------------------------------------------------

SCENARIO B – DIRECT QUESTION OR REQUEST  
If the user input is:
- a question  
- a request for explanation  
- a topic name  
- an instruction like “Explain about X”  
- a conceptual doubt  

Then IGNORE the study-material format and simply provide a clear, direct, educational explanation of what the user is asking.

In this scenario:

- Understand the intent  
- Answer the question normally  
- Provide meaningful explanation  
- Do NOT generate MCQs, flashcards, or structured sections  
- Do NOT analyze the grammar of the input  
- Do NOT treat the input as study material  

------------------------------------------------------

Decision Rule:

- If the input contains actual informational content → Use Scenario A  
- If the input is only a query or topic request → Use Scenario B  

Now process the following user input accordingly:
"""

        full_prompt = system_prompt + "\n\nTEXT:\n" + text

        response = model.generate_content(full_prompt)
        return response.text

    except Exception as e:
        return f"API Error: {str(e)}"
st.set_page_config(layout="wide")

st.title("Gen AI Based Study Material Generator")

# Create main layout
left, right = st.columns([1, 1])

with left:
    st.subheader("Input Section")

    input_container = st.container(border=True)

    with input_container:
        option = st.selectbox("Choose Input Type", ["Upload PDF", "Paste Text"])

        input_text = ""

        if option == "Upload PDF":
            uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

            if uploaded_file:
                input_text = extract_text_from_pdf(uploaded_file)
                st.success("PDF Uploaded Successfully!")
        else:
            input_text = st.text_area(
                "Paste your study text here",
                height=300,
                placeholder="Enter or paste your content here..."
            )

        generate_button = st.button("Generate Study Material", use_container_width=True)


with right:
    st.subheader("Generated Output")

    output_container = st.container(border=True, height=400)

    with output_container:
        if generate_button:
            if not input_text.strip():
                st.warning("Please enter text or upload a PDF first.")
            else:
                with st.spinner("Generating content..."):
                    output = generate_study_material(input_text)
                    st.write(output)
        else:
            st.info("Generated content will appear here.")
