import argparse

import pandas as pd

from scboy.command.command import Command

parser = argparse.ArgumentParser(description='generating moving average for time series')
parser.add_argument('period', type=int, nargs='?', default=60,
                    help='period of MVA')
parser.add_argument('-src', type=str, nargs='?', default='close',
                    help='column of data source in the Dataframe object')


class Mva(Command):
    name = 'Mva'

    def __init__(self, df, argsStr):

        args = argsStr.split(' ')
        if len(argsStr) > 0:
            args = parser.parse_args(args)
        else:
            args = parser.parse_args(['60'])  # default values

        self.df = df
        self.period = args.period
        self.src_col_name = args.src
        self.col_name = 'mva_{}'.format(self.period)

    @staticmethod
    def help():
        parser.print_help()

    def execute(self) -> pd.DataFrame:
        self.df[self.col_name] = self.df[self.src_col_name].rolling(self.period).mean()
        return self.df
