def square(func):
    def inner(x):
        return func(x) ** 2
    return inner

@square
def dbl(x):
    return x * 2


print(dbl(10)) # 10 * 2 ** 2
