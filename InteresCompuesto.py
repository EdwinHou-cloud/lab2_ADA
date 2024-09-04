from math import log

print("Bienvenido, ingrese los datos")
while(True):
    try:
        valorAcumulado = float(input('Valor acumulado: '))
        if valorAcumulado <= 0:
            print("El valor acumulado debe ser mayor que cero")
    except ValueError:
        print("Ha ocurrido un error con el valor ingresado, intente nuevamente")
    
    try:
        depositoMensual = float(input('Valor del depósito mensual: '))
        if depositoMensual <= 0:
            print("El valor del depósito mensual debe ser mayor que cero")
    except ValueError:
        print("Ha ocurrido un error con el valor ingresado, intente nuevamente")
    
    try:
        interesAnual = float(input('Interés anual en porcentaje: '))
        if interesAnual <= 0:
            print("El interés anual debe ser mayor que cero")
    except ValueError:
        print("Ha ocurrido un error con el valor ingresado, intente nuevamente")
    
    interesMensual = 0.01 * interesAnual / 12
    resultado = log(valorAcumulado * interesMensual / depositoMensual + 1) / log(1 + interesMensual)
        
    print("{:20} {:25} {:25} {:20}".format('Valor Acumulado', 'Valor del deposito mensual', 'Interes anual en porcentaje', 'Resultado'))
    print("{:10} {:20} {:25.2f} {:25.2f}".format(valorAcumulado, depositoMensual, interesAnual, resultado))
    break