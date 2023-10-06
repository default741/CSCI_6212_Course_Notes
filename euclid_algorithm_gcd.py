# Basic Euclidean Algorithm for GCD:
# The algorithm is based on the below facts.

#   If we subtract a smaller number from a larger one (we reduce a larger number), GCD doesn’t change. So if we keep subtracting repeatedly the larger of two, we end up with GCD.
#   Now instead of subtraction, if we divide the smaller number, the algorithm stops when we find the remainder 0.

#   Time Complexity: O(Log min(a, b))
#   Auxiliary Space: O(Log (min(a,b))

# Extended Euclidean Algorithm:
#   Extended Euclidean algorithm also finds integer coefficients x and y such that: ax + by = gcd(a, b)
#   Remainder Formula - r = a - (a // b) * b

import random

class EuclidAlgorithm:

    @staticmethod
    def basic_euclid_algorithm_gcd(num1: int, num2: int) -> int:
        """Returns the GCD of two numbers using the basic euclid algorithm.

        Args:
            num1 (int): Larger of the two numbers.
            num2 (int): Smaller of the two numbers.

        Returns:
            int: GCD (or Remainer) or the two numbers
        """

        if num2 == 0:
            return num1

        remainder = num1 % num2

        return EuclidAlgorithm.basic_euclid_algorithm_gcd(num1=num2, num2=remainder)

    @staticmethod
    def extended_euclid_algorithm_gcd(num1: int, num2: int) -> tuple:
        """Returns the GCD of two numbers using the basic euclid algorithm as well as the coefficients x, y such that ax + by = gcd(a, b).

        Args:
            num1 (int): Larger of the two numbers.
            num2 (int): Smaller of the two numbers.

        Returns:
            tuple: GCD (or Remainer) or the two numbers, x-coefficient, y-coefficient
        """

        if num2 == 0:
            return num1, 1, 0

        gcd, x_coef, y_coef = EuclidAlgorithm.extended_euclid_algorithm_gcd(num1=num2, num2=(num1 % num2))

        x_final = y_coef
        y_final = x_coef - (num1 // num2) * y_coef

        return gcd, x_final, y_final



if __name__ == '__main__':
    num1 = random.randint(1000, 5000)
    num2 = random.randint(0, 999)

    basic_gcd = EuclidAlgorithm.basic_euclid_algorithm_gcd(num1=num1, num2=num2)
    gcd, x, y = EuclidAlgorithm.extended_euclid_algorithm_gcd(num1=num1, num2=num2)

    print(f'The GCD of {num1} and {num2} is {basic_gcd}')
    print(f'The x and y coefficients of {num1} and {num2} such that {num1} * {x} + {num2} * {y} = {basic_gcd}')
