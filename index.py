class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count  # Maximum numbers to generate
        self.index = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.max_count:
            raise StopIteration

        if self.index == 0:
            self.index += 1
            return 0
        elif self.index == 1:
            self.index += 1
            return 1
        else:
            next_value = self.a + self.b
            self.a, self.b = self.b, next_value
            self.index += 1
            return next_value


# Example usage:
fib_iter = FibonacciIterator(10)  # Generate first 10 Fibonacci numbers
for num in fib_iter:
    print(num)
