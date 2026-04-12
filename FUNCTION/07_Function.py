# fn that takes variable num of argument and return their sum
def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4))
print(sum_all(1,23))