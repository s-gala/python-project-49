import operator
import random
from random import randint


def get_random_number(begin, end):
    return randint(begin, end)


def get_random_operator():
    math_symbol = {'+': operator.add,
                   '-': operator.sub,
                   '*': operator.mul}
    sign = random.choice(list(math_symbol.keys()))
    operator_metod = math_symbol.get(sign)
    return sign, operator_metod
    