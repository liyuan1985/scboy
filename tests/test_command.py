import unittest
import numpy as np
import pandas as pd

from scboy.command.mva import Mva
from scboy.command.test_series import TestSeries
from scboy.starter import zealot


class TestCommand(unittest.TestCase):
    def test_mva_1(self):
        df = TestSeries(None, None).execute()
        df = Mva(df, '2').execute()
        self.assertEqual(df['mva_2'][1], 4.5)
        self.assertEqual(df['mva_2'][2], 3.5)
        self.assertEqual(df['mva_2'][3], 2.5)
        self.assertEqual(df['mva_2'][4], 1.5)

    def test_mva_2(self):
        # test default period
        df = TestSeries(None, None).execute()
        df = Mva(df, '').execute()
        self.assertTrue(pd.isnull(df['mva_60'][0]))
        self.assertTrue(pd.isnull(df['mva_60'][1]))
        self.assertTrue(pd.isnull(df['mva_60'][2]))
        self.assertTrue(pd.isnull(df['mva_60'][3]))
        self.assertTrue(pd.isnull(df['mva_60'][4]))

    def test_mva_3(self):
        # test different src col
        df = TestSeries(None, None).execute()
        df = Mva(df, '2 -src open').execute()
        self.assertEqual(df['mva_2'][1], 1.5)
        self.assertEqual(df['mva_2'][2], 2.5)
        self.assertEqual(df['mva_2'][3], 3.5)
        self.assertEqual(df['mva_2'][4], 4.5)

    def test_starter(self):
        s = 'test_series|mva 2|mva 3 -src open'
        df = zealot(s)
        self.assertEqual(df['mva_2'][1], 4.5)
        self.assertEqual(df['mva_2'][2], 3.5)
        self.assertEqual(df['mva_2'][3], 2.5)
        self.assertEqual(df['mva_2'][4], 1.5)

        self.assertEqual(df['mva_3'][2], 2.0)
        self.assertEqual(df['mva_3'][3], 3.0)
        self.assertEqual(df['mva_3'][4], 4.0)


if __name__ == '__main__':
    unittest.main()
