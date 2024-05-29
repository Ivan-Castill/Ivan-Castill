'''
#contador
contador_miro=10
contador_miro=contador_miro-1
if contador_miro==0: 
    print("La comidad esta lista")


#acumulador

#for
#los iterables y los iteradores
#iterable==>tipo de dato
#iterador==> i lo q lo contiene
#for i in [1,2,3,4,5]:
  #  print(i)
#print("-------------------")
for i in range(1,7):
    print(f"el valor es"{i})
#iterable==>[1,2,3,4,5]
#iterador==> i lo q lo contiene

#while

while (True):
    #bloque de codigo
    print(" me muero de sueñor")

i=1
while(i<=3):
    print(i)
    i=i+1
    print("otra logica fuera del while")

passw=int(input("Ingresa tu password:"))
while passw !=3:
    print("password incorrecto:")
    passw =int(input("ingrese tu password")) #ese algo  |

print()
print("bienvenido usuario")
print("-------------------------------")


reiniciarprograma="si"
while reiniciarprograma=="si":
    print("realizar el pedido.....")
    print("desea realizar otro pedido?")
    reiniciarprograma=input("ingrese si o no:")
    print()
    print("muchas gracias por tu visita")


#ejercicio 1
contador_habitacion=0  #variable global
for i in range(1,6):
    print(f"¿la luz de la habitacion {i} se encuentra prendida o apagada?")
    estado_habitacion=input("si o no ")
    if estado_habitacion=="si":
        #estado_habitacion=0 ====>variable local
        contador_habitacion += 1
if contador_habitacionv>=2:
    print("alertar al usuario")

#while
contador_habitacion_luz=0
num_habitaciones=1
while num_habitaciones<=5:
    print(f"¿la luz de la habitacion {num_habitaciones} se encuentra prendida o apagada?")
    estado_habitacion=input("ingrese si o no :")
    if estado_habitacion=="si":
        contador_habitacion_luz+=1
    num_habitaciones+=1

if contador_habitacion_luz>=2:
    print("alertar al usuario")

'''

#while
sumatoria_guaguas=0.0
contador_mora=0
contador_guaguas=0
print("----------la union---------")
num_guaguas=int(input("Ingrese el numero de guaguas de pan "))
while contador_guaguas<num_guaguas:
    precio_guaguas=float(input(f"Ingrese el prescio de la guagua {contador_guaguas+1}"))
    sumatoria_guaguas+=precio_guaguas
    print("La guagua es de mora")
    tipo_guagua=input("si o no ")
    if tipo_guagua=="si":
        contador_mora+=1
    contador_guaguas+=1
print ("el pago a realizar.....")
print(f"el total de guaguas es {num_guaguas}")
print(f"el precio final es {sumatoria_guaguas}")
print(f"las guaguas de mora son {contador_guaguas}")
