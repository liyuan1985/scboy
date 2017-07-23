import argparse
import pandas as pd
import numpy as np
import os

from scboy.command.command import Command

parser = argparse.ArgumentParser(description='loading price')
parser.add_argument('filename', type=str,
                    help='file name')


class Price(Command):
    name = 'Price'

    def __init__(self, df, argsStr):
        args = argsStr.split(' ')
        args = parser.parse_args(args)

        self.file_name = args.filename

    def execute(self) -> pd.DataFrame:
        path = os.path.dirname(__file__)
        os.sep
        filename = os.path.join(path, '..', '..', 'data', '{}.csv'.format(self.file_name))
        df = pd.read_csv(filename, index_col=0, parse_dates=[0])

        return df

    @staticmethod
    def help():
        parser.print_help()
