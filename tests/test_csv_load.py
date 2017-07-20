import unittest

from scboy.command.price import Price
from scboy.starter import zealot


class TestCsvLoad(unittest.TestCase):
    def test_price1(self):
        df = Price(None, 'test').execute()
        self.assertEqual(df.shape, (16, 4))
        self.assertEqual(df.columns[0], 'open')
        self.assertEqual(df.columns[1], 'high')
        self.assertEqual(df.columns[2], 'low')
        self.assertEqual(df.columns[3], 'close')

    def test_price_in_pipe(self):
        df = zealot('price test|mva 5')
        self.assertEqual(df.shape, (16, 5))
        self.assertEqual(df['mva_5'][4], sum(df['close'][0:5]) / 5)


if __name__ == '__main__':
    unittest.main()
