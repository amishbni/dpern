import dpern
import unittest

class TestdPern(unittest.TestCase):

    def test_abc(self):
        self.assertRaises(Exception, dpern.describe, 'abc')

    def test_2(self):
        self.assertRaises(Exception, dpern.describe, -2)

    def test2(self):
        self.assertEqual('دو', dpern.describe(2))

    def test12(self):
        self.assertEqual('دوازده', dpern.describe(12))

    def test30(self):
        self.assertEqual('سی', dpern.describe(30))

    def test209(self):
        self.assertEqual('دویست و نه', dpern.describe(209))

    def test333(self):
        self.assertEqual('سیصد و سی و سه', dpern.describe(333))

    def test1001(self):
        self.assertEqual('یک هزار و یک', dpern.describe(1001))

    def test1089(self):
        self.assertEqual('یک هزار و هشتاد و نه', dpern.describe(1089))

    def test9999(self):
        self.assertEqual('نه هزار و نهصد و نود و نه', dpern.describe(9999))

    def test77777(self):
        self.assertEqual(
            'هفتاد و هفت هزار و هفتصد و هفتاد و هفت',
            dpern.describe(77777))

    def test654321(self):
        self.assertEqual(
            'ششصد و پنجاه و چهار هزار و سیصد و بیست و یک',
            dpern.describe(654321))

    def test9000808(self):
        self.assertEqual(
            'نه میلیون و هشتصد و هشت',
            dpern.describe(9000808))

    def test987654321(self):
        self.assertEqual(
            'نهصد و هشتاد و هفت میلیون'
                +' و ششصد و پنجاه و چهار هزار'
                +' و سیصد و بیست و یک',
            dpern.describe(987654321))

    def test1010101010(self):
        self.assertEqual(
            'یک میلیارد و ده میلیون و صد و یک هزار و ده',
            dpern.describe(1010101010))

    def test100000000111(self):
        self.assertEqual(
            'صد میلیارد و صد و یازده',
            dpern.describe(100000000111))

if __name__ == '__main__':
    unittest.main()
