#!/usr/bin/python3
""" Minimum Operations function """
import math


def minOperations(n):
    """Calculates the minimum number of operations"""
    prime_factors = []
    minOp = 0

    if n < 2 or type(n) != int:
        return 0

    while n % 2 == 0:
        prime_factors.append(2)
        n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n /= i

    if n > 2:
        prime_factors.append(n)

    for i in range(len(prime_factors)):
        minOp += prime_factors[i]

    return int(minOp)