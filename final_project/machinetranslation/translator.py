"""Module providing translate function."""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Translate English text to French text."""
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    """Translate French text to English text."""
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    return english_text
