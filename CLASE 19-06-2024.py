# # funciones..(0 w 0)
# # print("hello")

# # DECLARAR UNA FUNCIONA SIN PARAMETROS
# #SIN PARAMETROS Y RETORNO
# def mifuncion():
#     print("hola")
# #INVOCAR
# mifuncion()
# # DECLARAR UNA FUNCIONA SIN PARAMETROS
# #CON PARAMETROS Y RETORNO
# def VVALIDAR(USUARIO, mail,avatar):
#     return "hello ", USUARIO

# #INVOCAR
# mifuncion()
# #opcion1
# nombre=input("Ingrese el nombre")
# print(VVALIDAR(nombre,"ivan.castillo@gmail.com",True))
# # opcion2
# resultado=VVALIDAR("Ivan","ivan.castillo@gmail.com",True)
# print(resultado)

# def VVALIDAR(USUARIO, mail,avatar=True):
#     return "hello ", USUARIO,mail,avatar

# #INVOCAR
# # mifuncion()
# #opcion1
# nombre=input("Ingrese el nombre")
# print(VVALIDAR(nombre,"ivan.castillo@gmail.com"))
# # opcion2
# resultado=VVALIDAR("Ivan","ivan.castillo@gmail.com",True)
# print(resultado)
# # (._.)

# print("----------Login Amazon---------")
# email=input("Ingrese tu email: ")
# password=input("Ingrese tu password: ")
# while(email!= "admin@amazon.com" or password!="Secret*"):
#     print("------------Error-----------")
#     email=input("Ingrese tu email: ")
#     password=input("Ingrese tu password: ")
    

# opcion=0
# while opcion!=3:
#     print("----------Login Amazon---------")
#     print(f'BIENVENIDO {email}')
#     print("1- INGRESO DE PRODUCTOS")
#     print("2- FACTURA")
#     print("3- SALIR")
#     opcion=int(input("Ingresar opcion: "))
#     if opcion==1:
#         sumatoria=sumatoriadescuento=promo=0
#         num_produictos=int("ingresar el numero de productos a registrar: ")
#         for i in range(1,num_produictos+1):
#             print(f'El producto {i} tiene descuento?')
#             verificar=input("Ingrese Si o NO: ")
#             if verificar == "si":
#                 codigo=input("Ingresa el codigo de descuento")
#                 promo+=1
#                 precio=float(input(f'Ingrese el precio del producto{i}'))
#                 sumatoriadescuento+=precio
#             else:
#                 precio=float(input(f'Ingrese el precio del producto {i}'))
#                 sumatoriadescuento+=precio
#     elif opcion ==2:
#         print("---------------factura--------------")
#         if promo==2:
#             print("----------Descuento---------")
#             print("Cupon de secuento es junio_epn")
#             print(f" el numero de productos con descuento fueron{promo}")
#             print(f' el precio final es $ {(sumatoriadescuento*0.5)+sumatoria}')
#         else:
#             print("----------Sin descuento-----")
#             print(f'el numero de productos son:{num_produictos}')
#             print(f'el precio final es:{sumatoria}')
# print("muchas Gracias")


#funciones
#Funciones para el menu de opciones
def menuopciones(email):
    print("----------Login Amazon---------")
    print(f'BIENVENIDO {email}')
    print("1- INGRESO DE PRODUCTOS")
    print("2- FACTURA")
    print("3- SALIR")
    opcion=int(input("Ingresar opcion: "))
    return opcion
#funcion para validar el email y password
def validar_email_password(email,password):
    while(email!= "admin@amazon.com" or password!="Secret*"):
        print("------------Error-----------")
        email=input("Ingrese tu email: ")
        password=input("Ingrese tu password: ")
#funcion para validar la cantidad de productos
def validar_cantidad_de_productos():
    num_productos=int("ingresar el numero de productos a registrar: ")
    while num_productos<=0:
        print("------------Error-----------")
        num_productos=int("ingresar el numero de productos a registrar: ")
#funcion para ingresar productos
def ingresar_productos(num_productos):
    sumatoria=sumatoriadescuento=promo=0
    num_productos=int("ingresar el numero de productos a registrar: ")
    for i in range(1,num_productos+1):
        print(f'El producto {i} tiene descuento?')
        verificar=input("Ingrese Si o NO: ")
        if verificar == "si":
            codigo=input("Ingresa el codigo de descuento")
            promo+=1
            precio=float(input(f'Ingrese el precio del producto{i}'))
            sumatoriadescuento+=precio
        else:
            precio=float(input(f'Ingrese el precio del producto {i}'))
            sumatoriadescuento+=precio
    return (promo,sumatoria,sumatoriadescuento)
# funcion para moastrar num_produictos
def mostrar_productos(promo,sumatoria,sumatoriadescuento,num_productos):
    print("---------------factura--------------")
    if promo==2:
        print("----------Descuento---------")
        print("Cupon de secuento es junio_epn")
        print(f" el numero de productos con descuento fueron{promo}")
        print(f' el precio final es $ {(sumatoriadescuento*0.5)+sumatoria}')
    else:
        print("----------Sin descuento-----")
        print(f'el numero de productos son:{num_productos}')
        print(f'el precio final es:{sumatoria}')
# funcion main
def main():
    print("----------Login Amazon---------")
    email=input("Ingrese tu email: ")
    password=input("Ingrese tu password: ")
    opcion=0
    while opcion!=3:
        opcion==menuopciones(email)
        validar_email_password(email,password)
        if opcion==1:
            promo,sumatoria,sumatoriadescuento,num_productos=ingresar_productos(3)
        elif opcion==2:
            mostrar_productos(promo,sumatoria,sumatoriadescuento,num_productos)
    print("muchas gracias")
# 42 lineas ====
main()