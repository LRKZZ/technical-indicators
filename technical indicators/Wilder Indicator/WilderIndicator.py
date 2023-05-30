import numpy as np

def Wilder(data, periods):
    start = np.where(~np.isnan(data))[0][0]
    Wilder = np.array([np.nan] * len(data))
    Wilder[start + periods - 1] = data[start:(start + periods)].mean()
    for i in range(start + periods, len(data)):
        Wilder[i] = (Wilder[i - 1] * (periods - 1) + data[i]) / periods
    return (Wilder)
