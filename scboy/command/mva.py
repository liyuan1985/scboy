import pandas as pd
import argparse

from scboy.command.test_series import TestSeries


class Mva:
    name = 'Mva'

    def __init__(self, df, argsStr):
        self.parser = argparse.ArgumentParser(description='generating moving average for time series')
        self.parser.add_argument('period', type=int, nargs='?', default=60,
                                 help='period of MVA')
        self.parser.add_argument('-src', type=str, nargs='?', default='close',
                                 help='column of data source in the Dataframe object')

        args = argsStr.split(' ')
        if len(argsStr) > 0:
            args = self.parser.parse_args(args)
        else:
            args = self.parser.parse_args(['60']) # default values

        self.df = df
        self.period = args.period
        self.src_col_name = args.src
        self.col_name = 'mva_{}'.format(self.period)

    def help(self):
        self.parser.print_help()

    def execute(self) -> pd.DataFrame:
        self.df[self.col_name] = self.df[self.src_col_name].rolling(self.period).mean()
        return self.df


if __name__ == '__main__':
    df = TestSeries(None, None).execute()
    mva = Mva(df, '')

    df = mva.execute()
    print(df)