def result(n):
    sum = 0
    for num in range(1, n):
        if num % 5 == 0 or num % 3 == 0:
            sum += num
    return sum
