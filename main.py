from dao.connection import get_stocks
from helpers.helpers import apresentation,ask_user,isValid,extract_values


def play():
    apresentation()

    carry_on=True

    while carry_on:

        stock_data = get_stocks(ask_user())

        if (isValid(stock_data)):
            company = extract_values(stock_data)
            print('Company with Symbol: {}'.format(company.symbol))
            print('Total of record is: {}'.format(company.count_records))
            print('List of records are: {}'.format(company.records))
        else:
            continue

if __name__ == '__main__':
   play()