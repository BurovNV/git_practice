def say_hello(name):
    print(f'hello {name}!')


def what_time():
    import time
    print(time.time())


if __name__ == '__main__':
    for i in range(3):
        say_hello('bob')
