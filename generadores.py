#funciones que guardan un estado

def my_gen():

    """ejemplo de generadores"""

    print('hello world')
    n = 0
    yield n

    print('hello heaven')
    n = 1
    yield n

    print('hello heaven')
    n = 2
    yield n


a = my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a)) 