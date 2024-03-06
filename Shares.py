import pandas as pd
import os
from stocks import Stock


class Shares:

    def __init__(self, identifier : str, stock : Stock, current_holdings : float):
        self.identifier = identifier
        self.stock = stock
        self.holdings = current_holdings