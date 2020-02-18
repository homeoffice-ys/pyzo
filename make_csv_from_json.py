import json
import csv
import datetime
import re

full_path = r"C:\Users\Yochanan\PycharmProjects\HMM\data\currency_data\EUR_USD.json"
write_path = r"C:\Users\Yochanan\PycharmProjects\HMM\data\currency_data\EUR_USD.csv"

with open(full_path) as input_file:
    data = json.load(input_file)

    with open(write_path, 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['date', 'open', 'high', 'low', 'close'])

        for idx, val in enumerate(data['candles']):

            str = val['time']
            date = datetime.datetime(*map(int, re.split('[^\d]', str)[:-1])).date()
            open = float(val['mid']['o'])
            high = float(val['mid']['h'])
            low = float(val['mid']['l'])
            close = float(val['mid']['c'])
            thewriter.writerow([date, open, high, low, close])

