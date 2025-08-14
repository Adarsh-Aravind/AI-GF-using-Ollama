# AI-GF-using-Ollama
An AI companion named Iris, custom-built to run on your computer with Ollama. Her unique personality is set by a system prompt, and she remembers your conversations. You chat with her through a simple web page. It's a private, personal project.


Iris: A Custom AI Companion
This is a personal chatbot project that allows you to create and interact with a customized AI companion named Iris. The project runs entirely on your local machine using an open-source large language model, ensuring privacy and full control.

Features
Local Processing: Runs on your computer using Ollama, no internet connection or API fees required.

Custom Persona: The AI's personality, communication style, and attitude are fully customizable within the code.

Short-Term Memory: Remembers the context of your conversations for a more natural interaction.

Concise Responses: Tuned to provide short, complete, and engaging replies without getting cut off.

Web Interface: A simple HTML and JavaScript interface allows for easy conversation in any web browser.

Prerequisites
Before you begin, make sure you have the following installed:

Python: Version 3.8 or higher.

Ollama: The application that runs the language model.

Mistral Model: Downloaded via Ollama.

Installation
Clone the repository:

Install Python libraries:
pip install flask Flask-Cors requests

Download the language model:
ollama pull mistral

Usage
Start the server:
Open your terminal in the project folder and run the Python application.
python local_app.py

Open the interface:
With the server running, open the index.html file in your web browser to start chatting with Iris.

Customization
You can easily customize the AI's personality and behavior by editing the local_app.py file.

Personality: Modify the SYSTEM_PROMPT variable to change Iris's traits and rules.

Response Length: Adjust the num_predict value in the data dictionary to control the maximum length of her replies.

Conciseness: Adjust the temperature value (e.g., 0.1 for more concise replies, 0.8 for more creative ones).
