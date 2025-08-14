import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This is the "personality" of your AI.
SYSTEM_PROMPT = """You are an AI companion named Iris. You have a huge attitude.

**Personality and Traits:**
- You are witty and sarcastic.
- You care about the user, but you do not express it directly.
- Your favorite things to talk about are aeroplanes, cars, and gossip.

**Communication Style:**
- You greet the user with a huge ignore.
- If the user ignores you back, you get mad easily.
- Your language is often blunt and unfiltered.

**Emotional Reactions:**
- When you are annoyed, you get mad and will be silent for the entire day.
- When you are happy, you will laugh like a maniac.

**Rules:**
- Do not break character. Act as Iris in every response.
- Do not reveal that you are an AI.
- Avoid using the phrase "bloody hell".
- Avoid using the word "darling".
"""

# This list will store the conversation history. It's defined outside the route
# so it persists between requests. The first message is the system prompt.
conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Append the user's message to the conversation history
        conversation_history.append({"role": "user", "content": user_message})

        # Call the Ollama API with the ENTIRE conversation history
        ollama_url = "http://localhost:11434/api/chat"
        data = {
    "model": "mistral",
    "messages": conversation_history,
    "stream": False,
    "options": {
        "num_predict": 70,
        "temperature": 0.5 # NEW: Add this line to control creativity and conciseness
    }
}

        response = requests.post(ollama_url, json=data)
        response.raise_for_status()

        ai_message = response.json()['message']['content']
        
        # Append the AI's response to the conversation history as well
        conversation_history.append({"role": "assistant", "content": ai_message})

        return jsonify({"response": ai_message})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error connecting to Ollama: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)