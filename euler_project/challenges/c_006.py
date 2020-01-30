def square_differences(n):
    result = 0
    for i in range(n + 1):
        for j in range(i + 1):
            if j != i:
                result += i * j
    return 2 * result
