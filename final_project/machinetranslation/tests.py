import unittest

from translator import english_to_french, french_to_english

# English to French Test
class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(None), None) # test when null is given as input the output is null.
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is "Bonjour".
        self.assertEqual(english_to_french('World'), 'Monde') # test when 'World' is given as input the output is "Monde".

#French to English Test     
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(None), None) # test when null is given as input the output is null.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is "Hello".
        self.assertEqual(french_to_english('Monde'), 'World') # test when 'Monde' is given as input the output is "World".

unittest.main()