import unittest

import numpy as np
import pandas as pd
import os

from scboy.command.rsi import Rsi


class TestCommand(unittest.TestCase):
    def test_rsi_1(self):
        file = os.path.join('data', 'rsi.xls')
        df = pd.read_excel(file)
        df = Rsi(df, '14').execute()

        exptected = df.loc[16:, '14-day rsi'].values.astype(np.float64)
        actual = df.loc[16:, 'rsi_14']
        np.testing.assert_allclose(exptected, actual)
        return

if __name__ == '__main__':
    unittest.main()
