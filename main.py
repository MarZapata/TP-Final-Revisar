import os
from menu import menu
from salir import salir

def main():
    os.system("cls")
    menu()
    control=True
    while control==True:
        seleccion_menu = input("Digite su selección:")
        if seleccion_menu.isdigit():
            seleccion_menu=int(seleccion_menu)
            if seleccion_menu==1:
                from genticket import genticket
                genticket()
                control=False
            elif seleccion_menu==2:
                from consultaticket import consultaticket
                consultaticket()
                control=False
            elif seleccion_menu==3:
                control=False
                salir()   
            else:
                print("La opción ingresada no es válida, elige entre opción 1, 2 o 3")
        else:
            print("La opción ingresada no es válida, elige entre opción 1, 2 o 3")  
    os.system("cls")
    print(" ")
    print("----------------> Gracias por haber usado este software <----------------")
main()