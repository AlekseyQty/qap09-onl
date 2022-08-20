from functools import wraps


def print_task_no(task_no):
    def decorator(func_to_decorate):
        @wraps(func_to_decorate)
        def wrapper(*args, **kwargs):
            print(f"{'-'*20}Start task {task_no}{'-'*20}")
            func_to_decorate(*args, **kwargs)
            print(f"{'-'*62}")
        return wrapper
    return decorator
