import unittest
import numpy as np
import pandas as pd

from scboy.command.rsi import Rsi
from scboy.command.test_series import TestSeries
from scboy.starter import zealot


class TestCommand(unittest.TestCase):
    def test_rsi_1(self):
        df = pd.read_csv('rsi.csv')
        df = Rsi(df, '14').execute()
        self.assertEqual(df['rsi_2'][1], 4.5)
        self.assertEqual(df['rsi_2'][2], 3.5)
        self.assertEqual(df['rsi_2'][3], 2.5)
        self.assertEqual(df['rsi_2'][4], 1.5)


if __name__ == '__main__':
    unittest.main()
