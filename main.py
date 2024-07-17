# 1.- menu👌
# 2.- opcion 1(cliente(nombre;apellido;telefono;),
#             para la persona(nombre;apellido;telefono),
#             y otro menu de opciones)
# 3.-opcion 2(mostrar la informacion de todos los pedido con un codigo de pedido)
# 4.-opcion 3(con el codigo de pedido mostrar a detalle el pedido del codigo)
# 5.- opcion 4 ( salir del programa)

# 1.-menu
# MAXIMO 4 CLIENTES
# Máximo 4 clientes
clientes = []
plicrushes = []
pedidos = []

def menu():
    print("\n¿Qué acción desea realizar?")
    print("1) Registrar pedidos")
    print("2) Mostrar pedidos")
    print("3) Mostrar detalles de un pedido")
    print("4) Salir del sistema")
    opcion = input("Ingrese la opción: ")
    return int(opcion)

def registrar_pedido():
    if len(clientes) >= 4:
        print("Máximo de clientes alcanzado.")
        return
    
    print("------------NUEVO PEDIDO------------")
    print("Ingrese los datos del cliente")
    nombre_cliente = input("Nombre: ")
    apellido_cliente = input("Apellido: ")
    telefono_cliente = input("Teléfono: ")
    
    cliente = {
        'nombre': nombre_cliente,
        'apellido': apellido_cliente,
        'telefono': telefono_cliente
    }
    clientes.append(cliente)
    
    print("Ingrese los datos de la policrush")
    nombre_policrush = input("Nombre: ")
    dependencia_policrush = input("Dependencia: ")
    telefono_policrush = input("Teléfono: ")
    
    policrush = {
        'nombre': nombre_policrush,
        'dependencia': dependencia_policrush,
        'telefono': telefono_policrush
    }
    plicrushes.append(policrush)
    
    print("Seleccion del regalo")
    print("1) Poliflor + Polipeluche = $2.50")
    print("2) Poliflor + Policarta = $1.50")
    print("3) Poliflor + Polillavero = $2.00")
    print("4) Poliflor + Polivaso = $2.75")
    opc = int(input("Ingrese la opción: "))
    
    if opc == 1:
        precio = 2.50
    elif opc == 2:
        precio = 1.50
    elif opc == 3:
        precio = 2.00
    elif opc == 4:
        precio = 2.75
    else:
        print("Opción no válida")
        return
    
    codigo_pedido = len(pedidos) + 1
    pedido = {
        'codigo': codigo_pedido,
        'cliente': cliente,
        'policrush': policrush,
        'precio': precio
    }
    pedidos.append(pedido)
    
    print("--------PEDIDO REGISTRADO CON ÉXITO--------")

def mostrar_pedidos():
    print("--------DETALLE DE TODOS LOS PEDIDOS--------")
    if len(pedidos) > 0:
        for pedido in pedidos:
            print(f"Detalle del pedido {pedido['codigo']}")
            print("Datos del Cliente")
            print(f"    + Nombre: {pedido['cliente']['nombre']}")
            print(f"    + Apellido: {pedido['cliente']['apellido']}")
            print(f"    + Teléfono: {pedido['cliente']['telefono']}")
            print("Datos de la entrega")
            print(f"    + Nombre: {pedido['policrush']['nombre']}")
            print(f"    + Dependencia: {pedido['policrush']['dependencia']}")
            print(f"    + Teléfono: {pedido['policrush']['telefono']}")
            print("Datos del pago")
            print(f"    + Código del pedido: {pedido['codigo']}")
            print(f"    + Pago final: {pedido['precio']}")
            print("------------------------------")
    else:
        print("No existen pedidos registrados")
    print("------------------------------")

def mostrar_detalle_pedido():
    ingreso_codigo = int(input("Ingrese el código del pedido: "))
    pedido_encontrado = next((pedido for pedido in pedidos if pedido['codigo'] == ingreso_codigo), None)
    
    if pedido_encontrado:
        print("Pedido encontrado")
        print("--------------------------")
        print("Detalle")
        print("Datos del Cliente")
        print(f"    + Nombre: {pedido_encontrado['cliente']['nombre']}")
        print(f"    + Apellido: {pedido_encontrado['cliente']['apellido']}")
        print(f"    + Teléfono: {pedido_encontrado['cliente']['telefono']}")
        print("Datos de la entrega")
        print(f"    + Nombre: {pedido_encontrado['policrush']['nombre']}")
        print(f"    + Dependencia: {pedido_encontrado['policrush']['dependencia']}")
        print(f"    + Teléfono: {pedido_encontrado['policrush']['telefono']}")
        print("Datos del pago")
        print(f"    + Código del pedido: {pedido_encontrado['codigo']}")
        print(f"    + Pago final: {pedido_encontrado['precio']}")
    else:
        print("+++++++++ERROR+++++++++++")
        print("No existe ese código de pedido registrado")

def main():
    print("----------MI POLICRUSH-----------")
    print("     +++Bienvenido(a)+++")
    opcion = 0
    while opcion != 4:
        opcion = menu()
        if opcion == 1:
            registrar_pedido()
        elif opcion == 2:
            mostrar_pedidos()
        elif opcion == 3:
            mostrar_detalle_pedido()
        elif opcion == 4:
            print("Gracias por su atención. Lindo día....")
        else:
            print("Opción no válida")

main()
        
