def sum_even_fibo(max_value: int):
    fibo = Fibonacci()
    fibo_sum = 0
    while fibo.value <= max_value:
        if fibo.is_even():
            fibo_sum += fibo.value
        fibo.next_step()
    return fibo_sum


class Fibonacci:
    step = 0
    value = 1
    before = 1

    def next_step(self):
        self.step += 1
        stock = self.value
        self.value = self.before + self.value
        self.before = stock

    def is_even(self):
        return self.value % 2 == 0
