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