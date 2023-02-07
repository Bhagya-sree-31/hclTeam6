def demo():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
    yield 'E'
x=demo()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
n=(x*x for x in range(10000))
print(n)
n=[i for i in range(10000)]
print(n)