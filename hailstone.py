# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/17/2024
# Description: Define a function named hailstone that takes a positive integer
# parameter as the initial number of a hailstone sequence and returns how
# many steps it takes to reach 1.

def hailstone(seq):
    """
    A function that takes a positive integer parameter as the initial number in a
    hailstone sequence, and return how many steps it'll take to reach 1.
    :param seq: the number of operations (steps) it took to reduce the hailstone to 1
    :return: hailstone (int) = initial number in hailstone sequence + the steps to
    reach 1
    """
    if seq == 1:
        return 0
    steps = 0
    while seq != 1:
        if seq % 2 == 0:
            seq //= 2
        else:
            seq = 3 * seq + 1
        steps += 1
    return steps

# print(hailstone(10))
