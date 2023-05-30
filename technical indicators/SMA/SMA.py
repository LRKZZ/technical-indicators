import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

df = pd.read_csv('MOEX.SBER_SMAL_220501_230523 (2).csv', delimiter=',')

def Stock_SMA():  #функция SMA-индикатора
    global df
    current_date = str(date.today().day) + '/' + str(date.today().month) + '/' + str(date.today().year)
    SMA30 = pd.DataFrame()
    SMA30['Close Price'] = df['<CLOSE>'].rolling(window=30).mean()
    SMA90 = pd.DataFrame()
    SMA90['Close Price'] = df['<CLOSE>'].rolling(window=90).mean()
    data = pd.DataFrame()
    data['Stock'] = df['<CLOSE>']
    data['SMA30'] = SMA30['Close Price']
    data['SMA90'] = SMA90['Close Price']
    #Визуализируем
    plt.figure(figsize=(12.6, 4.6))
    plt.plot(data['Stock'], alpha=0.35)
    plt.plot(SMA30['Close Price'], label='SMA30', alpha=0.35)
    plt.plot(SMA90['Close Price'], label='SMA90', alpha=0.35)
    plt.title(' history (SMA)')
    plt.xlabel('01/01/2022 - ' + current_date)
    plt.ylabel('Close price')
    plt.legend(loc='upper left')
    plt.show()

Stock_SMA()


