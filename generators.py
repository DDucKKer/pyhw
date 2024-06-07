# data = [5, 8, 8]
# set_data = {item for item in data}
# print(set_data)
#
# list_data = [item * 2 for item in data]
# print(list_data)
#
# dict_data = {item: item for item in data}
# print(dict_data)
#
# generator_data = (item for item in data)
# print(generator_data)

def our_generator():
    print(1111111111111)
    yield 55
    print(1111111111111)
    yield 54
    print(1111111111111)
    yield 52


generated_obj = our_generator()

print(next(generated_obj))
print(next(generated_obj))
print(next(generated_obj))
