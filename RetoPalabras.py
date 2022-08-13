from operator import itemgetter

def suprimir_caracteres(lista):
    caracteres_especiales = ['-','¿','?','.',',','¡','!',':','"','–']
    lista = ' '.join(lista)
    lista = lista.lower()

    for caracter in caracteres_especiales:
        lista = lista.replace(caracter, "")

    lista = lista.split(" ")

    return lista

def contar_palabras(lista):
    mas_frecuentes = {}
    for palabra in lista:
        if palabra != '':
            mas_frecuentes[palabra] = lista.count(palabra)  

    lista_mas_frecuentes = sorted(mas_frecuentes.items(), key=itemgetter(1), reverse=True)
    lista_ordenada =[]
    for i in range(len(lista_mas_frecuentes)):
        lista_ordenada.append(list(lista_mas_frecuentes[i]))

    lista_texto = []
    for i in range(20):
        lista_texto.append(lista_ordenada[i])

    return lista_texto


def main(lista_texto):
    # ACÁ INICIA LA FUNCIÓN main
    lista = suprimir_caracteres(lista_texto)
    lista_conteo = contar_palabras(lista) 
    
    return lista_conteo