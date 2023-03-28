from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
import openai

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = "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"

# Set up your custom knowledge base
knowledge_base = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest country in the world?", "answer": "Russia"},
    {"question": "Who invented the telephone?", "answer": "Alexander Graham Bell"},
]

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '')
    response = MessagingResponse()

    # Check if the message is a question
    if "?" in incoming_msg:
        # Use ChatGPT to generate a response
        prompt = f"Q: {incoming_msg} \nA:"
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        answer = response.choices[0].text.strip()
    else:
        # Check if the message is in the knowledge base
        for item in knowledge_base:
            return item
