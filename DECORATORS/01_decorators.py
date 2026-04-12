# timing fn execution
import time

def timer(fn):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=fn(*args, **kwargs)
        end=time.time()
        print(f"{fn.__name__} ran in {end-start} time ")
        return result
    return wrapper

@timer
def ex_fn(n):
    time.sleep(n)
ex_fn(2)
