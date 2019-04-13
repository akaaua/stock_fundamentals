from models.company import Company

def apresentation():
    print("**************************************")
    print("*** Wellcome to Stock Fundamentals ***")
    print("**************************************")


def ask_user():
    company_symbol = input('\n Please, insert the company symbol: ')
    return company_symbol

def isValid(stock_data):

    if (stock_data[ 1 ] is 0):
        return True
    else:
        return False

def extract_values(stock_data):
    stock_metadata = stock_data[0][ 'Meta Data' ]
    company_symbol = stock_metadata[ '2. Symbol' ]
    company = Company(company_symbol)
    stock_historical = stock_data[0][ 'Time Series (Daily)' ]
    company.add_records(stock_historical)
    return company

def print_results(company):
    print('Company Symbol: {}'.format(company.symbol))
    print('Total of records are: {}'.format(company.count_records))
    print('Date: {}, the close value was: {:02.2f}, {:02.2f}% of difference from yesterday.' \
          .format(company.records[ 0 ].date, \
                  company.records[ 0 ].close, \
                  (100 - company.records[ 0 ].close / company.records[ 1 ].close * 100)))
    print('The High value was: {:02.2f} and the Lowest value: {:02.2f}.'.format(company.records[ 0 ].high,
                                                                                company.records[ 0 ].low))
    print('The difference between the Highest and the Lowest values is: {:02.2f}%'.format(
        100 - company.records[ 0 ].low / company.records[ 0 ].high * 100))