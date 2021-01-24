from pathlib import Path
from preprocessing import transform
from urllib.request import urlretrieve
from pandas import read_csv


def all_data() -> None:
    _our_world_in_data()
    _reproductiegetal()


def _our_world_in_data() -> None:
    print('Fetching from https://ourworldindata.org/')
    raw_csv_path = Path('./data_raw/our_world_in_data.csv')
    csv_path = Path('./data/our_world_in_data.csv')
    urlretrieve('https://covid.ourworldindata.org/data/owid-covid-data.csv?v=2021-01-24', raw_csv_path)
    df = read_csv(raw_csv_path, decimal='.', sep=',')
    df.to_csv(csv_path, decimal=',', sep=';')


def _reproductiegetal() -> None:
    print('Fetching from https://coronadashboard.rijksoverheid.nl/')
    json_path = Path('./data_raw/reproductiegetal.json')
    csv_path = Path('./data/reproductiegetal.csv')
    urlretrieve('https://data.rivm.nl/covid-19/COVID-19_reproductiegetal.json', json_path)
    transform.json2csv(json_path, csv_path)
