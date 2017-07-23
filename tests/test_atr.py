import os
import unittest

import numpy as np
import pandas as pd

from scboy.command.atr import Atr


class TestCommand(unittest.TestCase):
    def test_atr_1(self):
        file = os.path.join('data', 'atr.xls')
        df = pd.read_excel(file)
        df = Atr(df, '14').execute()

        # expected = df.loc[16:, 'atr2'].values.astype(np.float64)
        expected = df.loc[:, 'atr2'].iloc[14:]
        actual = df.loc[:, 'atr_14'].iloc[14:]
        np.testing.assert_allclose(expected, actual)
        return


if __name__ == '__main__':
    unittest.main()
