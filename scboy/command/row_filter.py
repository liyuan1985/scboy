import argparse

import pandas as pd
from numba import float64

from scboy.command.command import Command

parser = argparse.ArgumentParser(description='filter out rows based on conditions on certain column. Examples : '
                                             '"filter A > 1.0"  : returns rows with column A greater than 1.0; '
                                             '"filter A < 1.0"  : returns rows with column A smaller than 1.0; '
                                             '"filter A <> 1.0" : returns rows with column A not equals to 1.0; '
                                             '"filter A = 1.0"  : returns rows with column A equals to 1.0; '
                                             '"filter A in 1 2 3" : returns rows with column A has value in 1 or 2 or 3')

parser.add_argument('col', type=str, nargs='?',
                    help='column name')
parser.add_argument('op', type=str, nargs='?',
                    help='operation : <, >, <>, >=, <=, =, in')
parser.add_argument('crit', type=str, nargs='+',
                    help='criteria, can take multiples if using IN operator')

'''
filter A > 1.0  : return rows with column A greater than 1.0
filter A <= 1.0  : return rows with column A smaller or equal than 1.0
filter A <> 1.0 : return rows with column A not equals to 1.0
filter A = 1.0  : return rows with column A equals to 1.0
filter A in 1 2 3 : return rows with column A has value in 1 or 2 or 3
filter A ni 1 2 3 : return rows with column A has value not in 1 or 2 or 3
'''


class RowFilter(Command):
    name = 'RowFilter'

    def __init__(self, df, argsStr):

        args = argsStr.split(' ')
        if len(args) > 2:
            args = parser.parse_args(args)
        else:
            raise ValueError("invalid input {}, {}".format(argsStr, RowFilter.help()))

        self.df = df
        self.src_col_name = args.col
        self.op = args.op
        self.crit = args.crit

    @staticmethod
    def help():
        parser.print_help()

    def execute(self) -> pd.DataFrame:

        if self.op == '>':
            self.df = self.df.loc[self.df[self.src_col_name] > float64(self.crit[0])]
        elif self.op == '<':
            self.df = self.df.loc[self.df[self.src_col_name] < float64(self.crit[0])]
        elif self.op == '>=':
            self.df = self.df.loc[self.df[self.src_col_name] >= float64(self.crit[0])]
        elif self.op == '<=':
            self.df = self.df.loc[self.df[self.src_col_name] <= float64(self.crit[0])]
        elif self.op == '=':
            self.df = self.df.loc[self.df[self.src_col_name] == float64(self.crit[0])]
        elif self.op == '<>':
            self.df = self.df.loc[self.df[self.src_col_name] != float64(self.crit[0])]
        elif self.op == 'in':
            self.df = self.df.loc[self.df[self.src_col_name].isin(self.crit)]
        elif self.op == 'ni':
            self.df = self.df.loc[~self.df[self.src_col_name].isin(self.crit)]

        return self.df
