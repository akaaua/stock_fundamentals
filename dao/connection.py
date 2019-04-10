import urllib.parse
import requests


def get_stocks(company_symbol):
    main_api = "https://www.alphavantage.co/query?"
    period = 'TIME_SERIES_DAILY'
    outputsize = 'compact'
    api_key = '70CCIQQ5ZMGX1Y1O'

    url = main_api + urllib.parse.urlencode({"function": period}) + "&" + urllib.parse.urlencode(
        {"symbol": company_symbol}) + "&" + urllib.parse.urlencode({"outputsize": outputsize}) + "&" + urllib.parse.urlencode(
        {"apikey": api_key})

    json_data = call_api(url)
    return json_data


def get_currency():
    main_api = "https://www.alphavantage.co/query?"
    period = 'CURRENCY_EXCHANGE_RATE'
    from_currency = 'USD'
    to_currency = 'BRL'
    api_key = '70CCIQQ5ZMGX1Y1O'

    url = main_api + urllib.parse.urlencode({"function": period}) + "&" + urllib.parse.urlencode(
        {"from_currency": from_currency}) + "&" + urllib.parse.urlencode(
        {"to_currency": to_currency}) + "&" + urllib.parse.urlencode(
        {"apikey": api_key})

    json_data = call_api(url)
    return json_data


def call_api(url):


    try:
        json_data = requests.get(url).json()
    except Exception as err:
        print('Something is wrong: {}'.format(err))
        return (None, 1)
    else:
        if 'Error Message' in json_data.keys():
            print('Company not found, please try again.')
            return (None, 1)
        else:
            return (json_data, 0)


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

