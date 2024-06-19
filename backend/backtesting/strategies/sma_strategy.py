import backtrader as bt

class SmaCross(bt.Strategy):
    params = (('pfast', 10), ('pslow', 30),)

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.params.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.params.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if self.crossover > 0:  # if fast crosses slow to the upside
            self.buy()
        elif self.crossover < 0:  # in the market & cross to the downside
            self.sell()
