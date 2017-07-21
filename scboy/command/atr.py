import argparse

import pandas as pd
import talib
import numpy as np

from scboy.command.test_series import TestSeries

parser = argparse.ArgumentParser(description='generating average true range for time series')
parser.add_argument('period', type=int, nargs='?', default=60,
                    help='period of Atr')


class Atr:
    name = 'Atr'

    def __init__(self, df, argsStr):

        args = argsStr.split(' ')
        if len(argsStr) > 0:
            args = parser.parse_args(args)
        else:
            args = parser.parse_args(['14'])  # default values

        self.df = df
        self.period = args.period
        self.col_name = 'atr_{}'.format(self.period)

    @staticmethod
    def help():
        parser.print_help()

    def execute(self) -> pd.DataFrame:
        highs = self.df['high'].values
        lows = self.df['low'].values
        closes = self.df['close'].values
        self.df[self.col_name] = talib.ATR(highs, lows, closes, self.period)
        return self.df

if __name__ == '__main__':
    df = TestSeries(None, None).execute()
    rsi = Atr(df, '')

    df = rsi.execute()
    print(df)
