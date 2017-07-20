import argparse

import pandas as pd

parser = argparse.ArgumentParser(description='Base Command Class')


class Command:
    name = 'Command'

    def __init__(self, df, argsStr):
        self.df = df

    @staticmethod
    def help():
        parser.print_help()

    def execute(self) -> pd.DataFrame:
        pass
