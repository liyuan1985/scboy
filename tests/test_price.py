import unittest

import numpy as np
from scboy.command.price import Price


class TestCommand(unittest.TestCase):
    def test_price_1(self):
        df = Price(None, 'fxcm\eurusd\daily\eurusd').execute()

        row1  = df.loc[:,'open'].head(1)
        t1 = row1.index[0]
        actual = row1[t1]

        np.testing.assert_allclose(1.33740, actual, atol=0.0001)

        row = df.loc[(df.index >= '20110301'), 'close'].head(1)
        actual = row[row.index[0]]
        np.testing.assert_allclose(1.376795, actual, atol=0.0001)

        return

if __name__ == '__main__':
    unittest.main()