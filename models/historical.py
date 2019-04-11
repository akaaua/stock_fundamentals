from _datetime import datetime

class Historical:
    """
    This Class represents a unit of historical, in other words, each instance of this class is one day.
    """
    def __init__(self, cod, date, open, high, low, close, volume):
        """
        In this method, each value is  assigned to your respective attributes
        """
        self.__cod = cod
        self.__date = datetime.strptime(date, '%Y-%m-%d').date()
        self.__open = float(open)
        self.__high = float(high)
        self.__low = float(low)
        self.__close = float(close)
        self.__volume = int(volume)

    @property
    def cod(self):
        return self.__cod

    @property
    def date(self):
        return self.__date

    @property
    def open(self):
        return self.__open

    @property
    def high(self):
        return self.__high

    @property
    def low(self):
        return self.__low

    @property
    def close(self):
        return self.__close

    @property
    def volume(self):
        return self.__volume
