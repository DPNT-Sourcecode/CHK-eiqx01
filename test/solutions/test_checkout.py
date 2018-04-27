import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout('AAa-'), 130)


if __name__ == '__main__':
    unittest.main()
