import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Langsmith Tracking
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_PROJECT"] = "Enhanced Q&A Chatbot With Ollama"

# Prompt template
template = """
    Below is a draft text that may be poorly worded.
    Your goal is to:
    - Properly redact the draft text
    - Convert the draft text to a specified tone (if selected)
    - Convert the draft text to a specified dialect (if selected)

    Here are some examples of different tones:
    - Formal: Greetings! OpenAI has announced that Sam Altman is rejoining the company as its Chief Executive Officer. After a period of five days of conversations, discussions, and deliberations, the decision to bring back Altman, who had been previously dismissed, has been made. We are delighted to welcome Sam back to OpenAI.
    - Informal: Hey everyone, it's been a wild week! We've got some exciting news to share - Sam Altman is back at OpenAI, taking up the role of chief executive. After a bunch of intense talks, debates, and convincing, Altman is making his triumphant return to the AI startup he co-founded.  

    Here are some examples of words in different dialects:
    - American: French Fries, cotton candy, apartment, garbage, \
        cookie, green thumb, parking lot, pants, windshield
    - British: chips, candyfloss, flag, rubbish, biscuit, green fingers, \
        car park, trousers, windscreen

    Example Sentences from each dialect:
    - American: Greetings! OpenAI has announced that Sam Altman is rejoining the company as its Chief Executive Officer. After a period of five days of conversations, discussions, and deliberations, the decision to bring back Altman, who had been previously dismissed, has been made. We are delighted to welcome Sam back to OpenAI.
    - British: On Wednesday, OpenAI, the esteemed artificial intelligence start-up, announced that Sam Altman would be returning as its Chief Executive Officer. This decisive move follows five days of deliberation, discourse and persuasion, after Altman's abrupt departure from the company which he had co-established.

    Please start the redaction with a warm introduction. Add the introduction \
        if you need to.
    
    Below is the draft text, tone, and dialect:
    DRAFT: {draft}
    TONE: {tone}
    DIALECT: {dialect}

    YOUR RESPONSE:
"""

# PromptTemplate variables definition
prompt = PromptTemplate(
    input_variables=["tone", "dialect", "draft"],
    template=template,
)

def generate_response(input_data, llm):
    """
    Generate the rewritten response based on the input data.
    """
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke(input_data)
    return answer

# Streamlit App Configuration
st.set_page_config(
    page_title="Rewrite Your Text 🎨",
    page_icon="📝",
    layout="centered",
)

# Header Section
st.title("📝 Rewrite Your Text with Style")
st.subheader("✨ Powered by LangChain and Ollama ✨")
st.markdown(
    """
    Welcome to the **Text Rewrite Assistant**! 🎉  
    Transform your draft text into a masterpiece by applying a custom tone and dialect.  
    Simply input your text, select your preferences, and let AI do the rest! 🚀
    """
)

# Input Section
st.markdown("## 📋 Enter Your Text")
def get_draft():
    """
    Get the draft text from the user input.
    """
    draft_text = st.text_area(label="Your Text Here(Max 1500 words)✍️", placeholder="Enter your draft text...", key="draft_input")
    return draft_text

draft_input = get_draft()

if len(draft_input.split(" ")) > 1500:
    st.error("🚫 Your text is too long! Please keep it under 700 words.")
    st.stop()

# Tone and Dialect Options
st.markdown("## 🎭 Customize Your Rewrite")
col1, col2 = st.columns(2)
with col1:
    option_tone = st.checkbox('Apply a Tone? 🎵', value=True)
    selected_tone = st.selectbox(
        'Select a Tone:',
        ('Formal', 'Informal'),
        disabled=not option_tone,
    )

with col2:
    option_dialect = st.checkbox('Apply a Dialect? 🌍', value=True)
    selected_dialect = st.selectbox(
        'Select a Dialect:',
        ('American', 'British'),
        disabled=not option_dialect,
    )

# Generate Button
st.markdown("---")
if st.button("✨ Rewrite My Text ✨"):
    # Initialize the LLM
    llm = Ollama(model="llama3.1")

    # Build input data
    input_data = {
        "draft": draft_input,
        "tone": selected_tone if option_tone else "No tone specified",
        "dialect": selected_dialect if option_dialect else "No dialect specified",
    }

    # Generate the response
    try:
        st.spinner("Generating your rewritten text... 🛠️")
        answer = generate_response(input_data, llm)

        # Display the result
        st.markdown("### 🌟 Your Rewritten Text 🌟")
        st.success(answer)
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
