import pandas as pd
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot

from scboy.command.command import Command

init_notebook_mode(connected=True)


class KChart(Command):

    def __init__(self, df, argsStr=None):

        self.df = df.iloc[0:500]

    @staticmethod
    def help():
        pass

    def execute(self) -> pd.DataFrame:
        trace = go.Candlestick(x=self.df.index, open=self.df.open, high=self.df.high, low=self.df.low, close=self.df.close)
        data = [trace]
        iplot(data, filename='Price')
        return self.df

