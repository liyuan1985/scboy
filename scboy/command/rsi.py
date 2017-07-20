import pandas as pd
import argparse

from scboy.command.test_series import TestSeries


class Rsi:
    name = 'Rsi'

    def __init__(self, df, argsStr):
        self.parser = argparse.ArgumentParser(description='generating relative strength index for time series')
        self.parser.add_argument('period', type=int, nargs='?', default=60,
                                 help='period of Rsi')
        self.parser.add_argument('-src', type=str, nargs='?', default='close',
                                 help='column of data source in the Dataframe object')

        args = argsStr.split(' ')
        if len(argsStr) > 0:
            args = self.parser.parse_args(args)
        else:
            args = self.parser.parse_args(['14']) # default values

        self.df = df
        self.period = args.period
        self.src_col_name = args.src
        self.col_name = 'rsi_{}'.format(self.period)

    def help(self):
        self.parser.print_help()

    def RSI(self, prices, n=14):
        # https://stackoverflow.com/questions/20526414/relative-strength-index-in-python-pandas
        # third answer
        deltas = (prices['close'] - prices['close'].shift(1)).fillna(0)

        # Calculate the straight average seed values.
        # The first delta is always zero, so we will use a slice of the first n deltas starting at 1,
        # and filter only deltas > 0 to get gains and deltas < 0 to get losses
        avg_of_gains = deltas[1:n + 1][deltas > 0].sum() / n
        avg_of_losses = -deltas[1:n + 1][deltas < 0].sum() / n

        # Set up pd.Series container for RSI values
        rsi_series = pd.Series(0.0, deltas.index)

        # Now calculate RSI using the Wilder smoothing method, starting with n+1 delta.
        up = lambda x: x if x > 0 else 0
        down = lambda x: -x if x < 0 else 0
        i = n + 1
        for d in deltas[n + 1:]:
            avg_of_gains = ((avg_of_gains * (n - 1)) + up(d)) / n
            avg_of_losses = ((avg_of_losses * (n - 1)) + down(d)) / n
            if avg_of_losses != 0:
                rs = avg_of_gains / avg_of_losses
                rsi_series[i] = 100 - (100 / (1 + rs))
            else:
                rsi_series[i] = 100
            i += 1

        return rsi_series

    def execute(self) -> pd.DataFrame:
        self.df[self.col_name] = self.RSI(self.df, self.period).shift(1)
        return self.df

if __name__ == '__main__':
    df = TestSeries(None, None).execute()
    rsi = Rsi(df, '')

    df = rsi.execute()
    print(df)
