
import matplotlib.pyplot as plt
import pandas as pd


def CCI(data, ndays): 
    TP = (data['<HIGH>'] + data['<LOW>'] + data['<CLOSE>']) / 3
    CCI = pd.Series((TP - TP.rolling(ndays).mean()) / (0.015 * TP.rolling(ndays).std()),
                    name = 'CCI') 
    data = data.join(CCI) 
    return data


data = pd.read_csv('MOEX.SBER_SMAL_220501_230523 (2).csv', delimiter=',')
data = pd.DataFrame(data)


n = 20
NIFTY_CCI = CCI(data, n)
CCI = NIFTY_CCI['CCI']


fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(2, 1, 1)
ax.set_xticklabels([])
plt.plot(data['<CLOSE>'],lw=1)
plt.title('NSE Price Chart')
plt.ylabel('Close Price')
plt.grid(True)
bx = fig.add_subplot(2, 1, 2)
plt.plot(CCI,'k',lw=0.75,linestyle='-',label='CCI')
plt.legend(loc=2,prop={'size':9.5})
plt.ylabel('CCI values')
plt.grid(True)
plt.setp(plt.gca().get_xticklabels(), rotation=30)
plt.show()