from datetime import date, datetime

# def mayusculas(func):
#     def envoltura(texto):
#         return func(texto).upper()
#     return envoltura

# @mayusculas
# def mensaje(nombre):
#     return f'{nombre}, recibiste un mensaje'

# print(mensaje('cesar'))


#ejercicio decoradores:

def execution_time(func):
    def wrapper(*args, **kwargs): #recibe toda la cantidad de argunmentos necesarios de lo contrario no funcionaria
        initial_time = datetime.now()
        func(*args, **kwargs) #recibe toda la cantidad de argunmentos necesarios
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('pasaron {time} segundos'.format(
            time=time_elapsed.total_seconds()
        ))
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    suma(5,5)