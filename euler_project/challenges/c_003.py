from math import floor, sqrt


def largest_prime_number(n):
    for i in reversed(range(2, floor(sqrt(n)))):
        if n % i == 0:
            if is_prime(i):
                return i


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
