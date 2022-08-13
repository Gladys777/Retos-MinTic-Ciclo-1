from student_utilities import input, print
import math

def solucion(edad, peso): 
   
    
    edad = int(𝑖𝑛𝑝𝑢𝑡("Indicar la edad del paciente: "))
    peso = 𝑓𝑙𝑜𝑎𝑡(𝑖𝑛𝑝𝑢𝑡("Indicar el peso del paciente en kilogramos: "))
    
    carbohidratos = 60.1 /1000
    proteinas = 30.5 /1000
    verduras = -24.4 /1000
    
    dieta_a = 2 * carbohidratos + proteinas + 2 * verduras
    dieta_b = 0.6 * carbohidratos + proteinas + 4 * verduras
    dieta_c = 0.5 * carbohidratos + 0.7 * proteinas + 2 * verduras
    
    while edad >= 5 and edad <= 10:
        if peso < 16: 
           estado = 'A'
           dias = int((22-peso)/dieta_a)+1
           print(f'El estado nutricional del paciente es {estado} y se requieren {dias} dias de dieta para que alcance un peso saludable')
      
        elif peso >= 28: 
          estado = 'B'  
          dias = int((24-peso)/dieta_b)+1
          print(f'El estado nutricional del paciente es {estado} y se requieren {dias} dias de dieta para que alcance un peso saludable')
    
        elif peso >= 16 and peso <= 28:
          estado = 'C'  
          dias = int((28-peso)/dieta_c)+1
          print(f'El estado nutricional del paciente es {estado} y se requieren {dias} dias de dieta para que alcance el peso maximo')
        break
    
    while edad <= 13 and edad >= 11:
        if peso < 30: 
           estado = 'A'
           dias = int((32-peso)/dieta_a)+1
           print(f'El estado nutricional del paciente es {estado} y se requieren {dias} dias de dieta para que alcance un peso saludable')
      
        elif peso >= 50: 
          estado = 'B'  
          dias = int((43-peso)/dieta_b)+1
          print(f'El estado nutricional del paciente es {estado} y se requieren {dias} dias de dieta para que alcance un peso saludable')
    
        elif peso >= 30 and peso <= 50:
          estado = 'C'  
          dias = int((50-peso)/dieta_c)+1
          print(f'El estado nutricional del paciente es {estado} y se requieren {dias} dias de dieta para que alcance el peso maximo')
        break
    
    while edad <= 17 and edad >= 14:
        if peso < 51: 
           estado = 'A'
           dias = int((56-peso)/dieta_a)+1
           print(f'El estado nutricional del paciente es {estado} y se requieren {dias} dias de dieta para que alcance un peso saludable')
      
        elif peso >= 63: 
          estado = 'B'  
          dias = int((58-peso)/dieta_b)+1
          print(f'El estado nutricional del paciente es {estado} y se requieren {dias} dias de dieta para que alcance un peso saludable')
    
        elif peso >= 51 and peso <= 63:
          estado = 'C'  
          dias = int((63-peso)/dieta_c)+1
          print(f'El estado nutricional del paciente es {estado} y se requieren {dias} dias de dieta para que alcance el peso maximo')
        break

    