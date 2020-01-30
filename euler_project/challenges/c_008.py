import numpy


def highest_product(number_of_terms):
    max_product = 1
    number_reader = LongNumberReader(number_of_terms)
    if not number_reader.long_number_too_short:
        while not number_reader.end_of_file:
            product = numpy.prod(number_reader.numbers)
            if product > max_product:
                max_product = product
            number_reader.next_numbers()
        return max_product
    return "File too short"


class LongNumberReader:
    _f = open("euler_project/files/c_008/long_number.txt")
    end_of_file = False
    long_number_too_short = False

    def __init__(self, number_of_terms):
        self.number_of_terms = number_of_terms
        self.numbers = []
        for i in range(number_of_terms):
            next_number = self.next_number()
            if self.end_of_file:
                self.long_number_too_short = True
                break
            else:
                self.numbers.append(next_number)

    def next_numbers(self):
        next_number = self.next_number()
        if not self.end_of_file:
            result = [self.numbers[i] for i in range(1, self.number_of_terms)]
            result.append(next_number)
            self.numbers = result

    def next_number(self):
        if not self.end_of_file:
            char = self._f.read(1)
            if char == "":
                self.end_of_file = True
                return "EOF"
            elif char == "\n":
                return self.next_number()
            else:
                return int(char)
        else:
            return "EOF"
