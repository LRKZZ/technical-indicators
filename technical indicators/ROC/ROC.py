
import matplotlib.pyplot as plt
import pandas as pd


def ROC(data, n):
    N = data['<CLOSE>'].diff(n)
    D = data['<CLOSE>'].shift(n)
    ROC = pd.Series(N / D, name='Rate of Change')
    data = data.join(ROC)
    return data


data = pd.read_csv('MOEX.SBER_SMAL_220501_230523 (2).csv', delimiter=',')
data = pd.DataFrame(data)

n = 5
NIFTY_ROC = ROC(data, n)
ROC = NIFTY_ROC['Rate of Change']

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(2, 1, 1)
ax.set_xticklabels([])
plt.plot(data['<CLOSE>'], lw=1)
plt.title('Price Chart')
plt.ylabel('Close Price')
plt.grid(True)
bx = fig.add_subplot(2, 1, 2)
plt.plot(ROC, 'k', lw=0.75, linestyle='-', label='ROC')
plt.legend(loc=2, prop={'size': 9})
plt.ylabel('ROC values')
plt.grid(True)
plt.setp(plt.gca().get_xticklabels(), rotation=30)

plt.show()