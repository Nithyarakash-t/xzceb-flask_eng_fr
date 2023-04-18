import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(null), null) # test when null is given as input the output is null.
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is "Bonjour".
        
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
       self.assertEqual(frenchToEnglish(null), null) # test when null is given as input the output is null.
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is "Hello".
        
unittest.main()