import pandas as pd
import os
from portfolio import Portfolio
from stock import Stock

if __name__ == '__main__':
    PREDICTION_DIR = "data/predictions"
    TEST_DIR = "data/test"
    stock_names = ['AAPL', 'AXP', 'BA', 'CAT', 'CSCO', 'CVX', 'DOW', 'DIS', 'WBA', 'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE',  'PG', 'TRV', 'UNH',  'VZ', 'V', 'WMT', 'HON', 'AMGN', 'CRM']
    spend_per_stock = 200
    portfolio = Portfolio(stock_names, spend_per_stock=spend_per_stock, money_pool=6000)
    return_strategy = 'simple_return'

    for stock_name in stock_names:
        company = Stock(stock_name)
        # print("loaded stock: ", stock_name)
        prediction_file = os.path.join(PREDICTION_DIR, stock_name + "_predictions.csv")
        test_file = os.path.join(TEST_DIR, stock_name + ".csv")
        company.read_return_prediction(prediction_file)
        company.read_stock_price(test_file)
        # print("stock {}  got data".format(stock_name))
        portfolio.add_company_to_protfolio(company)
        
    
    portfolio.trade(return_strategy)

    # for return_strategy in ['simple_return']:
    #     portfolio.reset()
    
    #     for stock_name in stock_names:
    #         prediction_file = os.path.join(PREDICTION_DIR, stock_name + "_predictions.csv")
    #         test_file = os.path.join(TEST_DIR, stock_name + ".csv")
    #         prediction = pd.read_csv(prediction_file, usecols=['predicted_RET']).to_numpy().flatten()
    #         stock_price = pd.read_csv(test_file, usecols=['PRC']).to_numpy().flatten()
    #         if return_strategy == 'simple_return':
    #             portfolio.simple_return(prediction, stock_price, stock_name)

    #     portfolio.get_return(return_strategy)
