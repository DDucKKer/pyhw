our_list = [5, '8', 18] * 10

res_list = []
for item in our_list:
    res_list.append(item * 3)


def mult_3(item):
    return item * 3


another_list = map(mult_3, our_list)

print(another_list)
print(list(another_list))

list_2 = [1, 2, 3, 4, 5] * 5
another_list_2 = map(lambda item: item * 10, list_2)


# print(next(another_list_2))
def more3(item):
    return item > 3


clean_data = filter(more3, list_2)
print(list(clean_data))

super_data = map(mult_3, filter(more3, list_2))
print(list(super_data))