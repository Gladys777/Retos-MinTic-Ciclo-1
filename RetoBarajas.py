from random import shuffle

def generar_baraja(tipos_cartas, n_palos):
        
    tipos_barajas = []
    baraja = ()
    
    for i in range(n_palos):
      tipos_barajas.extend(tipos_cartas)
    shuffle(tipos_barajas) 
    baraja = tuple(tipos_barajas)
    
    return baraja