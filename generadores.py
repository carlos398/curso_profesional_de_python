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


#generator expresion
mylist = [0,1,2,3,4,5,6]
my_second_gen = (x*2 for x in mylist)