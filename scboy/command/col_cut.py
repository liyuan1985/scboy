import argparse

import pandas as pd

from scboy.command.command import Command

parser = argparse.ArgumentParser(description='cut (remove) data in dataFrom by columns')
parser.add_argument('col_names', type=str, nargs='+',
                    help='columnas to be cut (or remove)')
parser.add_argument('-rm', action="store_true",
                    help='if set, then input remove columns instead of retain')

'''
suppose input DF has column A B C

cut A,C will return DF with only columns A,C
cut -rm A,C will reutrn DF with only 1 only B
'''


class ColumnCut(Command):
    name = 'ColumnCut'

    def __init__(self, df, argsStr):

        args = argsStr.split(' ')
        if len(argsStr) > 0:
            args = parser.parse_args(args)
        else:
            raise ValueError("invalid input {}, {}".format(argsStr, ColumnCut.help()))

        self.df = df
        if args.rm:
            cols = df.columns.values.tolist()
            for c in args.col_names:
                cols.remove(c)
            self.col_names = cols
        else:
            self.col_names = args.col_names

    @staticmethod
    def help():
        parser.print_help()

    def execute(self) -> pd.DataFrame:
        return self.df.filter(items=self.col_names)
