import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 

    def test_english_to_french(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Hello World"), "Bonjour le monde")
        self.assertNotEqual(english_to_french("Welcome to France"), "Bienvenue en USA")

class TestFrenchToEnglish(unittest.TestCase): 

    def test_french_to_english(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Bonjour le monde"), "Hello World")
        self.assertNotEqual(french_to_english("Bienvenue en France"), "Welcome to USA")
        
unittest.main()