import datetime
import functools

# file = open('my.txt', mode='a')
# file.write('adwwadawd\n')
# file.close()

# with open('my.txt', mode='a', encoding='utf-8') as file:
#     file.write('fffffffawdadwa')
# data = file.read()
# print(data)


def logger(file_name='log_data.csv'):
    def wrapper1(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, mode='a', encoding='utf-8') as file:
                file.write(f'{datetime.datetime.now()}; {func.__name__}; {result}\n')
            return result
        return wrapper
    return wrapper1


@logger()
def foo(arg):
    return arg * 2


foo(55)
