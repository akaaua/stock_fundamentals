import urllib.parse
import requests

"""
This File has all the method that get data from API and create the file database.
"""


def get_stocks(company_symbol):
    """ The Method that receives a symbol and constructs the URL to connect to API """
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
    """ Method that get from API the currency rate, it will be used in the future implementation """
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
    """ The method that executes the connection to API and does the check """

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
    """ This method does the connection to a file database but first, check if exist a previously file """
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
    """
     This method creates a new file database.
    """
    import os
    path = 'database'
    try:
        os.mkdir(path)
    except OSError:
        print('Creation of the directory {} failed'.format(path))
    else:
        print('Successfully created the directory {} '.format(path))