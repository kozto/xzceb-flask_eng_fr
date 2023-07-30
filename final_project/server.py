"""Module providing json function."""
import json
"""Module providing translate function."""
import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """Translate English text to French text."""
    text_to_translate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(text_to_translate)
    return translated_text

@app.route("/frenchToEnglish")
def french_to_english():
    """Translate French text to English text."""
    text_to_translate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(text_to_translate)
    return translated_text

@app.route("/")
def render_index_page():
    """Render index.html."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
