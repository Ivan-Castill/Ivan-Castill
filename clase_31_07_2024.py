# # data=["Usuario"]
# # data[0]="Autorizado"
# # print(data)
# data2=("Usuario")
# data2[0]="Autorizado"
# print(data2)

# declaracionde una tupla
nombre_tupla = ()

tupleElementos=(1,True,"hola",5.6,'😂')

# # print(tupleElementos[4])

# # print(tupleElementos)

# # for i in tupleElementos:
# #     print(f'tupleElementos[i]',end="")

# # for i in tupleElementos:
# #     print(i,end="")

# i=0 
# while i<len(tupleElementos):
#     print(f'{tupleElementos[i]}',end="")
#     i+=1

# # convercion
# print(tupleElementos)
# print(type(tupleElementos))

# listaElementos= list(tupleElementos)
# print(listaElementos)
# print(type(listaElementos))

# listaElementos2=[1,2,3,54,5,6,'😊']
# print(listaElementos2)
# tupleElementos2=tuple(listaElementos2)
# print(tupleElementos2)
# print(type(tupleElementos2))

#ejercicio 1

# estucutura para progamas
#inportacion de librerias
# import os
# from stdiomask import getpass
# from prettytable import PrettyTable
# #definir variables y constantes globales
# calificaciones_tupla=()
# calificacionesLista=list(calificaciones_tupla)
# numCalificaciones=0
# #declarar funciones
# def menu():
# def agregarCalificaciones(arreglo,n):
# def mostrarCalificaciones(arreglo):
# def guardarAchivo(data):
# def mostarArchivo(data):
# def mostardetalle(arreglo,califi):
# #funcion main
# def main():
# main()
#inportacion de librerias
import os
from stdiomask import getpass
from prettytable import PrettyTable
#definir variables y constantes globales
calificaciones_tupla=()
calificacionesLista=list(calificaciones_tupla)
numCalificaciones=0
#declarar funciones
def menu():
    print("..........SISTEMA POLISAEW 2.0............")
    print("..........Modulo profesor............")
    print("¿que accion desea realizar?")
    print("1) ingrese calificaciones")
    print("2) mostrar calificaciones")
    print("3) detalle de las calificaciones")
    print("4) Mostrar detalle por archivo calificaciones")
    print("5) salir")
    tipoAccion=int(input("ingrese la opcion:"))
    return tipoAccion
def agregarCalificaciones(n):
    for i in range(n):
        print("ingrese la calificacion del estudiante",i+1)
        calificacion=float(input("Calificacion: "))
        calificacionesLista.append(calificacion)
def mostrarCalificaciones(arreglo):
    arreglo.sort()
    print("Las calificaciones registradas son: ")
    print(arreglo)
def guardarAchivo(data):
    archivo=open('C:/Users/ALGORITMOS DE DATOS/Desktop/EJERCI/reporte.txt','w')
    archivo.write("Detalle de calificaciones")
    archivo.write(f'{data}')
    archivo.close()
    print("Informacion agregada exitosamente.......")
def mostarArchivo():
    archivo=open('C:/Users/ALGORITMOS DE DATOS/Desktop/EJERCI/reporte.txt','r')
    lineas= archivo.readlines()
    for i in lineas:
        print(i,end="")
    archivo.close()
def mostardetalle(arreglo,califi):
    contadorApro,contadorRecha,contadorSuspe,sumCalifi=0,0,0,0.0
    for i in arreglo: 
        sumCalifi+=i
    for i in calificacionesLista:
        if 1<=i<=8:
            contadorRecha+=1
        elif 9<=i<=13:
            contadorSuspe+=1
        elif 14<=i<=20:
            contadorApro+=1
    promedio=round((sumCalifi/califi),2)
    print("El promedio es :",promedio)
    guardarAchivo(promedio)
#funcion main
def main():
    password="sistemas"
    if password=="sistemas":
        caso=menu()
        while caso !=5:
            if caso==1:
                N=int(input("Cuantas Calificaciones desea agregar:"))
                agregarCalificaciones(N)
                caso=menu()
            elif caso==2:
                mostrarCalificaciones(calificacionesLista)
                caso=menu()
            elif caso==3:
                mostardetalle(calificacionesLista,N)
                caso=menu()
            elif caso==4:
                mostarArchivo()
                caso=menu()
        print("Muchas gracias")
    else:
        print("Password Incorrecto")
main()
#https://youtu.be/XMvIAKcOJ_w?si=dowmQfqs4uqEJgqL