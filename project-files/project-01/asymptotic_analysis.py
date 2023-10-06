import math
import timeit
from tqdm import tqdm

import pandas as pd
import matplotlib.pyplot as plt


def analyse_time_complexity_manaaf(n: int) -> None:
    j = 2

    while j < n:
        k = 2

        while k < n:
            k = k * math.sqrt(k)

        j += j / 2


def analyse_time_complexity_gehna(n: int) -> None:
    j = 2

    while (j < n):
        k = j

        while (k < n):
            k = k * k

        j += math.log(k, 2)


if __name__ == '__main__':
    n_list = list(map(lambda x: int(x), [1E1, 1E3, 1E5, 1E7, 1E9, 1E11, 1E13, 1E15, 1E17, 1E19,
                  1E21, 1E23, 1E25, 1E27, 1E29, 1E31, 1E33, 1E35, 1E37, 1E39, 1E41, 1E43, 1E45, 1E47, 1E49]))
    time_list = []

    for n in tqdm(n_list):
        print(f'Running for n={n}')

        start_time = timeit.default_timer()
        analyse_time_complexity_manaaf(n=n)
        end_time = timeit.default_timer()

        time_list.append((end_time - start_time))

        print(f'Running time - {time_list[-1]} Units')

    pd.DataFrame({'time': time_list}).to_csv(
        './experimental_time_list.csv', index=False)

    plt.xlabel('n')
    plt.ylabel('Execution Time')
    plt.plot(n_list, time_list)
    plt.show()
