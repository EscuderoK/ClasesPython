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