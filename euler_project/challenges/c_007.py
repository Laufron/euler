def prime(n):
    prime_calc = PrimeCalculator()
    if n == 1:
        return prime_calc.prime_number
    else:
        prime_calc.go_to_step(n)
        return prime_calc.prime_number


class PrimeCalculator:
    index = 1
    prime_number = 2

    def next_step(self):
        self.index += 1
        self.prime_number = compute_next_prime(self.prime_number)

    def go_to_step(self, n):
        for i in range(n - 1):
            self.next_step()


def compute_next_prime(p):
    if p == 2:
        return 3
    else:
        while True:
            p += 2
            if is_prime(p):
                return p


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
