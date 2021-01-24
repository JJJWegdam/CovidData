from pandas import read_csv
from pathlib import Path
from preprocessing import calculate, transform
import matplotlib.pyplot as plt


months = [2020, 2020 + 31 / 365, 2020 + 59 / 365, 2020 + 90 / 365, 2020 + 120 / 365, 2020 + 151 / 365, 2020 + 181 / 365, 2020 + 212 / 365,
          2020 + 243 / 365, 2020 + 273 / 365, 2020 + 304 / 365, 2020 + 334 / 365, 2021, 2021 + 31 / 365, 2021 + 59 / 365]
month_names = ['1jan', '1feb', '1mrt', '1apr', '1mei', '1jun', '1jul', '1aug', '1sep', '1okt', '1nov', '1dec',
               '1jan', '1feb', '1mrt']


def reproductiegetal() -> None:
    df = read_csv(Path('./data/reproductiegetal.csv'), delimiter=';', decimal=',', index_col=0)
    df.Date = transform.dates2num_dates(df.Date)
    plt.fill_between(df.Date, df.Rt_low, df.Rt_up, color='#6b8689', alpha=0.1)
    plt.plot(df.Date, df.Rt_avg, c='#e64616')
    plt.xticks(months, month_names)
    plt.yticks([0.5+0.1*i for i in range(11)])
    plt.xlim(months[6], months[13])
    plt.ylim(0.5, 1.5)
    plt.title('R')


def weekly_change() -> None:
    df = read_csv(Path('./data/our_world_in_data.csv'), delimiter=';', decimal=',', index_col=0)
    df = df[df.iso_code == 'NLD'].reset_index()
    df.date = transform.dates2num_dates(df.date)
    _, changes = calculate.weekly(df.new_cases)
    plt.plot(df.date, changes, c='#00a6d6')
    plt.xticks(months, month_names)
    plt.xlim(months[6], months[13])
    plt.ylim(-0.5, 1)
    plt.title('Weekly change')


def weekly_change_versus_r() -> None:
    reproductiegetal()

    df = read_csv(Path('./data/our_world_in_data.csv'), delimiter=';', decimal=',', index_col=0)
    df = df[df.iso_code == 'NLD'].reset_index()
    df.date = transform.dates2num_dates(df.date)
    _, changes = calculate.weekly(df.new_cases)
    changes = [i/2 + 1 for i in changes]
    dates = [date - 14 / 365 for date in df.date.to_list()]
    plt.plot(dates, changes, c='#00a6d6')
    plt.xticks(months, month_names)
    plt.xlim(months[6], months[13])
    plt.ylim(0.5, 1.5)
    plt.legend(['R', 'Weekly change - 14 days'])
    plt.title('Weekly change versus R')
