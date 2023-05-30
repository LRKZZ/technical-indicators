
import pandas as pd
import matplotlib.pyplot as plt

n = 50
def BBANDS(data, window=n):
    MA = data.CLOSE.rolling(window=n).mean()
    SD = data.CLOSE.rolling(window=n).std()
    data['UpperBB'] = MA + (2 * SD)
    data['LowerBB'] = MA - (2 * SD)
    return data


data = pd.read_csv('changed_close.csv', delimiter=',')
data = pd.DataFrame(data)


NIFTY_BBANDS = BBANDS(data, n)
print(NIFTY_BBANDS)

pd.concat([NIFTY_BBANDS.CLOSE, NIFTY_BBANDS.UpperBB, NIFTY_BBANDS.LowerBB], axis=1).plot(figsize=(9, 5), grid=True)
plt.show()