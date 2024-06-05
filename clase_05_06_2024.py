'''
#numeros ramdom
import random
#acceder al S.O
import os
from os import system
#Correos
from email.message import EmailMessage
import smtplib

user_registro=""
password_registro=""

def enviarCorreo(correo,codigo):
  remitente = "ivan2003castillo12345@gmail.com"
  destinatario = correo
  mensaje = f"El codigo de acceso es {codigo}"
  email = EmailMessage()
  email["From"] = remitente
  email["To"] = destinatario
  email["Subject"] = "Correo de prueba"
  email.set_content(mensaje)
  smtp = smtplib.SMTP_SSL("smtp.gmail.com")
  smtp.login(remitente, "derf dqmk dhcc norg")
  smtp.sendmail(remitente, destinatario, email.as_string())
  smtp.quit()

print("BIENVENIDO A TIK TOK")
print("Si tiene una cuenta ingrese si")
print("Si no tiene una cuenta ingrese no")
login=input("Ingrese la palabra: ")
if login=="no":
    print("Para crear una cuenta, ingresa los siguientes datos")
    correo=input("ingrese tu correo electronico: ")
    user_registro=input("ingrese tu nombre de usuario: ")
    password_registro=input("Ingrese tu contraseña: ")
    codigo_acceso=random.randint(1,100)# crear numero aleatorio 1-100
    enviarCorreo(correo,codigo_acceso)
    print("codigo de acceso enviado al correo electronico")
    print("Felicidades. Ya puedes iniciar sesion")
if login=="no":
    print()
    codigo=int(input("Porfavor, ingrese el codigo enviado al correo: "))
    while codigo_acceso!=codigo:
        print("Error,verifique el codigo de acceso")
        codigo=int(input("Porfavor, ingrese el codigo enviado al correo: "))
login="si"
while login=="si":
    user=input("Ingrese el usuario: ")
    password=input("Ingrese el password: ")
    if (user==user_registro or user=="Ivvan") and(password==password_registro or password=="123"):
        print("Bienvenido",user) 
        print("revisa tus ultimos videos\nEPN\n MOMOS EPN\n POLICRUSH EPN\n NOTICIAS EPN\n Para salir, digitar x")
        login=input("Ingrese la opcion: ")
    else:
        print("usuario y contraseñas incorrecto")

print("muchas gracias")
'''
from os import system # nos sirve para acceder al sistema oprativo
print("-------Bienvenido-------")
print("MENU DE OPCIONES\n1.- Problema 1\n2.-Problema 2\n3.-Salir")
opcion=int(input("Ingresa la opcion: "))
#validacion de 1y2
system("cls")# si es una teminal basada en linux(clear) o en window(cls)
while opcion > 3 or opcion<=0:
    print("ERROR\n Esa opcion no existe")
    print("MENU DE OPCIONES\n1.- Problema 1\n2.-Problema 2\n3.-Salir")
    opcion=int(input("Ingresa la opcion: "))
while opcion ==1 or opcion==2:
    if opcion==1:
        print("logica del problema 1")
        print("MENU DE OPCIONES\n1.- Problema 1\n2.-Problema 2\n3.-Salir")
        opcion=int(input("Ingresa la opcion: "))
    elif opcion==2:
        print("logica del problema 2")
        print("MENU DE OPCIONES\n1.- Problema 1\n2.-Problema 2\n3.-Salir")
        opcion=int(input("Ingresa la opcion: "))
print("muchas gracias")