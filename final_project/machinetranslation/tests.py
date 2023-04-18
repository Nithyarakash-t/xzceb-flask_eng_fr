import unittest

from translator import englishToFrench, frenchToEnglish

# English to French Test
class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(None), None) # test when null is given as input the output is null.
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is "Bonjour".
        self.assertEqual(englishToFrench('World'), 'Monde') # test when 'World' is given as input the output is "Monde".

#French to English Test     
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(None), None) # test when null is given as input the output is null.
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is "Hello".
        self.assertEqual(frenchToEnglish('Monde'), 'World') # test when 'Monde' is given as input the output is "World".

unittest.main()