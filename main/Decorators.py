
def decorator(func):
    def wrapper():
        print("I am about to print hello before function... ")
        func()
        print("I just printed hello after function... ")
        func()
    return wrapper


def say_hello():
    print("hello from say_hello")

# say_hello()
f = decorator(say_hello)
f()