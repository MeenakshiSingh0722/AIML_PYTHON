name="meeshi"
def func():
    name="phugga"
    print(name)
print(name)
func()

x=99
def fun(y):
    z=x+y
    return z
print(fun(3))

# global var ko change
x=99
def func():
    global x
    x=12
func()
print(x)