import unittest

from translator import french_to_english,english_to_french


class TestF2E(unittest.TestCase):
    def testWord(self):
       self.assertTrue(french_to_english('Bonjour'), 'Hello')
       self.assertTrue(english_to_french('Hello'), 'Bonjour')
       

if __name__ == '__main__':
    unittest.main()

class TestNull(unittest.TestCase):
    def test2(self):
        testValue = None
        Message = "Error"

        self.assertTrue(french_to_english(testValue), Message)
        self.assertTrue(english_to_french(testValue), Message)
       

if __name__ == '__main__':
    unittest.main()
