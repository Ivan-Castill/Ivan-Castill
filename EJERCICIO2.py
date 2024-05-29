

import webbrowser


print("bienvenido, Byron")
dia= input("ingrese un dia de la semana: ")

match (dia):
    case "lunes":
        print("hoy debes, hacer ejercicios")
    case "martes":
        print("hoy debes, hacer las compras")
    case "miercoles":
        print("hoy debes, ver peliculas")
        print("deseas que te recomiende un canal?")
        tipoWeb=input("DIme si o no:")
        if tipoWeb== "si":
            webbrowser.open_new_tab("https://www.crunchyroll.com")
    case "jueves":
        print("hoy debes,hacer deberes")
    case "viernes":
        print("hoy debes, jugar futbol")
    case _:
        print("no existe actividad para ese dia")



