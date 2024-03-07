import pandas as pd
import os
# from portfolio import Portfolio
from stock import Stock
from share_holder import ShareHolder

if __name__ == '__main__':
    PREDICTION_DIR = "data/predictions"
    TEST_DIR = "data/test"
    
    investor = ShareHolder("Mike", 10000)
    investor.about_me()
    
    # Create Stock
    test_stock = Stock(issuing_corporation="Amazon", 
                       predicted_returns_file="data/predictions/AMGN_predictions.csv",
                       actual_prices_file="data/test/AMGN.csv",
                       required_rate_of_return=0.002)
    test_stock.about_me()
    
    print(f"Actual Prices ({len(test_stock.actual_prices)}) ", test_stock.actual_prices)
    
    test_stock.plot_predicted_returns()
    
    # print(f"\nPredicted Returns ({len(test_stock.predicted_returns)}) ", test_stock.predicted_returns)

    # for predicted_return in pre
    # stock_names = ['AAPL', 'AXP', 'BA', 'CAT', 'CSCO', 'CVX', 'DOW', 'DIS', 'WBA', 'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE',  'PG', 'TRV', 'UNH',  'VZ', 'V', 'WMT', 'HON', 'AMGN', 'CRM']
    # spend_per_stock = 200
    # money_pool = 6000
    # portfolio = Portfolio(stock_names)
    # portfolio.set_initial_spend_per_stock(spend_per_stock)
    # portfolio.set_initial_money_pool(money_pool)
    # return_strategy = 'simple_return'
    # # return_strategy = 'portfolio_simple_return'

    # for stock_name in stock_names:
    #     company = Stock(stock_name)
    #     # print("loaded stock: ", stock_name)
    #     prediction_file = os.path.join(PREDICTION_DIR, stock_name + "_predictions.csv")
    #     test_file = os.path.join(TEST_DIR, stock_name + ".csv")
    #     company.read_return_prediction(prediction_file)
    #     company.read_stock_price(test_file)
    #     # print("stock {}  got data".format(stock_name))
    #     portfolio.add_company_to_protfolio(company)
        
    
    # portfolio.trade(return_strategy)

