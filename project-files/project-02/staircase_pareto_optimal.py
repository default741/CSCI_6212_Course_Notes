import random
import timeit

import matplotlib.pyplot as plt
import pandas as pd

from tqdm import tqdm


class Point:
    '''Creates a Point in 2D Plane with x-coordinate and y-coordinate

    Methods:
        __init__: Initializes the x and y coordinate of a Point
        __str__: Returns a String conversion of a Point
        __rept__: Returns a String Representation of a Point
        __iter__: Returns a Iterable object
    '''

    def __init__(self, x: int, y: int) -> None:
        """Initializes the X and Y Coordinate of a Point

        Args:
            x (int): X-Coordinate
            y (int): Y-Coordinate
        """

        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Returns a String conversion of a Point

        Returns:
            str: String of Point(x, y)
        """
        return f'Point({self.x}, {self.y})'

    def __repr__(self) -> str:
        """Returns a String Representation of a Point

        Returns:
            str: String of Point(x, y)
        """
        return f'Point({self.x}, {self.y})'

    def __iter__(self) -> iter:
        """Returns a Iterable object

        Returns:
            iter: Iterable(x, y)
        """
        return iter((self.x, self.y))


class ParetoOptimalStaircase:

    @staticmethod
    def plot_staircase(points: list[Point]) -> None:
        """Plots the staircare of pareto-optimal points

        Args:
            points (list[Point]): List of Points to plot
        """

        x, y = zip(*points)

        plt.scatter(x, y, color='blue')
        plt.step(x, y, where='post', color='red')

        plt.xlabel('X')
        plt.ylabel('Y')

        plt.title('Pareto Optimal Staircase')
        plt.show()

    @staticmethod
    def merge_staircases(left_staircase: list[Point], right_staircase: list[Point]) -> list[Point]:
        """Merges the two Staircase in a merge sort fashion but based on the y-coordinate.

        Args:
            left_staircase (list[Point]): Left Half Optimal Staircase
            right_staircase (list[Point]): Right Half Optimal Staircase

        Returns:
            list[Point]: Pareto-Optimal Points (Appended with Non-Pareto Optimal Points)
        """

        merged_staircase = []
        idx_i = idx_j = 0

        while idx_i < len(left_staircase) and idx_j < len(right_staircase):
            left_point = left_staircase[idx_i]
            right_point = right_staircase[idx_j]

            if left_point.y >= right_point.y:
                merged_staircase.append(left_point)
                idx_i += 1

            else:
                merged_staircase.append(right_point)
                idx_j += 1

        merged_staircase.extend(left_staircase[idx_i:])
        merged_staircase.extend(right_staircase[idx_j:])

        return merged_staircase

    @staticmethod
    def compute_staircase(P: list[Point]) -> list[Point]:
        """Computes the Pareto Optimal Staircase in a divide and conquer fashion.

        Args:
            P (list[Point]): List of Points

        Returns:
            list[Point]: List of Pareto-Optimal Points
        """

        if len(P) <= 1:
            return P

        mid = len(P) // 2
        left_half = P[:mid]
        right_half = P[mid:]

        left_staircase = ParetoOptimalStaircase.compute_staircase(left_half)
        right_staircase = ParetoOptimalStaircase.compute_staircase(right_half)

        return ParetoOptimalStaircase.merge_staircases(left_staircase, right_staircase)


if __name__ == '__main__':

    n_list = list(
        map(lambda x: int(x), [1E1 // 4, 1E1 // 2, 3 * 1E1 // 4, 1E1, 1E2 // 4, 1E2 // 2, 3 * 1E2 // 4, 1E2, 1E3 // 4, 1E3 // 2,
                               3 * 1E3 // 4, 1E3, 1E4 // 4, 1E4 // 2, 3 * 1E4 // 4, 1E4, 1E5 // 4, 1E5 // 2, 3 * 1E5 // 4, 1E5]))
    time_list = []

    for n in tqdm(n_list):
        print(f'Running for n={n}')

        points = [Point(random.randint(0, n), random.randint(0, n))
                  for _ in range(n)]

        points.sort(key=lambda point: (-point.x, -point.y))

        start_time = timeit.default_timer()
        staircase = ParetoOptimalStaircase.compute_staircase(points)
        end_time = timeit.default_timer()

        # Code Snippet to filter only the Pareto Optimal Points appended with non-pareto-optimal points
        idx = 1

        while idx < len(staircase):
            if not staircase[idx - 1].x > staircase[idx].x:
                idx += 1
            break

        staircase = staircase[:idx]
        time_list.append((end_time - start_time))

        print(f'Running time - {time_list[-1]} Units')

    pd.DataFrame({'n_list': n_list, 'time': time_list}).to_csv(
        './experimental_time_list.csv', index=False)

    plt.xlabel('n')
    plt.ylabel('Execution Time')
    plt.plot(n_list, time_list)
    plt.show()
