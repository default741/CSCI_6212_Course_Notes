import math
import random
import timeit
from matplotlib import pyplot as plt
import numpy as np
from typing import Iterable
import pandas as pd

from tqdm import tqdm

np.random.seed(42)


def maximum_value_limited_neighbors(input_list: Iterable[int], k: int = 1) -> int:
    """Given a List of numbers, Finds the maximum value achievable with only k adjecent 1s.

    Args:
        input_list (Iterable[int]): Input List with integers
        k (int, optional): Atmost adjecent 1s. Defaults to 1.

    Returns:
        int: Maximum Value.
    """

    MVLN = np.zeros((k + 1, len(input_list)))
    b = [0] * len(input_list)
    b_list = []
    b_dict = {}

    print(b_list)

    MVLN[0][0] = input_list[0]

    b[input_list.index(MVLN[0][0])] = 1
    b_list.append(b)

    MVLN[0][1] = max(input_list[1], MVLN[0][0])

    b = [0] * len(input_list)

    b[input_list.index(MVLN[0][1])] = 1
    b_list.append(b)
    # b_dict[0] = b_list

    # Base Case for k = 0
    for i in range(2, len(input_list)):
        b = [0] * len(input_list)

        MVLN[0][i] = max(MVLN[0][i-1], MVLN[0][i-2] + input_list[i])

        if MVLN[0][i-1] > MVLN[0][i-2] + input_list[i]:
            b_list.append(b_list[-1])

        else:
            b[i - 2] = 1
            b[i] = 1
            b_list.append(b)

    b_dict[0] = b_list

    # For k >= 1
    for j in range(k):
        b_list = []
        b = [0] * len(input_list)

        MVLN[j + 1][0] = input_list[0]

        b[0] = 1
        b_list.append(b)

        MVLN[j + 1][1] = input_list[1] + input_list[0]

        b = [0] * len(input_list)

        b[0] = 1
        b[1] = 1

        b_list.append(b)
        b_dict[j + 1] = b_list

    for j in range(1, k + 1):
        b_list = []

        for i in range(2, len(input_list)):
            MVLN[j][i] = max(MVLN[j][i - 1], MVLN[j - 1][i - 1] +
                             input_list[i], MVLN[j][i - 2] + input_list[i])

            if MVLN[j][i - 1] > MVLN[j - 1][i - 1] + input_list[i] and MVLN[j][i - 1] > MVLN[j][i - 2] + input_list[i]:
                b_list.append(b_dict[j][i - 1].copy())

            elif MVLN[j - 1][i - 1] + input_list[i] > MVLN[j][i - 1] and MVLN[j - 1][i - 1] + input_list[i] > MVLN[j][i - 2] + input_list[i]:
                b = b_dict[j - 1][i - 1].copy()
                b[i] = 1
                b_list.append(b)

            else:
                b = b_dict[j][i - 2].copy()
                b[i] = 1
                b_list.append(b)

            b_dict[j].extend(b_list)

    print(b_dict[k])

    final_b = b_dict[k][-(k+1)]
    some_b_list = b_dict[k][-(k):]
    for i in range(k):
        final_b = np.logical_or(final_b, some_b_list[i])

    print(final_b)

    return MVLN[-1][-1]


if __name__ == '__main__':
    n_list = [1]  # list(map(lambda x: int(x), range(100, 5000, 200)))
    time_list, k_list = [], []

    for n in tqdm(n_list):
        print(f'Running for n={n}')

        # np.random.randint(low=0, high=1000, size=n).tolist()
        input_list = [10, 100, 300, 400, 50, 4500, 200, 30, 90]
        k = 2  # random.randint(1, math.isqrt(n))

        start_time = timeit.default_timer()
        max_value = maximum_value_limited_neighbors(input_list=input_list, k=k)
        end_time = timeit.default_timer()

        print(
            f'The Maximum Value for n = {len(input_list)} with atmost {k} adjecent 1s is: {max_value}')

        time_list.append((end_time - start_time))
        k_list.append(k)

        print(f'Running time - {time_list[-1]} Seconds')

    pd.DataFrame({'n_list': n_list, 'k_list': k_list, 'time': time_list}).to_csv(
        './experimental_time_list.csv', index=False)

    plt.xlabel('n')
    plt.ylabel('Execution Time')
    plt.plot(n_list, time_list)
    plt.show()
