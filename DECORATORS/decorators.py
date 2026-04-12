# timing fn execution
import time
#
# def timer(fn):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         result=fn(*args, **kwargs)
#         end=time.time()
#         print(f"{fn.__name__} ran in {end-start} time ")
#         return result
#     return wrapper
#
# @timer
# def ex_fn(n):
#     time.sleep(n)
# ex_fn(2)

# # debugging fn calls
# def debug(fn):
#     def wrapper(*args, **kwargs):
#         args_value='_ '.join(str(arg) for arg in args)
#         kwargs_value='_ '.join(f"{k}={v}" for k, v in kwargs.items())
#         print(f"calling : {fn.__name__} with args{args_value} and kwargs {kwargs_value}")
#         return fn(*args, **kwargs)
#     return wrapper
#
# @debug
# def hello():
#     print("hello")
#
# @debug
# def greet(name,greeting="hello"):
#     print(f"{greeting},{name}")
#
# hello()
# greet("chai",greeting="hanji")

# cache return values
# def cache(fn):
#     cache_value={}
#     print(cache_value)
#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         result = fn(*args)
#         cache_value[args]=result
#         return result
#     return wrapper
#
# @cache
# def long_running_fn(a,b):
#     time.sleep(4)
#     return a+b
#
# print(long_running_fn(2,3))
# print(long_running_fn(2,3))
