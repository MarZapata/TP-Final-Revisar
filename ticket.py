import pickle

def ticket():
    with open("tgenerado.pickle", "rb") as f:
            t_d2=pickle.load(f)
            f.close()
    t_d3=t_d2
    del t_d2
    print("====================================================================================")
    print("                    Generado exitosamente el siguiente Ticket")
    print("====================================================================================")
    print(" ")
    print(f'Su nombre es:{t_d3["nombre"].upper()}')
    print(f'Su sector es:{t_d3["sector"].upper()}')
    print(f'Su asunto es:{t_d3["asunto"].upper()}')
    print(f'Su mensaje es:{t_d3["mensaje"].upper()}')
    print(" ")
    print("====================================================================================")
    print(f'                         Su número de ticket es:{t_d3["numeroticket"]}')
    print("              Favor de recordar este número para posibles consultas")
    print("====================================================================================")
    
ticket()
from seguirgt import seguir
seguir()

