#1 Aca tenemos que llamar a la funcion validador y recibir
from funciones import validador

persona = ["apellido", 2010, 180]

resultado = validador(persona)

if resultado[0]:
    print("Nacido en 2010 o mas")

if resultado[1]:
    print("Cumple con la altura")

    
    
    