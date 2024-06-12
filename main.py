#presentacion del programa....
print("-------------LOGIN-AMAZON-------------")
#dato para el usuario y la contraseña...
usuario= "admin@amazon.com"
password= "Secret*"
codigo_cupo="junio-epn"
#verificacion de usuario...
user=input(" Ingrese tu email: ")
passw=input(" Ingrese tu password: ")
while user!=usuario and passw!=password:
    print("------------ERROR-------------\n Credenciales incorrectas....")
    user=input(" Ingrese tu email: ")
    passw=input(" Ingrese tu password: ")
if user==usuario and passw==password:
    print("-------------AMAZON-ECUADOR-------------")
    print(f"     Bienvenido {user}.")
    print("\n Menu de opciones \n 1.- Ingresar productos al carrito de compras.\n 2.- Facturar.\n 3.-Salir.")
    opcion=int(input(" Ingresar opcion: "))
#menu
#verificacion de menu...
while opcion!=1 and opcion!=2 and opcion!=3 :
    print("------------ERROR-------------\n Opcion no validad\n Intente de nuevo....")
    print("\n Menu de opciones \n 1.- Ingresar productos al carrito de compras.\n 2.- Facturar.\n 3.-Salir.")
    opcion=int(input(" Ingresar opcion: "))
if opcion==3:
    print(" Muchas gracias porutilizar nuestro sistema.....>-< \n Que tenga un lindo dia/noche..")
elif opcion==1:
    #validacion de producto..
    n_producto=int(input(" Ingrese el numero de productos a registrar: "))
    while n_producto<=0:
        print("------------ERROR-------------\n El numero de productos es incorrecto....")
        n_producto=int(input(" Ingrese el numero de productos a registrar: "))
    N_=1
    contador_producto=0
    sumatoria_precio_descuento=0.0
    contador_cupon=0
    while N_<=n_producto:
        print(f"El producto {N_} tiene cupon de descuento? ")
        contador_producto+=1
        N_+=1
        sumatoria_precio=0.0
        opcion_cupo=input(" Ingrese si o no: ")
        if opcion_cupo=="si":
            ingre_cupo=input(" Ingrese el codigo del cupon: ")
            while ingre_cupo!=codigo_cupo:
                print("------------ERROR-------------\n El codigo ingresado es incorrecto....")
                ingre_cupo=input(" Ingrese el codigo del cupon: ")
            if ingre_cupo==codigo_cupo:
                precio_producto=float(input(" Ingrese el precio del producto: "))
                descue=precio_producto/2
                contador_cupon+=1
            sumatoria_precio_descuento+=descue
        elif opcion_cupo=="no":
            precio_producto=float(input(" Ingrese el precio del producto: "))
            sumatoria_precio+=precio_producto
        total=sumatoria_precio_descuento+sumatoria_precio
elif opcion==2:
    print("----------------FACTURA ELECTRONICA------------")
    print(" La factura sera enviada a su correo electronico..")
    print("------------------DESCUENTO--------------------")
    print("    *Detalle del cupon de descuento.")
    print(f"    *Nombre del cupon de descuento es {codigo_cupo}.")
    print(f"    *El numero de productos con descuento son: {contador_cupon}")
    print(f"    *El precio final de la compra es de ${total}")
print("\n Menu de opciones \n 1.- Ingresar productos al carrito de compras.\n 2.- Facturar.\n 3.-Salir.")
opcion=int(input(" Ingresar opcion: "))
if opcion==2:
    print("----------------FACTURA ELECTRONICA------------")
    print(" La factura sera enviada a su correo electronico..")
    print("------------------DESCUENTO--------------------")
    print("    *Detalle del cupon de descuento.")
    print(f"    *Nombre del cupon de descuento es {codigo_cupo}.")
    print(f"    *El numero de productos con descuento son: {contador_cupon}")
    print(f"    *El precio final de la compra es de ${total}")
