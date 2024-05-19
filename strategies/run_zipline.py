from toolz import merge 
import pandas as pd

from strategies.buy_and_hold import BuyAndHold
from strategies.auto_correlation import AutoCorrelation


from zipline import run_algorithm
from zipline.utils.calendar_utils import register_calendar, get_calendar
#from zipline.utils.calendars import register_calendar, get_calendar
from os import environ
import pandas_datareader.data as web



# Define your benchmark symbol

start = pd.Timestamp('2012')
end = pd.Timestamp('2018')

#sp500 = web.DataReader('^GSPC', 'yahoo', start, end).SP500
sp500 = web.DataReader('SP500', 'fred', start, end).SP500

benchmark_returns = sp500.pct_change()

#print(benchmark_returns)

# Columns that we expect to be able to reliably deterministic
_cols_to_check = [
    'algo_volatility',
    'algorithm_period_return',
    'benchmark_period_return',
    'benchmark_volatility',
    'capital_used',
    'ending_cash',
    'ending_value',
    'excess_return',
    'long_value',
    'period_close',
    'period_open',
    'portfolio_value',
    'returns',
    'short_value',
    'shorts_count',
    'starting_cash',
    'starting_exposure',
    'starting_value',
    'trading_days',
]
 
 
def run_strategy(strategy_name):
    mod = None


    
    if strategy_name == "buy_and_hold": 
        mod = BuyAndHold()
    elif strategy_name == "auto_correlation":
        mod = AutoCorrelation()
 
    register_calendar("YAHOO", get_calendar("NYSE"), force=True)
 
    return run_algorithm(
        initialize=getattr(mod, 'initialize', None),
        handle_data=getattr(mod, 'handle_data', None),
        before_trading_start=getattr(mod, 'before_trading_start', None),
        analyze=getattr(mod, 'analyze', None),
        bundle='quandl',
        benchmark_returns=benchmark_returns,  # Specify the benchmark symbol here
        environ=environ,
        # Provide a default capital base, but allow the test to override.
        **merge({'capital_base': 1e3}, mod._test_args())
    )


 
 











 