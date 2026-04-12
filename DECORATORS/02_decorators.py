# # debugging fn calls
def debug(fn):
    def wrapper(*args, **kwargs):
        args_value='_ '.join(str(arg) for arg in args)
        kwargs_value='_ '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling : {fn.__name__} with args{args_value} and kwargs {kwargs_value}")
        return fn(*args, **kwargs)
    return wrapper


@debug
def hello():
    print("hello")

@debug
def greet(name,greeting="hello"):
    print(f"{greeting},{name}")

hello()
greet("chai",greeting="hanji")