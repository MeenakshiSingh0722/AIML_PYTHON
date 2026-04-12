# cache return values
import time
def cache(fn):
    cache_value={}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = fn(*args)
        cache_value[args]=result
        return result
    return wrapper

@cache
def long_running_fn(a,b):
    time.sleep(4)
    return a+b

print(long_running_fn(2,3))
print(long_running_fn(2,3))
