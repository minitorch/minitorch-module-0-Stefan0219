"""Collection of the core mathematical operators used throughout the code base."""

import math
from functools import reduce

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(x: float, y: float) -> float:
    return x * y

def id(x: float) -> float:
    return x

def add(x: float, y: float)-> float:
    return x + y

def neg(x: float) -> float:
    return -x

def lt(x: float, y: float) -> bool:
    return  x < y

def eq(x: float, y: float) -> bool:
    return  x == y

def max(x: float, y: float) -> float:
    return  x if x >= y else y

def is_close(x: float, y: float) -> float:
    return  abs(x - y) < 1e-2

def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))

def relu(x: float) -> float:
    return  0.0 if x < 0.0 else x

def log(x: float) -> float:
    return math.log(x + 1e-6)

def exp(x: float) -> float:
    return math.exp(x)

def inv(x: float) -> float:
    return 1.0 / x

def log_back(x: float, y: float) -> float:
    return inv(x) * y

def inv_back(x: float, y: float) -> float:
    t = inv(x)
    return - t * t * y

def relu_back(x: float, y: float) -> float:
    return y if x > 0.0 else 0.0
# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def map(fn, lst) -> list:
    ret = []
    for l in lst:
        ret.append(fn(l))
    return ret

def reduce(fn, lst:list):
    start = fn(lst[0], lst[1])
    for i in range(2 , len(lst)):
        start = fn(start, lst[i])
    return start

def zipWith(fn, l1:list, l2:list) -> list:
    assert len(l1) == len(l2)
    ret = []

    for i in range(len(l1)) :
        ret.append(fn(l1[i], l2[i]))
    return ret






def negList(x: list[float]) -> list[float]:
    return map(neg, x)

def addLists(x: list[float], y: list[float]) -> list[float]:
    return zipWith(add, x, y)


def sum(x: list[float]) -> float:
    if len(x) == 0:
        return 0
    if len(x) == 1:
        return x[0]
    return reduce(add, x)

def prod(x: list[float]) -> float:
    return reduce(mul, x)



