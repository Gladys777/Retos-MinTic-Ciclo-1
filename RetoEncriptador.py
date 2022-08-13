from string import ascii_uppercase as alfabeto


def encriptador(mensaje):
    
    valorestUnicos = list(mensaje)
    valorestUnicos = set(valorestUnicos) 
    if len(valorestUnicos) <= 26:
        
        clave= dict(zip(valorestUnicos, alfabeto))
        
        encriptado = ''
        for letra in mensaje:
            encriptado = encriptado+clave[letra]
    
   
    return encriptado, clave

    
def desencriptador(encriptado, clave):
  
    listaClave = list(clave.keys())
    listatValor = list(clave.values())
    desencriptado=[]
        
    for i in encriptado:
         serie=listatValor.index(i)
         desencriptado.append(listaClave[serie])
    
    desencriptado = "".join(desencriptado)
    print(desencriptado)
    
    
    return desencriptado
