import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r}, iterating {args[0]} in {run_time:.4f} secs")
        return value

    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])
        

a = waste_some_time(1)
b = waste_some_time(10)
c = waste_some_time(100)
