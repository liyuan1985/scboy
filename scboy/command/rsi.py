import argparse

import pandas as pd

from scboy.command.test_series import TestSeries

parser = argparse.ArgumentParser(description='generating relative strength index for time series')
parser.add_argument('period', type=int, nargs='?', default=60,
                    help='period of Rsi')
parser.add_argument('-src', type=str, nargs='?', default='close',
                    help='column of data source in the Dataframe object')


class Rsi:
    name = 'Rsi'

    def __init__(self, df, argsStr):

        args = argsStr.split(' ')
        if len(argsStr) > 0:
            args = parser.parse_args(args)
        else:
            args = parser.parse_args(['14'])  # default values

        self.df = df
        self.period = args.period
        self.src_col_name = args.src
        self.col_name = 'rsi_{}'.format(self.period)

    @staticmethod
    def help():
        parser.print_help()

    def execute(self) -> pd.DataFrame:
        prices = self.df[self.src_col_name]

        # Get the difference in price from previous step
        delta = prices.diff()

        # Make the positive gains (up) and negative gains (down) Series
        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0

        # Calculate the EWMA
        roll_up = pd.stats.moments.ewma(up, com=self.period)
        roll_down = pd.stats.moments.ewma(down.abs(), com=self.period)

        # Calculate the RSI based on EWMA
        RS = roll_up / roll_down
        RSI = 100.0 - (100.0 / (1.0 + RS))

        self.df[self.col_name] = RSI
        return self.df

if __name__ == '__main__':
    df = TestSeries(None, None).execute()
    rsi = Rsi(df, '2')

    df = rsi.execute()
    print(df)
