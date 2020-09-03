

from data_factory import DataFactory
from monte_carlo_strat import MonteCarloStrat

import backtrader as bt
import backtrader.feeds as btfeeds
import os
import pandas as pd
import datetime




def main():
    #make some dummy data
    # DataFactory().make_data("monte_carlo", "test_data.csv")
    df = pd.read_csv('test_data.csv')

    #Initialis cerebro - the brains of the back trader framework
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000.0)
    cerebro.addstrategy(MonteCarloStrat)

    
    data = btfeeds.GenericCSVData(
        dataname='test_data.csv',

        fromdate=datetime.datetime(2020, 1, 1),
        todate=datetime.datetime(2020, 1, 3),

        nullvalue=0.0,

        dtformat=('%Y-%m-%d'),

        datetime=0,
        high=1,
        low=2,
        open=3,
        close=4,
        volume=5,
        openinterest=-1
    )
    
    cerebro.adddata(data)



    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()
    # cerebro.plot()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())


if __name__ == "__main__":
    main()