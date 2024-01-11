def gen():
    import random
    while True:
        yield random.randint(0, 100)


if __name__ == '__main__':
    g = gen()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print("it's OK!")
