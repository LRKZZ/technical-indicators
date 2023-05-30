import pandas as pd
import matplotlib.pyplot as plt





df = pd.read_csv('MOEX.SBER_SMAL_220501_230523 (2).csv', delimiter=',')


def Stock_RSI(): #Функция RSI-индикатора

    delta = df['<CLOSE>'].diff(1)
    delta.dropna(inplace=True)

    positive = delta.copy()
    negative = delta.copy()

    positive[positive < 0] = 0
    negative[negative > 0] = 0

    days = 14 # указываем интервал для подсчета среднего значения и убытка

    average_gain = positive.rolling(window=days).mean() # Средняя длина растущих свечек
    average_loss = abs(negative.rolling(window=days).mean()) # Средняя длина падающих свечек

    relative_strength = average_gain / average_loss # частное от среднего значения роста цены и среднего значения снижения цены за период переменной days (по желанию можно поменять, но самый актуальный вариант - 14)
    RSI = 100.0 - (100.0 / (1.0 + relative_strength)) #основная формула RSI

    combined = pd.DataFrame()
    combined['<CLOSE>'] = df['<CLOSE>']
    combined['RSI'] = RSI
    #Визуализируем
    plt.figure(figsize=(12, 8))
    ax1 = plt.subplot(211)
    ax1.plot(combined.index, combined['<CLOSE>'], color='lightgray')
    ax1.set_title("Adjusted Close Price", color='white')

    ax1.grid(True, color='#555555')
    ax1.set_axisbelow(True)
    ax1.set_facecolor('black')
    ax1.figure.set_facecolor('#121212')
    ax1.tick_params(axis='x', colors = 'white')
    ax1.tick_params(axis='y', colors = 'white')

    ax2 = plt.subplot(212, sharex=ax1)
    ax2.plot(combined.index, combined['RSI'], color='lightgray')
    #Закоментированные строки - RSI-индикаторы с другими показателями (показатель указан в начале скобок)
    #ax2.axhline(0, linestyle='--', alpha = 0.5, color = '#ff0000')
    #ax2.axhline(10, linestyle='--', alpha=0.5, color='#ffaa00')
    #ax2.axhline(20, linestyle='--', alpha=0.5, color='#00ff00')
    ax2.axhline(30, linestyle='--', alpha=0.5, color='#cccccc')
    ax2.axhline(70, linestyle='--', alpha=0.5, color='#cccccc')
    #ax2.axhline(80, linestyle='--', alpha=0.5, color='#00ff00')
    #ax2.axhline(90, linestyle='--', alpha=0.5, color='#ffaa00')
    #ax2.axhline(100, linestyle='--', alpha=0.5, color='#ff0000')

    ax2.set_title("RSI Value")
    ax2.grid(False)
    ax2.set_axisbelow(True)
    ax2.set_facecolor('black')
    ax2.tick_params(axis='x', colors='white')
    ax2.tick_params(axis='y', colors='white')
    plt.show()

Stock_RSI()