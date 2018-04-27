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
        self.assertEqual(checkout('HHHHHHHHHH'), 80)
        self.assertEqual(checkout('HHHHHHHHHHH'), 90)
        self.assertEqual(checkout('HHHHHHHHHHHH'), 100)
        self.assertEqual(checkout('ZZZXXXX'), 107)
        self.assertEqual(checkout("KK"), 120)
        self.assertEqual(checkout("KKK"),  190)
        self.assertEqual(checkout("KKKK"),  240)


if __name__ == '__main__':
    unittest.main()
