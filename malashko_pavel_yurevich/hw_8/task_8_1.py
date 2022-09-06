def typed(type):
    def decorator(func):
        def wrapper(*args):
            if type == 'str':
                new_args = tuple(map(str, args))
                print(func(*new_args))
            elif type == 'int':
                new_args = tuple(map(int, args))
                print(func(*new_args))

            elif type == 'float':
                new_args = tuple(map(float, args))
                print(func(*new_args))
        return wrapper
    return decorator


@typed(type='int')
def add_two_symbols(a, b):
    return a + b


@typed(type='str')
def add_three_symbols(a, b, c):
    return a + b + c


add_two_symbols(5, 6)
add_two_symbols('4', '3')
add_three_symbols('4', 5, 10.3)
