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

    def RSI(cls, ohlc, period=14):
         ## get the price diff
        delta = ohlc["close"].diff()[1:]

        ## positive gains (up) and negative gains (down) Series
        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0

        # EMAs of ups and downs
        _gain = up.ewm(span=period, min_periods=period-1).mean()
        _loss = down.abs().ewm(span=period, min_periods=period-1).mean()

        RS = _gain / _loss
        return pd.Series(100 - (100 / (1 + RS)), name="RSI")

    def myRsi(self, ohlc, period):
        # first average gain = sum of gains in the past x period
        # first average loss = sum of losses over the past x period
        # average gain = (previous average gain * (x - 1) + current gain) / 14
        # average loss = (previous average loss * (x - 1) + current loss) / 14
        delta = ohlc["close"].diff()[1:]
        gains, losses = delta.copy(), delta.copy()
        gains[gains < 0] = 0
        losses[losses > 0] = 0

        avg_gains = gains.rolling(self.period).mean()
        avg_losses = losses.abs().rolling(self.period).mean()
        rs = avg_gains / avg_losses
        return pd.Series(100 - (100 / (1 + rs)))

    def execute(self) -> pd.DataFrame:
        #self.df[self.col_name] = self.df[self.src_col_name].rolling(self.period).mean()
        self.df[self.col_name] = self.myRsi(self.df, self.period)
        return self.df

if __name__ == '__main__':
    df = TestSeries(None, None).execute()
    rsi = Rsi(df, '')

    df = rsi.execute()
    print(df)
