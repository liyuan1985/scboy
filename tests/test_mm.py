import unittest

from scboy.command.minmax import MinMax
from scboy.command.test_series import TestSeries
from scboy.starter import zealot


class TestMinMax(unittest.TestCase):
    def test_mm_1(self):
        df = TestSeries(None, None).execute()
        df = MinMax(df, '2').execute()
        self.assertEqual(df['min_2'][1], 3.0)
        self.assertEqual(df['min_2'][2], 1.0)
        self.assertEqual(df['min_2'][3], 1.0)
        self.assertEqual(df['min_2'][4], 1.0)
        self.assertEqual(df['max_2'][1], 6.0)
        self.assertEqual(df['max_2'][2], 4.0)
        self.assertEqual(df['max_2'][3], 3.0)
        self.assertEqual(df['max_2'][4], 3.0)

    def test_mm_2(self):
        s = 'test_series|mm 2'
        df = zealot(s)
        self.assertEqual(df['min_2'][1], 3.0)
        self.assertEqual(df['min_2'][2], 1.0)
        self.assertEqual(df['min_2'][3], 1.0)
        self.assertEqual(df['min_2'][4], 1.0)
        self.assertEqual(df['max_2'][1], 6.0)
        self.assertEqual(df['max_2'][2], 4.0)
        self.assertEqual(df['max_2'][3], 3.0)
        self.assertEqual(df['max_2'][4], 3.0)

if __name__ == '__main__':
    unittest.main()