import unittest

from int_roman import IntRoman


class IntRomanCase(unittest.TestCase):
    def setUp(self):
        self.ir = IntRoman()

    def test_one_to_three(self):
        self.assertEqual(self.ir.one_to_three(3, 3), 'CCC')
        self.assertEqual(self.ir.one_to_three(2, 2), 'XX')
        self.assertEqual(self.ir.one_to_three(1, 1), 'I')
        self.assertEqual(self.ir.one_to_three(3, 1), 'III')
        self.assertEqual(self.ir.one_to_three(2, 3), 'CC')
        self.assertEqual(self.ir.one_to_three(2, 4), 'MM')

    def test_mid_six(self):
        self.assertEqual(self.ir.mid_six(4, 2), 'XL')
        self.assertEqual(self.ir.mid_six(4, 3), 'CD')
        self.assertEqual(self.ir.mid_six(5, 1), 'V')
        self.assertEqual(self.ir.mid_six(5, 2), 'L')
        self.assertEqual(self.ir.mid_six(5, 3), 'D')
        self.assertEqual(self.ir.mid_six(7, 1), 'VII')
        self.assertEqual(self.ir.mid_six(8, 2), 'LXXX')
        self.assertEqual(self.ir.mid_six(6, 3), 'DC')

    def test_nine(self):
        self.assertEqual(self.ir.nine(1), 'IX')
        self.assertEqual(self.ir.nine(2), 'XC')
        self.assertEqual(self.ir.nine(3), 'CM')

    def test_resolute(self):
        self.assertEqual(self.ir.resolute(0), '')
        self.assertEqual(self.ir.resolute(89), 'LXXXIX')
        self.assertEqual(self.ir.resolute(50), 'L')
        self.assertEqual(self.ir.resolute(10), 'X')
        self.assertEqual(self.ir.resolute(24), 'XXIV')
        self.assertEqual(self.ir.resolute(17), 'XVII')
        self.assertEqual(self.ir.resolute(666), 'DCLXVI')
        self.assertEqual(self.ir.resolute(1999), 'MCMXCIX')
        self.assertEqual(self.ir.resolute(19), 'XIX')

    def test_to_roman(self):
        self.assertRaises(TypeError, self.ir.to_roman, '453')
        self.assertRaises(TypeError, self.ir.to_roman, 344.46)
        self.assertRaises(TypeError, self.ir.to_roman, False)
        self.assertRaises(ValueError, self.ir.to_roman, 4000)

    def test_list_roman(self):
        nums = [1, 22, 333, 1553, 2224]
        roms = ['I', 'XXII', 'CCCXXXIII', 'MDLIII', 'MMCCXXIV']
        self.assertListEqual(self.ir.to_roman_list(nums), roms)


if __name__ == '__main__':
    unittest.main()
