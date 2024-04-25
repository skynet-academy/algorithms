import functools
import time

def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwgars):
        time.sleep(1)
        return func(*args, **kwgars)

    return wrapper_slow_down

@slow_down
def countdowwn(from_number):
    if(from_number < 1):
        print("Liftoff!")
    else:
        print(from_number)
        countdowwn(from_number - 1)

countdowwn(4)

