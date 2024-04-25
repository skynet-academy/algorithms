import functools

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("creating greeting")
    return f"Hi {name}"

def do_twice1(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice1
def return_greeting1(name):
    print("creating greeting1")
    return f"Hi {name}"



hello = return_greeting('nicolas')
hello1 = return_greeting1('nicolas1')
print(hello)
print(hello1)
