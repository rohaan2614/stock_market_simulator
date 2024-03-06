import pandas as pd
import os
import numpy as np
from Shares import Shares

class Stock:

    def __init__(self, stock_name : str, issuing_corporation : str, predicted_returns : np.ndarray, 
                 actual_prices : np.ndarray):
        self.name = stock_name
        self.issuer = issuing_corporation
        self.predicted_returns = predicted_returns
        self.actual_prices = actual_prices
        self.shares : list(Shares) = []
        
        self.__read_return_predictions()
        
    def reset(self):
        """Why do we need this method?"""
        self.shares = []
        self.bought_price = 0

    def __read_return_predictions(self, file_path):
        self.return_prediction = pd.read_csv(file_path, usecols=['predicted_RET']).to_numpy().flatten()
        self.testing_period = len(self.return_prediction)

    def __read_stock_price(self, file_path):
        self.stock_price = pd.read_csv(file_path, usecols=['PRC']).to_numpy().flatten()
        if len(self.return_prediction) != 0:
            if len(self.return_prediction) + 1 != len(self.stock_price):
                print('Length of predicted_return is not equal to price')
                exit()