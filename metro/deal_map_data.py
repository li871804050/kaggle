import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

def read_map(path):
    data = pd.read_csv(path)
    np_data = np.asarray(data)[:, 1:]
    x = []
    y = []
    for i in range(len(np_data)):
        for j in range(i, len(np_data[0])):
            if np_data[i][j] == 1 and i != j:
                x.append(i)
                y.append(j)
    plot.figure(figsize=(16, 16))
    new_ticks = np.linspace(0, 80, 81)
    plot.xticks(new_ticks)
    plot.yticks(new_ticks)

    plot.scatter(x, y)
    plot.savefig('1.png')
    plot.show()
    print(x, y)

if __name__ == '__main__':
    path = 'data/Metro_roadMap.csv'
    read_map(path)