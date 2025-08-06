from models import PowInput, FibInput, FactInput

def calculate_pow(data: PowInput) -> int:
    return data.base ** data.exponent

def calculate_fib(data: FibInput) -> int:
    a, b = 0, 1
    for _ in range(data.n):
        a, b = b, a + b
    return a

def calculate_fact(data: FactInput) -> int:
    result = 1
    for i in range(2, data.n + 1):
        result *= i
    return result
