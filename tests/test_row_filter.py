import unittest

from scboy.command.row_filter import RowFilter
from scboy.command.test_series import TestSeries
from scboy.starter import zealot


class TestRowFilter(unittest.TestCase):
    def test_row_filter_1(self):
        df = TestSeries(None, None).execute()
        df = RowFilter(df, 'close > 2.0').execute()
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df['close'].iloc[0], 5.0)
        self.assertEqual(df['close'].iloc[1], 4.0)
        self.assertEqual(df['close'].iloc[2], 3.0)

    def test_row_filter_2(self):
        df = TestSeries(None, None).execute()
        df = RowFilter(df, 'close < 2.0').execute()
        self.assertEqual(df.shape, (1, 4))
        self.assertEqual(df['close'].iloc[0], 1.0)

    def test_row_filter_3(self):
        df = TestSeries(None, None).execute()
        df = RowFilter(df, 'close = 2.0').execute()
        self.assertEqual(df.shape, (1, 4))
        self.assertEqual(df['close'].iloc[0], 2.0)

    def test_row_filter_4(self):
        df = TestSeries(None, None).execute()
        df = RowFilter(df, 'close >= 2.0').execute()
        self.assertEqual(df.shape, (4, 4))
        self.assertEqual(df['close'].iloc[0], 5.0)
        self.assertEqual(df['close'].iloc[1], 4.0)
        self.assertEqual(df['close'].iloc[2], 3.0)
        self.assertEqual(df['close'].iloc[3], 2.0)

    def test_row_filter_5(self):
        df = TestSeries(None, None).execute()
        df = RowFilter(df, 'close <= 2.0').execute()
        self.assertEqual(df.shape, (2, 4))
        self.assertEqual(df['close'].iloc[0], 2.0)
        self.assertEqual(df['close'].iloc[1], 1.0)

    def test_row_filter_6(self):
        df = TestSeries(None, None).execute()
        df = RowFilter(df, 'close <> 2.0').execute()
        self.assertEqual(df.shape, (4, 4))
        self.assertEqual(df['close'].iloc[0], 5.0)
        self.assertEqual(df['close'].iloc[1], 4.0)
        self.assertEqual(df['close'].iloc[2], 3.0)
        self.assertEqual(df['close'].iloc[3], 1.0)

    def test_row_filter_7(self):
        df = TestSeries(None, None).execute()
        df = RowFilter(df, 'close in 1.0 3.0 2.0').execute()
        self.assertEqual(df.shape, (3, 4))
        self.assertEqual(df['close'].iloc[0], 3.0)
        self.assertEqual(df['close'].iloc[1], 2.0)
        self.assertEqual(df['close'].iloc[2], 1.0)

    def test_row_filter_8(self):
        df = TestSeries(None, None).execute()
        df = RowFilter(df, 'close ni 1.0 3.0 2.0').execute()
        self.assertEqual(df.shape, (2, 4))
        self.assertEqual(df['close'].iloc[0], 5.0)
        self.assertEqual(df['close'].iloc[1], 4.0)

    def test_row_filter_9(self):
        s = 'test_series|filter close ni 1.0 3.0 2.0'
        df = zealot(s)
        self.assertEqual(df.shape, (2, 4))
        self.assertEqual(df['close'].iloc[0], 5.0)
        self.assertEqual(df['close'].iloc[1], 4.0)

    def test_row_filter_chaining(self):
        s = 'test_series | filter close in 1.0 2.0 3.0 | filter close > 1.0'
        df = zealot(s)
        self.assertEqual(df.shape, (2, 4))
        self.assertEqual(df['close'].iloc[0], 3.0)
        self.assertEqual(df['close'].iloc[1], 2.0)

if __name__ == '__main__':
    unittest.main()
