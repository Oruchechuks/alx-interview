#!/usr/bin/python3


"""
    The letter H is the only character in a text file.
    There are only two operations that your text editor can do on 
	this file: Copy All and Paste. Write a method that calculates 
	given a number n.
    the least amount of processes necessary to produce exactly 
	n H characters in the file.
"""


def minOperations(n):
    if n == 1:
        return 0

    min_ops = float('inf')
    for d in range(2, n+1):
        if n % d == 0:
            ops = d + minOperations(n // d)
            min_ops = min(min_ops, ops)

    return min_ops

