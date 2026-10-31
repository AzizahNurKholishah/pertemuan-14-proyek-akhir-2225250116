
import sys
import os
import unittest

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)

from perhitungan import (
    hitung_persegi,
    hitung_persegi_panjang,
    hitung_segitiga,
    hitung_lingkaran
)


class TestKalkulatorGeometri(unittest.TestCase):

    def test_persegi(self):
        self.assertEqual(hitung_persegi(5), (25, 20))

    def test_persegi_panjang(self):
        self.assertEqual(hitung_persegi_panjang(6, 4), (24, 20))

    def test_segitiga(self):
        self.assertEqual(hitung_segitiga(6, 4, 5, 5, 6), (12, 16))

    def test_lingkaran(self):
        luas, keliling = hitung_lingkaran(7)
        self.assertAlmostEqual(luas, 153.938, places=2)
        self.assertAlmostEqual(keliling, 43.982, places=2)


if __name__ == "__main__":
    unittest.main()
