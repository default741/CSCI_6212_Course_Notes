import math
import random
import timeit
from matplotlib import pyplot as plt
import numpy as np
from typing import Iterable
import pandas as pd

from tqdm import tqdm

np.random.seed(42)

# return the highest idx on maximum
def get_highest_max_ind(lis):
    m = max(lis)
    ind = [i for i in range(len(lis)) if lis[i]==m]
    return ind[-1]


def maximum_value_limited_neighbors(input_list: Iterable[int], k: int = 1) -> int:

    """Given a List of numbers, Finds the maximum value achievable with only k adjecent 1s.

    Args:
        input_list (Iterable[int]): Input List with integers
        k (int, optional): Atmost adjecent 1s. Defaults to 1.

    Returns:
        int: Maximum Value.
    """

    MVLN = np.zeros((k + 1, len(input_list)))

    MVLN[0][0] = input_list[0]
    MVLN[0][1] = max(input_list[1], MVLN[0][0])
    
    # for backtracking the input_listay for base case solution
    prev = [0]*len(input_list)
    curr = [0]*len(input_list)
    
    
    # b_track input_listay for all values for one k and for each position 
    b_track = []

    # base case for k = 0 and first two elements which is maximum
    base_0_1 = [input_list[1], MVLN[0][0]]
    MVLN[0][1] = max(base_0_1)

    # max index
    ind = base_0_1.index(max(base_0_1))

    # updating the prev and curr prev is for b input_listay for n-1 elements and curr is including n elements
    if(ind == 0):
        prev[0] = 1
        curr[1] = 1
    else:
        prev[1] = 1
        curr[0] = 1
    
    # appending to b_track to use it for next k 
    b_track.append([0]*len(input_list))

    b_track[0][0] = 1
    b_track.append(curr)

    



    # Base Case for k = 0
    for i in range(2, len(input_list)):

        # checking whether max value for element i is same as i-1 excluding i or sum till i-2 inclucing i
        chk = [MVLN[0][i-1], MVLN[0][i-2] + input_list[i]]
        MVLN[0][i] = max(chk)

        # index of the maximum of the two max values if two are having same numbers
        ind = get_highest_max_ind(chk)

        if(ind == 0):
            prev = curr.copy()
        else:
            prev,curr = curr, prev
            curr[i] = 1
        # appending for each input i the b input_listay
        b_track.append(curr)

    # b input_listay 
    b = np.zeros((k+1,len(input_list)))
    

    # For k >= 1
    for j in range(k):

        MVLN[j + 1][0] = input_list[0]
        MVLN[j + 1][1] = input_list[1] + input_list[0]
        b[j+1][0:2]    = [1,1]

    b[0] = curr
    
    for j in range(1, k + 1):

        # initializing the b_track_prev which is the b_track values for k-1 and we need that in updating the values of k
        b_track_prev = b_track.copy()
        b_track = []
        b_track.append([0]*len(input_list))

        # for k>=1 the values we can always include first two value to get the maximum if numbers are positive
        b_track[0][0:2] = [1,1]


        for i in range(2, len(input_list)):

            # three conditions
            chk = [MVLN[j][i - 1], MVLN[j - 1][i - 1] +
                             input_list[i], MVLN[j][i - 2] + input_list[i]]
            
            MVLN[j][i] = max(chk)

            # the b input_listay will be same as the 
            ind = get_highest_max_ind(chk)
            if(ind ==0):

                b[j][:i] = b[j][:i]
                b[j][i]  = 0

            elif(ind ==1):

                b[j][:i] = b_track_prev[i-1][:i]
                b[j][i]  = 1

            else:

                b[j][:i-1] = b[j][:i-1]
                b[j][i-1]  = 0
                b[j][i]    = 1
            b_track.append(b[j])

    return MVLN[-1][-1], b_track[-1]


if __name__ == '__main__':
    n_list = list(map(lambda x: int(x), range(100, 5000, 200)))
    time_list, k_list = [], []

    for n in tqdm(n_list):
        print(f'Running for n={n}')

        input_list = np.random.randint(low=0, high=1000, size=n).tolist()
        k = random.randint(1, math.isqrt(n))

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
