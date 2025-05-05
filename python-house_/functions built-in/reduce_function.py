"""
 A função reduce() em Python é usada para reduzir uma sequência de valores a um único valor, aplicando repetidamente uma função de dois argumentos
"""
from functools import reduce

numbers = [47, 11, 42, 13]

def sum(a,b):
    return a + b

print(reduce(sum,numbers))