import random, pickle, os

def genticket():
    os.system("cls")
    u_ticket = str(input("----->Ingresa tu nombre:"))
    u_sector = str(input("----->Ingresa tu sector:"))
    u_asunto = str(input("----->Ingresa tu asunto:"))
    u_mensaje = str(input("----->Ingresa tu mensaje:"))
    numero_random = random.randrange(1000, 9999)
    t_d1={"nombre": " ","sector": " ","asunto": " ","mensaje": " ","numeroticket": " "}
    nuevos_datos = {"nombre" : u_ticket,"sector":u_sector,"asunto":u_asunto,"mensaje": u_mensaje,"numeroticket": numero_random }
    t_d1.update(nuevos_datos)
    t_d2=t_d1
    with open("tgenerado.pickle", "wb") as f:
        pickle.dump(t_d2, f)
    with open("tgenerado.pickle", "rb") as f:
        t_d2=pickle.load(f)
        f.close()
    os.system("cls")
    from ticket import ticket
    ticket()
genticket()