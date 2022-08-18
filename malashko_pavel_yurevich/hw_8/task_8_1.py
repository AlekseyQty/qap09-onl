def typed(type):
    def decorator(func):
        def wrapper(elements):
            if type == 'str':
                sum_symbols = ''
                for elem in func(elements):
                    sum_symbols += str(elem)
                print(sum_symbols)
            if type == 'int':
                sum_symbols = 0
                for elem in func(elements):
                    sum_symbols += int(elem)
                print(sum_symbols)
            if type == 'float':
                sum_symbols = 0
                for elem in func(elements):
                    sum_symbols += float(elem)
                print(sum_symbols)

        return wrapper
    return decorator


@typed(type='str')
def add_symbols(elements):
    return elements


add_symbols(["5", '4', 4, 0.1])
add_symbols(['40', 5, 6, 0.01])