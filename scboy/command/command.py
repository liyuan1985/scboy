import pandas as pd


class Command:
    name = 'Command'

    def __init__(self, df, argsStr):
        self.df = df

    def help(self):
        pass

    def execute(self) -> pd.DataFrame:
        pass
