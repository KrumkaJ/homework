from math import factorial


def factorial_numb():
    n = 0
    while n < 10:
        factorial(n)
        n += 1
        yield factorial(n)


fact = factorial_numb()

for el in fact:
    print(el)
