from datetime import datetime
from pandas import read_json, Series
from pathlib import Path


def json2csv(input_path: Path, output_path: Path) -> None:
    df = read_json(input_path)
    df.to_csv(Path(output_path), decimal=',', sep=';')


def dates2num_dates(dates: Series) -> Series:
    days_in_a_year = 365
    first_of_month_value = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    num_dates = Series(index=dates.index)
    for row, value in dates.iteritems():
        date_time = datetime.strptime(value, '%Y-%m-%d')
        num_dates.iloc[row] = date_time.year + (first_of_month_value[date_time.month-1] + date_time.day) / days_in_a_year
    return num_dates
