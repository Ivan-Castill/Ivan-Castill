'''
# operadores aritmeticos
## + - * / % **  //
x=10
y=3

print(x//3)##solo me da el resultado

#operadores realcionales
# == != > >= < <=
x=2
y=3

print(x!=y)

#operadores logicos
# and or not

print(True and False)

print(not False)

print(True and True)
print(True or False)

#Condicional Simple

user ="joel123"

if user=="joel123":
    print("user correct")
else:
    print("user denied")

'''

#condicional anidado
user = "Joel123"
rol = "admin"

if (user=="Joel123"and rol=="admin"):
    print("welcome user admin")
    status=True
    if status==False:   #condicion multiple
        print("profile")
    else:
        print("guest")
elif (user=="ivan123"and rol=="employee"):
    print("welcome user employee")
elif (user=="susan123"and rol=="secretary"):
    print("welcome user secretary")
elif (user=="byron123"and rol=="invite"):
    print("welcome user invite")
else:
    print("user and rol not found")
