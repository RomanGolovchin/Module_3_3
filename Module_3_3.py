def print_params(a=1, b='string', c=True):
    print(a, b, c)
values_list = [54.32, 'Строка', 43]
values_dict = {'a': 1984, 'b': 1982, 'c': 1988}
values_list_2 = [54.32, 'Строка']

print_params(1, 25, [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)


def print_params(**qwards):
    print(qwards)

values_dict = {'Max': 1984, 'Andrew': 1982, 'Sys': 1988}
print_params(**values_dict)

def print_params(**qwards):
    for key, value in qwards.items():
        print(key, value)


values_dict = {'Nax': 1984, 'Andrew': 1982, 'Sys': 1988}
print_params(**values_dict)


