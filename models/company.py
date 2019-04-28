from models.historical import Historical


class Company():
    """
    The Company Class represent a Company Unit.
    There is a main attribute called symbol that means a Company Code.
    """
    def __init__(self, symbol):
        self.__symbol = symbol
        self.__records = [ ]
        self.__balances = [ ]

    def add_records(self, stock_historical):
        """
           This Function receives a historical dictionary, assign each element and finally add to a list.
        """
        for day in stock_historical:
            record = Historical(self.__symbol, day, stock_historical[ day ][ '1. open' ],
                                stock_historical[ day ][ '2. high' ], stock_historical[ day ][ '3. low' ],
                                stock_historical[ day ][ '4. close' ], stock_historical[ day ][ '5. volume' ])

            self.__records.append(record)

    @property
    def symbol(self):
        return self.__symbol

    @property
    def records(self):
        return self.__records

    @property
    def count_records(self):
        return len(self.records)

    def set_balances(self, list_balances):
        self.__balances = list_balances

    @property
    def balances(self):
        return self.__balances