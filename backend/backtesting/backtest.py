import backtrader as bt
import pandas as pd
from backend.backtesting.strategies.sma_strategy import SmaCross

def run_backtest(datafile, strategy=SmaCross, cash=10000, commission=0.001, stake=10):
    # Load data
    data = pd.read_csv(datafile, index_col='Date', parse_dates=True)
    datafeed = bt.feeds.PandasData(dataname=data)

    # Initialize Cerebro engine
    cerebro = bt.Cerebro()
    cerebro.adddata(datafeed)
    cerebro.addstrategy(strategy)
    cerebro.broker.set_cash(cash)
    cerebro.addsizer(bt.sizers.FixedSize, stake=stake)
    cerebro.broker.setcommission(commission=commission)

    # Run the backtest
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Plot the result
    cerebro.plot()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run Backtrader backtest')
    parser.add_argument('--datafile', type=str, required=True, help='CSV file with historical data')
    args = parser.parse_args()

    run_backtest(datafile=args.datafile)
