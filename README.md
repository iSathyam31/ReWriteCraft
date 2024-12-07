---
title: Text Rewrite with LangChain
emoji: 😎
colorFrom: green
colorTo: blue
sdk: streamlit
app_file: app.py
pinned: false
---

# ReWriteCraft: Text Rewrite with Custom Tone and Dialect 🎨
## Introduction
Welcome to **ReWriteCraft**! 🎉 This project allows you to rewrite your text in a customized tone and dialect using the **LLama 3.1** model. The app provides an intuitive interface to input your draft text and apply different tones (Formal/Informal) and dialects (American/British).

This app leverages LangChain and Ollama models to enhance the AI's rewriting capabilities. Whether you want to refine the tone of a formal letter or add a casual touch to your writing, this app has you covered! 📝


## Project Structure
The project is organized as follows:
```
ReWriteCraft/
│
├── app.py                # Main Streamlit application file
├── requirements.txt      # Python dependencies for the project
├── LICENSE               # License file (GNU)
├── README.md             # Project documentation
│
├── assets/               # Folder containing output examples for tone and dialect conversion
│   ├── FormaltoInformal/ # Folder with examples of text converted from formal to informal tone
│   └── InformaltoFormal/ # Folder with examples of text converted from informal to formal tone
```


## Features
* **Customizable Tone**: Choose between Formal or Informal tones for your rewritten text.
* **Customizable Dialect**: Choose between American or British dialects.
* **Easy-to-use Interface**: The app is built using Streamlit, making it interactive and simple.
* **Quick Response**: Rewritten text is generated with the help of the LLama 3.1 model.


## Prerequisites
Before running the project, ensure the following requirements are met:
1. **Install Ollama**: Ollama is the platform required to run the LLama 3.1 model. Follow the instructions on the Ollama official website to download and install it on your device.
2. **Download LLama 3.1 Model**: After installing Ollama, download the LLama 3.1 model by running the following command in your terminal:
```
ollama pull llama3.1
```
3. **Python Environment**: Ensure you have Python installed on your machine. It's recommended to use Python 3.9 or later for compatibility with the dependencies listed in `requirements.txt`.


## How to Use
1. **Clone the Repository**: Clone this repository to your local machine or server:
```
git clone https://github.com/iSathyam31/ReWriteCraft.git
cd ReWriteCraft
```
2. **Create a `.env` file**: In the root directory, create a `.env` file to store your LangChain API key:
```
LANGCHAIN_API_KEY=your_api_key_here
```
3. **Install Dependencies**: Install the required Python packages listed in the `requirements.txt`:
```
pip install -r requirements.txt
```
4. **Run the App**: Once the dependencies are installed, you can run the Streamlit app using:
```
streamlit run app.py
```
The app will be accessible in your browser at `http://localhost:8501`.


## Project Constraints
* **Word Limit**: The app currently supports a maximum of 1500 words for input. You can modify this limit in the code if needed. The input text must be within this word count to avoid performance issues.
* **Tone & Dialect Selection**:
  - The options for tone (Formal/Informal) and dialect (American/British) are optional. You can choose one or both options based on your needs.
  - If you want a specific tone or dialect applied to your text, simply check the corresponding boxes. You can apply both tone and dialect together or choose either one independently.
  - This flexibility allows you to get a variety of outputs depending on your selection.  


## Requirements
You can find the necessary dependencies in the `requirements.txt` file. Here is the list:
```
ipykernel
langchain==0.2.10
langchain_community==0.2.10
langchain-openai==0.1.17
langchain-groq==0.1.6
langchain-ollama==0.1.0
python-dotenv==1.0.1
streamlit
```


## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more information.


## Acknowledgements
* **LangChain**: Used for integrating LLMs and text processing functionalities.
* **Ollama**: The primary language model used in this project (LLama 3.1) for text generation.
* **Streamlit**: The framework used to build this interactive web app.

Thanks to all the developers and contributors of these tools for making them available to the open-source community! 🙌

