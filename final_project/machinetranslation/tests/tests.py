import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 

    def test_english_to_french(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Hello World"), "Bonjour le monde")
        self.assertEqual(english_to_french("Welcome to France"), "Bienvenue en France")

class TestFrenchToEnglish(unittest.TestCase): 

    def test_french_to_english(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Bonjour le monde"), "Hello World")
        self.assertEqual(french_to_english("Bienvenue en France"), "Welcome to France")
        
unittest.main()