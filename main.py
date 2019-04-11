from dao.connection import get_stocks
from models.company import Company
from helpers.helpers import apresentation,ask_user


def play():
    apresentation()
    carry_on=True

    while carry_on:
        stock_data = get_stocks(ask_user())

        if (stock_data[1] is 0):
            stock_metadata = stock_data[0][ 'Meta Data' ]
            company_symbol = stock_metadata[ '2. Symbol' ]
            company = Company(company_symbol)

            stock_historical = stock_data[0][ 'Time Series (Daily)' ]
            company.add_records(stock_historical)
        else:
            continue

if __name__ == '__main__':
   play()





