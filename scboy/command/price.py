import argparse
import pandas as pd
import os

from scboy.command.command import Command


class Price(Command):
    name = 'Price'

    def __init__(self, df, argsStr):
        self.parser = argparse.ArgumentParser(description='loading price')
        self.parser.add_argument('filename', type=str,
                                 help='file name')

        args = argsStr.split(' ')
        args = self.parser.parse_args(args)

        self.file_name = args.filename

    def execute(self) -> pd.DataFrame:
        path = os.path.dirname(__file__)
        filename = os.path.join(path, '../../data/{}.csv'.format(self.file_name))
        df = pd.read_csv(filename, index_col=0)

        return df

    def help(self):
        super().help()

