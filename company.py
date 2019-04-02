from historical import Historical


class Company():
    def __init__(self, symbol):
        self.__symbol = symbol
        self.__records = [ ]

    def add_records(self, stock_historical):
        for day in stock_historical:
            record = Historical(self.__symbol, day, stock_historical[ day ][ '1. open' ],
                                stock_historical[ day ][ '2. high' ], stock_historical[ day ][ '3. low' ],
                                stock_historical[ day ][ '4. close' ], stock_historical[ day ][ '5. volume' ])

            self.__records.append(record)

    @property
    def records(self):
        return self.__records

    @property
    def count_records(self):
        return len(self.records)
