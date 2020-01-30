def largest_palindrom(digit_number: int):
    max_result = 1
    lower_limit = 10 ** (digit_number - 1)
    high_limit = 10 ** digit_number
    for i in range(lower_limit, high_limit):
        for j in range(lower_limit, i + 1):
            if i * j > max_result:
                if is_palindrom(i * j):
                    max_result = i * j
    return max_result


def is_palindrom(n):
    string_number = str(n)
    for i in range(len(string_number) // 2):
        if string_number[i] != string_number[-i - 1]:
            return False
    return True
