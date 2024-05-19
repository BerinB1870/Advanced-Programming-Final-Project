from zipline.api import order, symbol, record, set_benchmark
from matplotlib import pyplot as plt
import pandas as pd


class BuyAndHold:
    
    #stocks = ['AAPL', 'MSFT', 'TSLA']

    stocks = ['TSLA']
    
    def initialize(self, context):
        context.has_ordered = False
        context.stocks = self.stocks
        context.asset = symbol('TSLA')
     
    def handle_data(self, context, data):
        if not context.has_ordered:
            for stock in context.stocks:
                order(symbol(stock), 100)
            context.has_ordered = True
        
        record(TSLA=data.current(context.asset, 'price'))

    def _test_args(self):
        return {
            'start': pd.Timestamp('2012', tz='utc'),
            'end': pd.Timestamp('2018', tz='utc'),
            'capital_base': 1e3
        }
    
    def analyze(self, context, perf):
        fig = plt.figure()
        ax1 = fig.add_subplot(211)
        perf.portfolio_value.plot(ax=ax1)
        ax1.set_ylabel('portfolio value in $')
    
        ax2 = fig.add_subplot(212)
        perf['TSLA'].plot(ax=ax2)

        ax2.set_ylabel('price in $')
        plt.legend(loc=0)
        plt.show()
