import pickle, os

def consultaticket():
    os.system("cls") 
    controlconsulta=True
    while controlconsulta==True:
        with open("tgenerado.pickle", "rb") as f:
            t_d2=pickle.load(f)
            f.close()
        aux1=int(t_d2.get('numeroticket'))
        num_ticket =(input("----->Ingresa el número del ticket a consultar:"))
        if num_ticket.isdigit():
            num_ticket=int(num_ticket)
            if num_ticket==aux1:
                from ticketconsulta import ticketconsulta
                ticketconsulta()
                controlconsulta=False
            else:
                print("el ticket seleccionado no existe")
                controlconsulta=False
        else:
            print("La opción ingresada no es válida, favor solo ingresar números")
consultaticket()
