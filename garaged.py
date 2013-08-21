#!/usr/bin/env python
# -*- coding: utf8 -*-

def fib(n):
    """ Imprime una serie de Fibonacci hasta n"""
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


print "prueba de programa nuevo..."
print fib(10)
mi_lista = fib2(20)
print mi_lista
print "otra prueba de programa nuevo..."
