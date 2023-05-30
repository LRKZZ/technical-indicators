import matplotlib.pyplot as plt
import pandas as pd


def EVM(data, ndays):
    dm = ((data['<HIGH>'] + data['<LOW>']) / 2) - ((data['<HIGH>'].shift(1) + data['<LOW>'].shift(1)) / 2)
    br = (data['<VOL>'] / 100000000) / ((data['<HIGH>'] - data['<LOW>']))
    EVM = dm / br
    EVM_MA = pd.Series(EVM.rolling(ndays).mean(), name='EVM')
    data = data.join(EVM_MA)
    return data


data = pd.read_csv('MOEX.SBER_SMAL_220501_230523 (2).csv', delimiter=',')
data = pd.DataFrame(data)

n = 14
SMTH_EVM = EVM(data, n)
EVM = SMTH_EVM['EVM']

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(2, 1, 1)
ax.set_xticklabels([])
plt.plot(data['<CLOSE>'], lw=1)
plt.title('Price Chart')
plt.ylabel('Close Price')
plt.grid(True)
bx = fig.add_subplot(2, 1, 2)
plt.plot(EVM, 'k', lw=0.75, linestyle='-', label='EVM(14)')
plt.legend(loc=2, prop={'size': 9})
plt.ylabel('EVM values')
plt.grid(True)
plt.setp(plt.gca().get_xticklabels(), rotation=30)
plt.show()
