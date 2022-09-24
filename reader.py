"""
エクセルのデータを読み込むクラス
"""
from typing import List
import pandas as pd

# 電気代/発電量
WS_DENKI_NAME: str = '電気'
ROWNO_DENKI_HEADER: int = 2
WS_DENKI_USECOLS: List[int] = [0, 3, 4, 5, 6, 7, 8]
WS_DENKI_COL_DATE: str = 'DATE'
WS_DENKI_COL_DAYTIME: str = 'DAY_TIME'
WS_DENKI_COL_MOREVTIME: str = 'MOREV_TIME'
WS_DENKI_COL_NIGHTTIME: str = 'NIGHT_TIME'
WS_DENKI_COL_PAYMENT: str = 'PAYMENT'
WS_DENKI_COL_ELECGEN: str = 'ELEC_GEN'
WS_DENKI_COL_SALE: str = 'SALE'
WS_DENKI_NAMES: List[str] = [
    WS_DENKI_COL_DATE,
    WS_DENKI_COL_DAYTIME,
    WS_DENKI_COL_MOREVTIME,
    WS_DENKI_COL_NIGHTTIME,
    WS_DENKI_COL_PAYMENT,
    WS_DENKI_COL_ELECGEN,
    WS_DENKI_COL_SALE
]

# 水道代
WS_SUIDO_NAME: str = '水道'
ROWNO_SUIDO_HEADER: int = 1
WS_SUIDO_USECOLS: List[int] = [0, 2, 3]
WS_SUIDO_COL_DATE: str = 'DATE'
WS_SUIDO_COL_AMOUNT: str = 'AMOUNT'
WS_SUIDO_COL_PAYMENT: str = 'PAYMENT'
WS_SUIDO_NAMES: List[str] = [
    WS_SUIDO_COL_DATE,
    WS_SUIDO_COL_AMOUNT,
    WS_SUIDO_COL_PAYMENT
]

# 共通
WS_COL_YEAR: str = 'YEAR'
WS_COL_MONTH: str = 'MONTH'

class Reader:
    def __init__(self, file: str) -> None:
        self._denki_data: pd.DataFrame = self._read_denki(file)
        self._suido_data: pd.DataFrame = self._read_suido(file)
    
        self.denki_years: List[int] = sorted(self._denki_data[WS_COL_YEAR].unique())
        self.suido_years: List[int] = sorted(self._suido_data[WS_COL_YEAR].unique())

    def _read_denki(self, file: str):
        """
        電気代データを読み込む
        """
        df: pd.DataFrame = pd.read_excel(
            file,
            sheet_name=WS_DENKI_NAME,
            header=ROWNO_DENKI_HEADER,
            usecols=WS_DENKI_USECOLS,
            names=WS_DENKI_NAMES)
        df[WS_COL_YEAR] = df[WS_DENKI_COL_DATE].dt.year
        df[WS_COL_MONTH] = df[WS_DENKI_COL_DATE].dt.month
        return df

    def _read_suido(self, file: str):
        """
        電気代データを読み込む
        """
        df: pd.DataFrame = pd.read_excel(
            file,
            sheet_name=WS_SUIDO_NAME,
            header=ROWNO_SUIDO_HEADER,
            usecols=WS_SUIDO_USECOLS,
            names=WS_SUIDO_NAMES)
        df[WS_COL_YEAR] = df[WS_SUIDO_COL_DATE].dt.year
        df[WS_COL_MONTH] = df[WS_SUIDO_COL_DATE].dt.month
        return df

def factory() -> Reader:
    import configparser
    cfg = configparser.ConfigParser()
    cfg.read('config.ini', encoding='utf-8')
    return Reader(cfg['Reader']['FILE_UTILITY_COST'])