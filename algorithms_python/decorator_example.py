import functools 

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwgars):
        print(f"this is my value {args}{kwgars}")
        value = func(*args, **kwgars)
        value += ' adding text'
        return value
    return wrapper_decorator

@decorator
def operation(value):
    return f'this is the value {value}'

a = operation(100)
print(a)

