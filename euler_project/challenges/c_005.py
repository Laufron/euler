def smallest_evenly_divisible(divide_until):
    i = divide_until
    while True:
        print(i)
        if is_evenly_divisible(i, divide_until):
            return i
        else:
            i += divide_until


def is_evenly_divisible(number, divide_until):
    for i in range(1, divide_until + 1):
        if number % i != 0:
            return False
    return True
