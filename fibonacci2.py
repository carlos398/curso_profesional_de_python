import time

def fibo_gen():
    n1, n2, counter = 0, 1, 0

    while True:
        if counter == 0:
            counter +=1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter +=1
            yield aux
