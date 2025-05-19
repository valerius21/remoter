import unittest
from app.lib import greet

class TestLib(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == "__main__":
    unittest.main() 