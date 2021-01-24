from pandas import read_csv
from pathlib import Path
from preprocessing import transform
import matplotlib.pyplot as plt


months = [2020, 2020 + 31 / 365, 2020 + 59 / 365, 2020 + 90 / 365, 2020 + 120 / 365, 2020 + 151 / 365, 2020 + 181 / 365, 2020 + 212 / 365,
          2020 + 243 / 365, 2020 + 273 / 365, 2020 + 304 / 365, 2020 + 334 / 365, 2021, 2021 + 31 / 365, 2021 + 59 / 365]
month_names = ['1jan', '1feb', '1mrt', '1apr', '1mei', '1jun', '1jul', '1aug', '1sep', '1okt', '1nov', '1dec',
               '1jan', '1feb', '1mrt']


def reproductiegetal() -> None:
    df = read_csv(Path('./data/reproductiegetal.csv'), delimiter=';', decimal=',', index_col=0)
    df.Date = transform.dates2num_dates(df.Date)
    plt.fill_between(df.Date, df.Rt_low, df.Rt_up, color='#6b8689', alpha=0.1)
    plt.plot(df.Date, df.Rt_avg, c='#00a6d6')
    plt.xticks(months, month_names)
    plt.yticks([0.5+0.1*i for i in range(11)])
    plt.xlim(months[6], months[13])
    plt.ylim(0.5, 1.5)
    plt.title('R')
    plt.show()


def weekly_change() -> None:
    df = read_csv(Path('./data/reproductiegetal.csv'), delimiter=';', decimal=',', index_col=0)

