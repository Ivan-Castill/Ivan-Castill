# 1.- menu👌
# 2.- opcion 1(cliente(nombre;apellido;telefono;),
#             para la persona(nombre;apellido;telefono),
#             y otro menu de opciones)
# 3.-opcion 2(mostrar la informacion de todos los pedido con un codigo de pedido)
# 4.-opcion 3(con el codigo de pedido mostrar a detalle el pedido del codigo)
# 5.- opcion 4 ( salir del programa)

# 1.-menu
# MAXIMO 4 CLIENTES
cliente_nombres=[]
cliente_apellido=[]
cliente_telefono=[]

plicrush_nombre=[]
plicrush_dependencia=[]
plicrush_telefono=[]

codigo=[]
pago_final=[]



def menu():
    print("\n ¿Que accion desea realizar?")
    print(" +  1) Registrar pedidos")
    print(" +  2) Mostrar pedidos")
    print(" +  3) Mostrar detalles de un pedido")
    print(" +  4) Salir del sistema")
    opcion=input(" Ingrese la opcion: ")
    return int(opcion)
def opcion1():
    print("------------NUEVO PEDIDO-----")
    print("         Ingrese los datos del cliente  ")
    nombre_cliente=input(" Nombre: ")
    apellido_cliente=input(" Apellido: ")
    telefono_cliente=input(" Telefono: ")
    # cliente_nombres[0].append(nombre_cliente)
    # cliente_nombres[0].append(apellido_cliente)
    # cliente_nombres[0].append(telefono_cliente)
    print("         Ingrese los datos de la policrush")
    nombre_policrush=input(" Nombre: ")
    dependencia_policrush=input(" Dependencia: ")
    telefono_policrush=input(" Telefono: ")
    print("         Seleccion del regalo")
    print(" +  1) Opcion 1: Poliflor + Polipeluche = $2.50")
    print(" +  2) Opcion 2: Poliflor + Policarta = $1.50")
    print(" +  3) Opcion 3: Poliflor + Polillavero = $2.00")
    print(" +  4) Opcion 4: Poliflor + Polivaso = $2.75")
    opc=input(" Ingrese la opcion: ")
    print("--------PERDIDO REGISTRADO CON EXITO------")
    return int(opc)
def opcion2(n_pedidos):
    
    print("--------DETALLE DE TODOS LOS PEDIDOS----------")
    print("------------------------------")
    if n_pedidos>0:
        for i in range(n_pedidos):
            print(f" Detalle del pedido {i+1}")
            print("\n Datos del Cliente")
            print(f"         + Nombre: {cliente_nombres[i+1]}")
            print(f"         + Apellido: {cliente_apellido[i+1]}")
            print(f"         + Telefono: {cliente_telefono[i+1]}")
            print("\n Datos de la entrega")
            print(f"         + Nombre: {plicrush_nombre[i+1]}")
            print(f"         + Dependencia: {plicrush_dependencia[i+1]}")
            print(f"         + Telefono: {plicrush_telefono[i+1]}")
            print("\n Datos del pago ")
            print(f"         + Codigo del pedido: {codigo[i+1]} ")
            print(f"         + Pago final: {pago_final[i+1]} ")
    elif n_pedidos<= 0: 
        print(" No Existen Pedidos Registrados")
    print("------------------------------")
def opcion3():
    ingreso_codigo=input(" Ingrese el codigo del pedido: ")
    if (ingreso_codigo in codigo):
        print("Pedido encontrado")
        print("--------------------------")
        print("Detalle")
        print("\n Datos del Cliente")
        print(f"         + Nombre: {cliente_nombres[i+1]}")
        print(f"         + Apellido: {cliente_apellido[i+1]}")
        print(f"         + Telefono: {cliente_telefono[i+1]}")
        print("\n Datos de la entrega")
        print(f"         + Nombre: {plicrush_nombre[i+1]}")
        print(f"         + Dependencia: {plicrush_dependencia[i+1]}")
        print(f"         + Telefono: {plicrush_telefono[i+1]}")
        print("\n Datos del pago ")
        print(f"         + Codigo del pedido: {codigo[i+1]} ")
        print(f"         + Pago final: {pago_final[i+1]} ")
    elif(ingreso_codigo!= codigo):
        print("+++++++++ERROR+++++++++++")
        print("No existe ese codigo de pedido registrado")
def main():
    print("----------MI POLICRUSH-----------")
    print("     +++Bienvenido(a)+++")
    men=menu()
    opcion=0
    while opcion != 4:
        opcion = MENU()
        if opcion == 1:
            opcion1()
        elif opcion == 2:
            opcion2()
        elif opcion == 3:
            opcion3
        elif opcion ==4:
            print(" Gracias por su atencion \n lindo dia....")
        else:
            print("Opcion no valida")
main()





