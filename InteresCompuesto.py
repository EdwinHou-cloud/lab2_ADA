"""
Hou, Edwin	        8-1021-1916
Arosemena, Miguel	8-1016-2330
Corrales, Diego		8-1001-1890
Camaño, Edward		8-1010-515
Pino, Josué		8-1012-688
"""

# InicioAlgoritmo
from math import log # Importa la función logaritmo de la librería math

print("Bienvenido, ingrese los datos") # Mensaje de bienvenida

while (True): # Bucle infinito hasta que se ingresen los datos correctos
    try:
        # Solicita el valor acumulado al usuario
        valorAcumulado = float(input('Ingrese el valor acumulado: '))
        if valorAcumulado <= 0: # Verifica que el valor acumulado sea mayor que cero
            print("El valor acumulado debe ser mayor que cero")
            continue
        break
    except ValueError:
        print("Ha ocurrido un error con el valor ingresado, intente nuevamente")
        
while(True):    
    try:
         # Solicita el valor del depósito mensual al usuario
        depositoMensual = float(input('Ingrese el valor del depósito mensual: '))
        if depositoMensual <= 0: # Verifica que el depósito mensual sea mayor que cero
            print("El valor del depósito mensual debe ser mayor que cero")
            continue
        break
    except ValueError:
        print("Ha ocurrido un error con el valor ingresado, intente nuevamente")
    
while(True):  
    try:  
         # Solicita el interés anual al usuario
        interesAnual = float(input('Ingrese el interés anual en porcentaje: '))
        if interesAnual <= 0: # Verifica que el interés anual sea mayor que cero
            print("El interés anual debe ser mayor que cero")
            continue
    except ValueError:
        print("Ha ocurrido un error con el valor ingresado, intente nuevamente")
        continue
    
    # Calcula el interés mensual dividiendo el interés anual entre 12 y convirtiéndolo en decimal
    interesMensual = 0.01 * interesAnual / 12
    resultado = log(valorAcumulado * interesMensual / depositoMensual + 1) / log(1 + interesMensual)
    
    # Impresión de la tabla con bordes y separaciones
    print("+" + "-"*22 + "+" + "-"*29 + "+" + "-"*29 + "+" + "-"*22 + "+")
    print("| {:<20} | {:<27} | {:<25} | {:<20} |".format('Valor Acumulado', 'Valor del depósito mensual', 'Interés anual en porcentaje', 'Resultado'))
    print("+" + "-"*22 + "+" + "-"*29 + "+" + "-"*29 + "+" + "-"*22 + "+")
    print("| {:<20.2f} | {:<27.2f} | {:<27.2f} | {:<20.2f} |".format(valorAcumulado, depositoMensual, interesAnual, resultado))
    print("+" + "-"*22 + "+" + "-"*29 + "+" + "-"*29 + "+" + "-"*22 + "+")
    break
# FinAlgoritmo