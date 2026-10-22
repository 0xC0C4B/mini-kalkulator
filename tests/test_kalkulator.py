import unittest
from kalkulator import izracunaj


class TestKalkulator(unittest.TestCase):
    def test_sestevanje(self):
        self.assertEqual(izracunaj(2, "+", 3), 5)

    def test_odstevanje(self):
        self.assertEqual(izracunaj(7, "-", 4), 3)

    def test_mnozenje(self):
        self.assertEqual(izracunaj(3, "*", 4), 12)

    def test_deljenje(self):
        self.assertEqual(izracunaj(8, "/", 2), 4)

    def test_deljenje_z_nic(self):
        with self.assertRaisesRegex(ValueError, "Deljenje z ničlo"):
            izracunaj(4, "/", 0)

    def test_neznan_operator(self):
        with self.assertRaises(ValueError):
            izracunaj(1, "^", 2)


if __name__ == "__main__":
    unittest.main()

class TestZaokrozevanje(unittest.TestCase):
    def test_zaokrozevanje(self):
        from kalkulator import zaokrozi
        self.assertEqual(zaokrozi(3.14159, 2), 3.14)
