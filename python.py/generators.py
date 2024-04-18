def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
x = my_generator()
print(next(x))
print(next(x))
print(next(x))
print(next(x))