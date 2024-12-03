
def seguir():
    controlgt=True
    while controlgt==True:
        consultaseguir= input("--------->   Querés crear otro ticket?   <---------   ( 1 = si / 2 = no ):")
        if consultaseguir.isdigit():
            consultaseguir=int(consultaseguir)
            if consultaseguir == 1:
                from genticket import genticket
                controlgt=False
                genticket()
            elif consultaseguir == 2:
                controlgt=False
                from main import main
                main()
            else:
                print("La opción ingresada no es válida, elegí entre 1 ó 2")
        else:
            print("La opción ingresada no es válida, elegí entre 1 ó 2")
seguir()
           
