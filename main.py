from dao.connection import get_stocks
from helpers.helpers import apresentation, ask_user, isValid, extract_values, print_results


def play():
    apresentation()

    carry_on = True

    while carry_on:

        stock_data = get_stocks(ask_user())

        if (isValid(stock_data)):
            company = extract_values(stock_data)
            print_results(company)

        else:
            continue


if __name__ == '__main__':
    play()
