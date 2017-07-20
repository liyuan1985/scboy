import unittest
import numpy as np
import pandas as pd

from scboy.command.rsi import Rsi
from scboy.command.test_series import TestSeries
from scboy.starter import zealot


class TestCommand(unittest.TestCase):
    def test_rsi_1(self):
        df = pd.read_excel('rsi.xls')
        df = Rsi(df, '14').execute()

        exptected = df.loc[16:, '14-day rsi']
        actual = df.loc[16:, 'rsi_14']
        np.testing.assert_array_equal(exptected, actual)
        return

if __name__ == '__main__':
    unittest.main()
