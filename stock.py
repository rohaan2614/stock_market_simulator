import pandas as pd
import seaborn as sns
import numpy as np
from utils import generate_random_string, time_stamp_now
from shares import Shares

sns.set_theme(style="darkgrid")

class Stock:

    def __init__(self, issuing_corporation : str, predicted_returns_file : str, 
                 actual_prices_file : str, stock_name : str = None, pred_col_name='predicted_RET', 
                 price_col_name='PRC', required_rate_of_return=0, time_min=0, time_max=None, time_step=1):
        self.issuer = issuing_corporation
        self.shares : list(Shares) = []
        self.predictions_column_name = pred_col_name
        self.price_column_name = price_col_name
        self.required_return_rate = required_rate_of_return
        self.time_min = time_min
        self.time_max = time_max
        self.time_step = time_step
        
        # Generate a random name if name not provided
        if stock_name is None:
            self.name = generate_random_string(10)
        else:
            self.name = stock_name
        
        # to read predicted returns from the source csv
        self.__read_return_predictions_csv(file_path=predicted_returns_file)
        # to read actual returns from the source csv
        self.__read_stock_price_csv(file_path=actual_prices_file)
        
    def set_required_rate_of_return(self, required_rate):
        self.required_return_rate = required_rate
        
    def reset(self):
        """Why do we need this method?"""
        self.shares = []
        self.bought_price = 0

    def __read_return_predictions_csv(self, file_path):
        self.predicted_returns = pd.read_csv(file_path, usecols=[self.predictions_column_name]).to_numpy().flatten()
        self.sample_size = len(self.predicted_returns)
        self.time = np.arange(start=self.time_min, stop=self.sample_size, step=self.time_step)

    def __read_stock_price_csv(self, file_path):
        self.actual_prices = pd.read_csv(file_path, usecols=[self.price_column_name]).to_numpy().flatten()
        if len(self.predicted_returns) != 0:
            if len(self.predicted_returns) + 1 != len(self.actual_prices):
                print('Length of predicted_return is not equal to price')
                exit()
                
    def about_me(self):
        print(f'Hi, I represent {self.name} stock issued by {self.issuer} corporation. Currently, I have {len(self.shares)} shares in the market!')
        
    def plot_predicted_returns(self, optional_filename=None, file_extension=".png"):
        if optional_filename is None:
            filename = time_stamp_now() + '_' + generate_random_string(4)
        else:
            filename = optional_filename
            
        filename += file_extension

        # sns_plot = sns.lineplot(x=self.time_dimension, y=self.actual_prices,
        #             # hue="region", style="event",
        #             # data=fmri
        #             )
        ax=sns.lineplot(y=self.predicted_returns, x=self.time)
        ax.axhline(y=self.required_return_rate, color='red')
        ax.get_figure().savefig(filename)
        
        print (f"plot saved as {filename}")
        
    
    def plot_actual_prices(self, optional_filename=None, file_extension=".png"):
        if optional_filename is None:
            filename = time_stamp_now() + '_' + generate_random_string(4)
        else:
            filename = optional_filename
            
        filename += file_extension

        sns_plot = sns.lineplot(x=self.time_dimension, y=self.actual_prices,
                    # hue="region", style="event",
                    # data=fmri
                    )
        
        print (f"plot saved as {filename}" if sns_plot.get_figure().savefig(filename) else "Error executing plot_actual_prices")
        
    # def plot_predicted_return_vs_price(self):
        