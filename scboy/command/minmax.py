import argparse

import pandas as pd

from scboy.command.command import Command

parser = argparse.ArgumentParser(description='generating Min/Max for time series for given period')
parser.add_argument('period', type=int, nargs='?', default=60,
                    help='period of Min/Max')
parser.add_argument('-min', type=str, nargs='?', default='low',
                    help='src of min column in the Dataframe object')
parser.add_argument('-max', type=str, nargs='?', default='high',
                    help='src of max column in the Dataframe object')


class MinMax(Command):
    name = 'MinMax'

    def __init__(self, df, argsStr):

        args = argsStr.split(' ')
        if len(argsStr) > 0:
            args = parser.parse_args(args)
        else:
            args = parser.parse_args(['20'])  # default values

        self.df = df
        self.period = args.period
        self.min_src = args.min
        self.max_src = args.max
        self.min_name = 'min_{}'.format(self.period)
        self.max_name = 'max_{}'.format(self.period)

    @staticmethod
    def help():
        parser.print_help()

    def execute(self) -> pd.DataFrame:
        self.df[self.min_name] = self.df[self.min_src].rolling(self.period).min()
        self.df[self.max_name] = self.df[self.max_src].rolling(self.period).max()
        return self.df
