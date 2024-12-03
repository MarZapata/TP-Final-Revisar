import pickle
def ticketconsulta():
    with open("tgenerado.pickle", "rb") as f:
            t_d2=pickle.load(f)
            f.close()
    t_d4=t_d2
    del t_d2
    print("====================================================================================")
    print(f'                         Recuperado el ticket:{t_d4["numeroticket"]}')
    print("====================================================================================")
    print(" ")
    print(f'Generado por:{t_d4["nombre"].upper()}')
    print(f'Del sector:{t_d4["sector"].upper()}')
    print(f'Asunto:{t_d4["asunto"].upper()}')
    print(f'Mensaje:{t_d4["mensaje"].upper()}')
    print(" ")
    print("====================================================================================")
    print("                      Gracias por usar el sistema de consulta")
    print("====================================================================================")   
ticketconsulta()
from seguirct import seguirct
seguirct()