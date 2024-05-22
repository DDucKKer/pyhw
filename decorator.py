from typing import Callable


def foo():
    """printed"""
    print(23)


def decorate_as_string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = str(result)
        return result

    return wrapper


@decorate_as_string
def add(a, b):
    return a + b


@decorate_as_string
def greet(name):
    return f"Hello, {name}!"


result1 = add(10, 5)
print(result1)
result2 = greet("Alice")
print(result2)


def decorate_as_float(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(*args)
        print(kwargs)
        result = func(*args, **kwargs)
        result = float(result)
        return f'result = {result}'

    return wrapper


@decorate_as_float
def mul_two(value1: int, value2: int) -> int:
    return value1 * value2


@decorate_as_float
def conv_to_int(value: str) -> int:
    if value.isdigit():
        return int(value)
    return 0

# res = mul_two(5, 10)
# print(res)
# res = conv_to_int('5')
# print(res)
