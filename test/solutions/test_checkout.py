import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout('AAAA'), 180)
        self.assertEqual(checkout('C'), 20)
        self.assertEqual(checkout('BEE'), 80)
        self.assertEqual(checkout('FFF'), 20)


if __name__ == '__main__':
    unittest.main()
