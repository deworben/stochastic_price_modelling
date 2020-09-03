
import pandas as pd
import numpy as np


class DataFactory():

    def __init__(self):
        # super().__init__()
        pass

    def make_data(self, data_type, path):
        # To do: Convert these into enum
        if data_type == "monte_carlo":
            self._make_monte_carlo_data(path)

    def _make_monte_carlo_data(self, path):
        #Make 100 random data points for now
        df = pd.DataFrame(np.random.randint(0,100,size=(100, 6)), columns=['Open', 'High', 'Low', 'Close', 'Volume', 'OpenInterest'])
        df['date'] = pd.date_range(start='1/1/2020', periods=len(df), freq='1D20min')
        df = df.set_index('date')
        df.to_csv(path)