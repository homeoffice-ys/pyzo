import json
import matplotlib.pyplot as plt
import numpy as np
import Arima_algo as aa
import warnings
from types import SimpleNamespace
#from datetime
import datetime
import re

full_path = r"C:\Users\Yochanan\Documents\Data\json\result.json"

full_path = r"C:\Users\Yochanan\PycharmProjects\HMM\data\currency_data\EUR_USD.json"

with open(full_path) as input_file:
    data = json.load(input_file)

print(data.keys())
input('stop')
print(data)

# for key,val in data.items():
#     exec(key + '=val')
# candles
# data['candles'][0]['mid']['o']
# for key in data:
#    print("key: %s , value: %s" % (key, data[key]))

LD = len(data['candles'])
print(LD)
dat1 = [None] * LD
dat2 = [None] * LD
x = np.arange(LD)

for idx, val in enumerate(data['candles']):
    str = val['time']
    print(str)
    str = datetime.datetime(*map(int, re.split('[^\d]', str)[:-1])).date()
    print(str)
    print()
    dat1[idx] = float(val['mid']['o'])
    dat2[idx] = int(val['volume'])


fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x, dat1, 'g-')
ax2.plot(x, dat2, 'b-')

ax1.set_xlabel('Days')
ax1.set_ylabel('Open', color='g')
ax2.set_ylabel('Volume', color='b')
plt.tight_layout()

plt.show()

plt.plot(dat1)
plt.title(data['instrument'] + ', gran = ' + data['granularity'])
plt.show()

p_values = [0, 1, 2]
d_values = range(0, 3)
q_values = range(0, 3)
warnings.filterwarnings("ignore")
#aa.evaluate_models(np.asarray(dat), p_values, d_values, q_values)
mse, test, pred = aa.evaluate_arima_model(dat1, (0, 1, 0))


plt.plot(dat1)
plt.plot(np.arange(LD-len(test),122), test)
plt.plot(np.arange(LD-len(test)-1,121), pred, 'o-')
plt.title(data['instrument'] + ', gran = ' + data['granularity'])
plt.show()