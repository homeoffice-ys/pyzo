import datetime
import warnings
import numpy as np
from matplotlib import cm, pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator
import json
from dateutil import parser

# try:
#    from mpl_finance import quotes_historical_yahoo_och1
# except ImportError:
#    from mpl_finance import (
#       quotes_historical_yahoo as quotes_historical_yahoo_och1)

from hmmlearn.hmm import GaussianHMM

# start_date = datetime.date(1995, 10, 10)
# end_date = datetime.date(2015, 4, 25)
# quotes = quotes_historical_yahoo_och1('INTC', start_date, end_date)
#
# closing_quotes = np.array([quote[2] for quote in quotes])
#
# volumes = np.array([quote[5] for quote in quotes])[1:]

with open(r"C:\Users\Yochanan\Documents\Data\json\result.json") as input_file:
    data = json.load(input_file)

LD = len(data['candles'])
closing_quotes = [None] * LD
volumes = [None] * LD
dates = [None] * LD

for idx, val in enumerate(data['candles']):
    closing_quotes[idx] = float(val['mid']['c'])
    volumes[idx] = int(val['volume'])
    dates[idx] = parser.parse(val['time'])

start_date = dates[0]
end_date = dates[-1]


diff_percentages = 100.0 * np.diff(closing_quotes) / closing_quotes[:-1]
#dates = np.array([quote[0] for quote in quotes], dtype = np.int)[1:]
training_data = np.column_stack([diff_percentages, np.asarray(volumes[:-1])])

hmm = GaussianHMM(n_components = 7, covariance_type = 'diag', n_iter = 1000)
with warnings.catch_warnings():
   warnings.simplefilter('ignore')
   hmm.fit(training_data)

num_samples = LD + 7
samples, _ = hmm.sample(num_samples)

plt.figure()
plt.title('Difference percentages')
plt.plot(np.arange(num_samples), samples[:, 0], c = 'black')

plt.figure()
plt.title('Volume of shares')
plt.plot(np.arange(num_samples), samples[:, 1], c = 'black')
plt.ylim(bottom = 0)
plt.show()