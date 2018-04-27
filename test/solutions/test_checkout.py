import unittest

from lib.solutions.checkout import checkout

class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout('AAAA'), 180)
        self.assertEqual(checkout('C'), 20)
        self.assertEqual(checkout('BEE'), 80)
        self.assertEqual(checkout('FF'), 20)
        self.assertEqual(checkout('FFF'), 20)
        self.assertEqual(checkout('FFFF'), 30)
        self.assertEqual(checkout('FFFFF'), 40)
        self.assertEqual(checkout('FFFFFF'), 40)
        self.assertEqual(checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 40)


if __name__ == '__main__':
    unittest.main()
