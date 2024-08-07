

# # intro a diccionarios

# # barco={}
# # barco_dos = dict()

# # barco ={
# #    "contenedor1":"Ropa",
# #    "contenedor1":"zapatos",
# #    "contenedor1":"tecnologia",
# #    "contenedor1":"herraminentas"
# # }
# # #  clave/Propiedad           valor   , 

# carritoCompra={
#     "id":           123,
#     "ordenCompra":  "C-3534",
#     "numItems":     5,
#     "descuento":    True,
#     "totalPagar":   1525.50,
#     "carrito":      ["tv","play","laptop"],
#     "datosEnvio":   {
#                         "ciudad":   "Quito",
#                         "id":           123
#                     }
# }

# # Acceder a los valores

# print(carritoCompra["datosEnvio"].get("ciudad"))

# print(carritoCompra.get("ordenCompra"))

# for clave in carritoCompra:
#     print(carritoCompra[clave])

import pyqrcode
import random
from PIL import Image
# pip install Pillow


# # intro a diccionarios

# # barco={}
# # barco_dos = dict()

# # barco ={
# #    "contenedor1":"Ropa",
# #    "contenedor1":"zapatos",
# #    "contenedor1":"tecnologia",
# #    "contenedor1":"herraminentas"
# # }
# # #  clave/Propiedad           valor   , 

# carritoCompra={
#     "id":           123,
#     "ordenCompra":  "C-3534",
#     "numItems":     5,
#     "descuento":    True,
#     "totalPagar":   1525.50,
#     "carrito":      ["tv","play","laptop"],
#     "datosEnvio":   {
#                         "ciudad":   "Quito",
#                         "id":           123
#                     }
# }

# # Acceder a los valores

# print(carritoCompra["datosEnvio"].get("ciudad"))

# print(carritoCompra.get("ordenCompra"))

# for clave in carritoCompra:
#     print(carritoCompra[clave])

import pyqrcode
import random
from PIL import Image
# pip install Pillow

datospoliperros= {
    "nombre":[],
    "huellaDactilar":[]
}

fotosPoliperros={
    "foto":[]
}

numPerros=0
def menu():
    print("-----BIENVVENIDO/A--------")
    print("¿Que accion desea realixar?")
    print("1) Registrar Poliperros")
    print("2) Mostrar Poliperros")
    print("3) Registrar Foto")
    print("4) Carnet Digital")
    print("5) Salir")
    op=int(input("Ingresa la opcion: "))
    return op
def registroPoliperro(numPerros):
    for i in range(numPerros):
        print("Ingresa los datos del poliperro",i+1)
        nombre=input("Nombre: ")
        huella=input("Huella: ")
        datospoliperros['nombre'].append(nombre)
        datospoliperros['huellaDactilar'].append(huella)
def mostrarPoliperro(numPerros,):
    for i in range (numPerros):
        print("--------------------")
        print("Mostrar los datos del Poliperro",i+1)
        print("* Nombre",datospoliperros['nombre'][i])
        print("* Huella", datospoliperros['huellaDactilar'][i])
        if "foto" in datospoliperros:
            print("* Foto",fotosPoliperros['foto'][i])
            print("-----------------------------")
            imagen=Image.open(fotosPoliperros['foto'][i])
            imagen.show()
            imagen.save(rf'C:\Users\ALGORITMOS DE DATOS\Desktop\Clase 31_07_2024\BDD\dog{i}.png')
def registrarFoto(numPerros):
    for i in range(numPerros):
        print("Ingrese la foto del poliperro",i+1)
        print("¿El poliperro dispone de una imagen?")
        foto=input("Ingrese si o no: ")
        if foto=="si":
            foto=input("Ingrese la ruta de la foto: ")
            fotosPoliperros['foto'].append(foto)
        else:
            fotosPoliperros['foto'].append(r"C:\Users\ALGORITMOS DE DATOS\Desktop\defaultdog.png")
    datospoliperros.update(fotosPoliperros)
def carnetDigital():
    codigo_qr= pyqrcode.create(f'hola')
    nombre_archivo_png="codigo_qr.png"
    codigo_qr.png(nombre_archivo_png,scale=8)


    
def main():
    print("------------SISTEMAS - POLIPERRROS----------------")
    opcion=menu()
    while opcion != 5:
        if opcion==1:
            numPerros =int (input("Ingrese lacantidad de poliperros a registrar: "))
            registroPoliperro(numPerros)
            opcion=menu()
        elif opcion==2:
            mostrarPoliperro(numPerros)
            opcion= menu()
        elif opcion==3:
            registrarFoto(numPerros)
            opcion= menu()
        elif opcion==4:
            print("--- Caso 4---")
            opcion= menu()
    print("gracias buen dia/noche")

main()