my_list = [1, "hello", 3.14, True, [5, 6, 7], {"name": "John", "age": 30}, 7, 8, 2]


def to_string(item):
    return str(item)


string_list = map(to_string, my_list)
print(list(string_list))


def return_ints(item):
    return type(item) == int


int_list = filter(return_ints, my_list)
print(list(int_list))
