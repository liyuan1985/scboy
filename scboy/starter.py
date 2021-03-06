import pandas as pd

from scboy.command.atr import Atr
from scboy.command.col_cut import ColumnCut
from scboy.command.minmax import MinMax
from scboy.command.mva import Mva
from scboy.command.price import Price
from scboy.command.row_filter import RowFilter
from scboy.command.rsi import Rsi
from scboy.command.test_series import TestSeries

supprted_cmds = {'test_series': TestSeries.name,
                 'mva': Mva.name,
                 'price': Price.name,
                 'rsi': Rsi.name,
                 'atr': Atr.name,
                 'mm': MinMax.name,
                 'cut': ColumnCut.name,
                 'filter': RowFilter.name}


def execute_cmd(name, df, argStr) -> pd.DataFrame:
    if not name in supprted_cmds:
        raise ValueError('Unsupported command {}'.format(name))

    name = supprted_cmds[name]
    cmd = globals()[name](df, argStr)

    return cmd.execute()


def evaluate_head(argStr) -> pd.DataFrame:
    """
    we are not expecting Dataframe as input for the first command in the pipeline.
    The very first command supposed to initialise the Dataframe
    :param argStr: argment string
    :return: -> Dataframe
    """
    args = argStr.strip().split(' ')
    name = args[0]
    if len(args) == 1:
        argStr = ''
    else:
        argStr = ' '.join(args[1:])

    return execute_cmd(name, None, argStr)


def evaluate_pipe(argStr, df) -> pd.DataFrame:
    args = argStr.strip().split(' ')
    name = args[0]
    if len(args) == 1:
        argStr = ''
    else:
        argStr = ' '.join(args[1:])

    return execute_cmd(name, df, argStr)


def zealot(argStr):
    args = argStr.strip().split('|')
    ret = evaluate_head(args[0])
    for i in range(1, len(args)):
        ret = evaluate_pipe(args[i], ret)

    return ret
