import urllib.parse
import requests


def get_stocks():
    API = "70CCIQQ5ZMGX1Y1O"
    main_api = "https://www.alphavantage.co/query?"
    period = 'TIME_SERIES_DAILY'
    symbol = 'ABEV'
    outputsize = 'compact'
    api_key = '70CCIQQ5ZMGX1Y1O'

    url = main_api + urllib.parse.urlencode({"function": period}) + "&" + urllib.parse.urlencode(
        {"symbol": symbol}) + "&" + urllib.parse.urlencode({"outputsize": outputsize}) + "&" + urllib.parse.urlencode(
        {"apikey": api_key})

    json_data = requests.get(url).json()
    print(url)
    print(json_data)


def get_currency():
    API = "70CCIQQ5ZMGX1Y1O"
    main_api = "https://www.alphavantage.co/query?"
    period = 'CURRENCY_EXCHANGE_RATE'
    from_currency = 'USD'
    to_currency = 'BRL'
    api_key = '70CCIQQ5ZMGX1Y1O'

    url = main_api + urllib.parse.urlencode({"function": period}) + "&" + urllib.parse.urlencode(
        {"from_currency": from_currency}) + "&" + urllib.parse.urlencode(
        {"to_currency": to_currency}) + "&" + urllib.parse.urlencode(
        {"apikey": api_key})

    json_data = requests.get(url).json()
    print(url)
    print(json_data)


def connect_database():
    path = 'database/database.py'
    try:
        database = open(path, 'w+')
        print('Successfully connected to the database')
    except:
        print('Something is wrong and you will need to create a new database.')
        create_database()
        database = open(path, 'w+')
        print('Successfully connected to the database')
    return database


def create_database():
    import os
    path = 'database'
    try:
        os.mkdir(path)
    except OSError:
        print('Creation of the directory {} failed'.format(path))
    else:
        print('Successfully created the directory {} '.format(path))


if __name__ == '__main__':
    pass

