#cuenta Regresiva
def countdown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list
print(countdown(5)) 

#Imprimir y Devolver
def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]
imprimir_y_devolver([1, 2]) 

#Primero más longitud
def primero_mas_longitud(lista):
    return lista[0] + len(lista)
print(primero_mas_longitud([1, 2, 3, 4, 5])) 

#Valores mayores que el segundo
#Profe No la entiendo esta complicado el enunciado

#Esta longitud, ese valor
def tamano_and_valor(tamaño, valor):
    nueva_lista = [valor] * tamaño
    return nueva_lista
print(tamano_and_valor(4, 7)) 
print(tamano_and_valor(6, 2)) 