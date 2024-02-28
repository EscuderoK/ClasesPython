import numpy as np
import math

#El lado izquierdo de la variable se conoce como identificador, el simbolo en la mitad (=)
#se conoce como simbolo de asignacion y me asigna al espacio de memoria identificado con 
# el nombre de la variable el valor que  tiene a su derecha.

x = 10                   #

#Tenemos los tipos de datos, string,integer,float,boolean(True o False). Estos se conocen
# como tipo de datos primarios

nombre= 'Karol'                    #Es un string
edad = 25                          #Es un integer
estatura= 1.57                     #Es un float
es_vacunado = True                 #Es tipo bool

#Tipado dinamico , es decir python no verifica si las variables son del mismo tipo de dato

#Listas : Son contenedores que permiten almacenar varios objetos de diferentes tipos de datos

Lista= [1,'valor',3,False,4.6]

for value in Lista:
    print(value)

#Las listas son mutables

#Tuplas  : Son contenedores similares a las listas pero son imutables, es decir una vez creada
#no pueden ser alteradas
tupla=(1,'Valor',3,False,4.6)
print(tupla[0])

#Conjuntos Son contenedores que permiten almacenar objetos de diferentes tipos de datos, sin embargo solo permite tener
# valores únicos
conjuntos= {1,2,3,4}              

#Dada la lista_con_dup= [1,1,2,2,3,4,5,6,6,6] construir una lista con los valores sin duplicados, use list y set

lista_con_dup= [1,1,2,2,3,4,5,6,6,6]
lista= list(set(lista_con_dup)) 
print(lista)

#Diccionarios  :Son contenedores que permite almacenar pares de llave-valor
diccionario={"Nombre":"karol","Edad":23,"Estatura":1.57}

for key,value in diccionario.items():
    print (f"{key}:{value}")


#Sentencias de control de flujo 
if edad>=18:
    print("Eres mayor de edad")
elif edad<18 and edad>0:
    print ("Eres menor de edad")
else:
    print("La edad debe ser positiva")

#Funciones

def suma(num_1: float,num_2: float) ->float:
    """Suma dos numeros flotantes
    
    Args:
        num_1 (float): Primer numero
        num_2 (float): Segundo numero
    Returns:
        float: Resultado de la suma de los numeros anteriores
    """
    return num_1+num_2

print(suma(5.5,3.3))

#Ejercicio: Escribir una funcion que muestre por pantalla 'Hola Mundo'

def hola_mundo() -> None:
    print('Hola Mundo')

#Ejercicio Escribir una funcion que reciba el nombre de una personas y muestre  un mensaje con su nombre completo

def saludo(nombre:str) -> None:
    saludo=f"Hola {nombre}"
    print(saludo)
saludo('Karol')

#Ejercicio: Escribir una funcion que reciba un numero entero y devuelva su factorial, esta funcion si tiene retorno

def factorial(numero:int)-> int :
    """Esta funcion calcula  el factorial de un numero entero

    Args:
        numero (int): _Numero para tener factorial

    Returns:
        int: Valor del factorial
    """
    numero_factorial= math.factorial(numero)
    return numero_factorial

#Ejercicio: Escribir una funcion que reciba una lista y retorne su media

def media(lista_numeros:list)->float:
    """Calcula la media de una lista de numeros
    
    Args:
        lista_numeros (list): Lista con numeros enteros o decimales
        
    Returns:
        float: Media de la lista de numeros
    """
    return np.mean(lista_numeros)
print(media([1,2,3,4,5]))