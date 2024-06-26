import functools


def debug(func):
    """Print the function signature and return value """

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if(age is None):
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

make_greeting("Nicolas")
make_greeting("Rita",age=20)

