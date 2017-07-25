import unittest

from scboy.command.col_cut import ColumnCut
from scboy.command.test_series import TestSeries
from scboy.starter import zealot


class TestColumnCut(unittest.TestCase):
    def test_cut_1(self):
        df = TestSeries(None, None).execute()
        df = ColumnCut(df, 'open close').execute()
        self.assertEqual(len(df.columns.values), 2)
        self.assertEqual(df.columns.values[0], 'open')
        self.assertEqual(df.columns.values[1], 'close')

    def test_cut_2(self):
        s = 'test_series|cut -rm open close'
        df = zealot(s)
        self.assertEqual(len(df.columns.values), 2)
        self.assertEqual(df.columns.values[0], 'high')
        self.assertEqual(df.columns.values[1], 'low')


if __name__ == '__main__':
    unittest.main()
