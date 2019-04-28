import pandas as pd
from models.balance import Balance

def get_data(symbol):
    url = 'archieve/bal_{}.xls'.format(symbol)
    raw_data = pd.read_excel(url, sheet_name=0, header=None, skiprows=1)
    header = raw_data.iloc[0]
    header[0] = 'Indicadores'
    raw_data = raw_data[1:]
    data_indexed = raw_data.rename(columns = header)
    series = []
    for i in range(1,len(header)):
        series.append(data_indexed[ header[ i ] ])
    return data_indexed


def get_balance_values(symbol):
    data_indexed = get_data(symbol)
    list_balance = []

    for y in range(1, data_indexed.shape[1]):
        balance = Balance(
            data_indexed.iloc[ 0, y ], data_indexed.iloc[ 1, y ], data_indexed.iloc[ 2, y ],
            data_indexed.iloc[ 3, y ], data_indexed.iloc[ 4, y ], data_indexed.iloc[ 5, y ], data_indexed.iloc[ 6, y ],
            data_indexed.iloc[ 7, y ], data_indexed.iloc[ 8, y ], data_indexed.iloc[ 9, y ], data_indexed.iloc[ 10, y ],
            data_indexed.iloc[ 11, y ], data_indexed.iloc[ 12, y ], data_indexed.iloc[ 13, y ],
            data_indexed.iloc[ 14, y ],
            data_indexed.iloc[ 15, y ], data_indexed.iloc[ 16, y ], data_indexed.iloc[ 17, y ],
            data_indexed.iloc[ 18, y ],
            data_indexed.iloc[ 19, y ], data_indexed.iloc[ 20, y ], data_indexed.iloc[ 21, y ],
            data_indexed.iloc[ 22, y ],
            data_indexed.iloc[ 23, y ], data_indexed.iloc[ 24, y ], data_indexed.iloc[ 25, y ],
            data_indexed.iloc[ 26, y ],
            data_indexed.iloc[ 27, y ], data_indexed.iloc[ 28, y ], data_indexed.iloc[ 29, y ],
            data_indexed.iloc[ 30, y ],
            data_indexed.iloc[ 31, y ], data_indexed.iloc[ 32, y ], data_indexed.iloc[ 33, y ],
            data_indexed.iloc[ 34, y ], data_indexed.iloc[ 35, y ], data_indexed.iloc[ 36, y ],
            data_indexed.iloc[ 37, y ],
            data_indexed.iloc[ 38, y ], data_indexed.iloc[ 39, y ], data_indexed.iloc[ 40, y ],
            data_indexed.iloc[ 41, y ],
            data_indexed.iloc[ 42, y ], data_indexed.iloc[ 43, y ], data_indexed.iloc[ 44, y ],
            data_indexed.iloc[ 45, y ],
            data_indexed.iloc[ 46, y ], data_indexed.iloc[ 47, y ], data_indexed.iloc[ 48, y ],
            data_indexed.iloc[ 49, y ],
            data_indexed.iloc[ 50, y ], data_indexed.iloc[ 51, y ], data_indexed.iloc[ 52, y ],
            data_indexed.iloc[ 53, y ],
            data_indexed.iloc[ 54, y ])

        list_balance.append(balance)

    return list_balance

#    for x in range(0, data_indexed.shape[0]):
#           print(data_indexed.iloc[x,y])
