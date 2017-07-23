from scboy.command.command import Command
import pandas as pd


class TestSeries(Command):
    name = 'TestSeries'

    def __init__(self, df, argsStr):
        if df is None:
            self.df = pd.DataFrame({'open': [1., 2., 3., 4., 5.],
                                    'close': [5., 4., 3., 2., 1.],
                                    'high': [6., 4., 3., 3., 2.],
                                    'low': [4., 3., 1., 1., 1.]})
        else:
            self.df = df

    def execute(self) -> pd.DataFrame:
        return self.df


