import random

PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Hey {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")     # "r" inside of formating prints in a beautiful way an string
    return greeter_func(name)

print(PLUGINS)
randomly_greet("nicolas")
print("printing globals")
globals()
