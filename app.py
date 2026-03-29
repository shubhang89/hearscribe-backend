from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend running ✅"

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get("text")
    target_lang = data.get("target_lang")

    res = requests.post("https://libretranslate.de/translate", data={
        "q": text,
        "source": "auto",
        "target": target_lang,
        "format": "text"
    })

    return jsonify({
        "translated_text": res.json()["translatedText"]
    })

if __name__ == '__main__':
    app.run()