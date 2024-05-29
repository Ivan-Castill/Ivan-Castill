import time

precioCompra= float(input("ingrese el precio final de compra: "))
cantidadPrendas= int(input("ingrese la cantidad de prendas"))

print("procesando los datos")
print("por favor espere.....")
time.sleep(3)

if cantidadPrendas>20:
    descuento=0,1 * precioCompra
    precioFinal= precioCompra-descuento
    print(f"La cantidad de prendas fueron {cantidadPrendas}")
    print(f"El precio final a pagar es de {precioFinal}")
elif cantidadPrendas>=10 and cantidadPrendas<= 20:
    descuento=0,5 * precioCompra
    precioFinal= precioCompra-descuento
    print(f"La cantidad de prendas fueron {cantidadPrendas}")
    print(f"El precio final a pagar es de {precioFinal}")
elif cantidadPrendas<=9:
    print(f"la cantidad de prendas fueron {cantidadPrendas}")
    print(f"el precio final a pagar es de {precioCompra}")