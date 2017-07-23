import argparse

import pandas as pd

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
        highs = self.df['high']
        lows = self.df['low']
        closes = self.df['close']
        closes_prev = closes.copy().shift(1)

        # Calculate TRs
        trs = pd.DataFrame({'hl': highs - lows,
                            'hc': abs(highs - closes_prev),
                            'lc': abs(lows - closes_prev)})
        trs = trs.max(axis=1)

        # get the moving average
        atr = trs.rolling(self.period).mean()
        self.df[self.col_name] = atr

        return self.df


if __name__ == '__main__':
    df = TestSeries(None, None).execute()
    rsi = Atr(df, '2')

    df = rsi.execute()
    print(df)
