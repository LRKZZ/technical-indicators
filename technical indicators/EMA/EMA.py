import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

df = pd.read_csv('MOEX.SBER_SMAL_220501_230523 (2).csv', delimiter=',')

def Stock_EMA(): #функция EMA-индикатора
    global df
    current_date = str(date.today().day) + '/' + str(date.today().month) + '/' + str(date.today().year)
    EMA50 = pd.DataFrame()
    EMA50['Close Price'] = df['<CLOSE>'].ewm(span=50).mean()
    EMA200 = pd.DataFrame()
    EMA200['Close Price'] = df['<CLOSE>'].ewm(span=200).mean()
    EMA21 = pd.DataFrame()
    EMA21['Close Price'] = df['<CLOSE>'].ewm(span=21).mean()
    data = pd.DataFrame()
    data['Stock'] = df['<CLOSE>']
    data['EMA21'] = EMA21['Close Price']
    data['EMA50'] = EMA50['Close Price']
    data['EMA200'] = EMA200['Close Price']

    # Визуализируем
    plt.figure(figsize=(12.6, 4.6))
    plt.plot(data['Stock'], alpha=0.35)
    plt.plot(EMA21['Close Price'], label='EMA21', alpha=0.35)
    plt.plot(EMA50['Close Price'], label='EMA50', alpha=0.35)
    plt.plot(EMA200['Close Price'], label='EMA200', alpha=0.35)
    plt.title(' history (EMA)')
    plt.xlabel('01/01/2022 - ' + current_date)
    plt.ylabel('Close price')
    plt.legend(loc='upper left')
    plt.show()

Stock_EMA()

