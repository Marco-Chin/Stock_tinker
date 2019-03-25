import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


def get_n_day_average(n = 50):
    average_value_array = [0] * (n-1)
    initial_start = 0
    initial_end = n-1

    start_index = initial_start
    end_index = initial_end
    while end_index < len(raw_values):
        time_period_values = raw_values[start_index:end_index]
        total = 0
        for v in time_period_values:
            total += v
        average = total/n
        average_value_array.append(average)

        start_index +=1
        end_index +=1

    for i in range(n):
        average_value_array[i] = average_value_array[n]

    return average_value_array
    
file_path = 'APPL_data.csv'
file_path1 = 'appl_rsi.csv'

data=pd.read_csv(file_path)
#data = data[1:500]

dates = data.Date.values
dates = matplotlib.dates.datestr2num(dates)

raw_values = data.Close.values
ave = get_n_day_average(n=50)
ave2 = get_n_day_average(n=200)

plt.title("Apple Stock")
plt.xlabel("Date")
plt.ylabel("Stock value")


plt.plot_date(dates, raw_values, ms = .5, label = "raw_stock")
plt.plot_date(dates, ave, ms = .5, label = "50")
plt.plot_date(dates, ave2, ms = .5, label = "200")

legend = plt.legend(loc='lower right')
# Put a nicer background color on the legend.
plt.show()
