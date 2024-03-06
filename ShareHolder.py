import pandas as pd
import os
from Shares import Shares


class ShareHolder:

    def __init__(self, name : str, starting_balance : float):
        self.name = name
        self.holdings = []
        self.balance = starting_balance
        
    def about_me(self):
        print(f'Hi, my name is {self.name}. I am a share holder with ${self.balance} and following holdings:')
        if len(self.holdings) > 0:
            for holding in self.holdings:
                print(holding)
        else:
            print("----NONE----")