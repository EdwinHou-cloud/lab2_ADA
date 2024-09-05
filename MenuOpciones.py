"""
Hou, Edwin	        8-1021-1916
Arosemena, Miguel	8-1016-2330
Corrales, Diego		8-1001-1890
Camaño, Edward		8-1010-515
Pino, Josué		    8-1012-688
"""

# InicioAlgoritmo
def presentacion():
    print("\n{:^70}".format("UNIVERSIDAD TECNOLÓGICA DE PANAMÁ"))
    print("{:^70}".format("FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES"))
    print("{:^70}".format("DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS"))
    print("{:^70}".format("LABORATORIO 1"))
    print("{:^70}".format("FC-FISC-1-8-2016"))
    print("Integrantes: Arosemana, Miguel")
    print("{:^40}".format("Camaño, Edward"))
    print("{:^41}".format("Corrales, Diego"))
    print("{:^36}".format("Hou, Edwin"))
    print("{:^38}".format("Pino, Josue"))
    
def tienda_zapatos():
    # Esta función calcula el total a pagar, incluyendo posibles descuentos según la cantidad comprada.
    try:
        # Solicita al usuario la cantidad de zapatos a comprar
        num_zapatos = int(input("Ingrese la cantidad de zapatos a comprar: "))
        precio_zapatos = 35 # Precio fijo por zapato
        total = num_zapatos * precio_zapatos # Calcula el costo total sin descuento
        
        # Aplica descuento según la cantidad de zapatos
        if num_zapatos > 40:
            descuento = 0.40
        elif num_zapatos > 20 and num_zapatos < 25:
            descuento=0.20
        elif num_zapatos > 10:
            descuento=0.10
        else:
          descuento=0.0 # Sin descuento si no se cumplen las condiciones anteriores
          
        # Calcula el total con descuento  
        total_con_descuento= total * (1-descuento)
        print("El descuento aplicado es del {} porciento".format(int(descuento*100)))
        print(f"El total con descuento es: ${total_con_descuento:.2f}")
    except ValueError:
        # Maneja errores si el usuario ingresa un valor no numérico
        print("Error: Por favor, ingrese un número valido.")
        
def supermercado():
     # Esta función calcula el total a pagar con descuentos basados en el tipo de membresía y el monto de la compra.
    try:
        # Solicita al usuario el monto de la compra y el tipo de membresía
        monto_compra = float(input("Ingrese el monto de la compra: "))
        tipo_membresia = input("Ingrese el tipo de membresía (A,B,C): ") .upper() # Convierte la membresía a mayúscula para evitar errores de comparación
        if tipo_membresia == 'A'or tipo_membresia == 'B'or tipo_membresia == 'C':
            # Aplica descuento según el tipo de membresía y monto de compra
            if tipo_membresia == "A" and monto_compra > 100:
                descuento = 0.10
            elif tipo_membresia == "B" and monto_compra > 250:
                descuento= 0.15
            elif tipo_membresia == "C" and monto_compra > 320:
                descuento = 0.20
            else:
                descuento = 0.0 # Sin descuento si no se cumplen las condiciones anteriores            
            # Calcular el total con descuento    
            total_con_descuento= monto_compra * (1-descuento)
            print(f"El total con descuento es: ${total_con_descuento:.2f}")
        else:
            print("El tipo de membresia ingresada es erronea, intente nuevamente")   
    except ValueError:
        # Manejar errores si el usuario ingresa un valor no numérico
        print("Error: por favor, ingrese un monto válido.")
        
        
def despedida():
    # Esta función imprime un mensaje de despedida.
    print("Gracias por usar el programa. ¡Hasta Luego!")
    
def menu():
    # Esta función muestra un menú principal y permite al usuario seleccionar una opción para ejecutar.
    while True: 
        print("\n--- Menú Principal ---")
        print("1. Presentación")
        print("2. Tienda de Zapatos")
        print("3. Supermercado")
        print("4. Despedida")
        
        try: 
            # Captura la opción seleccionada por el usuario
            opcion =int(input("Seleccione una opción: "))
            
            # Ejecuta la función correspondiente según la opción seleccionada
            if opcion == 1:
                presentacion()
            elif opcion == 2:
                tienda_zapatos()
            elif opcion == 3:
                supermercado()
            elif opcion == 4:
                despedida()
                break # Salir del bucle y finalizar el programa
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
        except ValueError:
            # Maneja errores si el usuario ingresa un valor no numérico
            print("Error: Por favor, ingrese un número válido.")

# Inicia el programa llamando a la función del menú
menu() 
# FinAlgoritmo