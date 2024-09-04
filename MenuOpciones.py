def presentacion():
    print("\n{:^70}".format("UNIVERSIDAD TECNOLÓGICA DE PANAMÁ"))
    print("{:^70}".format("FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES"))
    print("{:^70}".format("DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS"))
    print("{:^70}".format("LABORATORIO 1"))
    print("{:^70}".format("FC-FISC-1-8-2016"))
    print("Integrantes: Arosemana, Miguel")
    print("{:^40}".format("Camano, Edward"))
    print("{:^41}".format("Corrales, Diego"))
    print("{:^36}".format("Hou, Edwin"))
    print("{:^38}".format("Pino, Josue"))
    
def tienda_zapatos():
    try:
        num_zapatos = int(input("Ingrese la cantidad de zapatos a comprar: "))
        precio_zapatos = 35
        total = num_zapatos * precio_zapatos
        
        if num_zapatos > 40:
            descuento = 0.40
        elif num_zapatos > 20 and num_zapatos < 25:
            descuento=0.20
        elif num_zapatos > 10:
            descuento=0.10
        else:
          descuento=0.0
        total_con_descuento= total * (1-descuento)
        print("El descuento aplicado es del {} porciento".format(int(descuento*100)))
        print(f"El total con descuento es: ${total_con_descuento:.2f}")
    except ValueError:
        print("Error: Por favor, ingrese un número valido.")
        
def supermercado():
    try:
        monto_compra = float(input("Ingrese el monto de la compra: "))
        tipo_membresia = input("Ingrese el tipo de membresía (A,B,C) ") .upper()
        if tipo_membresia == "A" and monto_compra > 100:
            descuento = 0.10
        elif tipo_membresia == "B" and monto_compra > 250:
            descuento= 0.15
        elif tipo_membresia == "C" and monto_compra > 320:
            descuento = 0.20
        else:
            descuento = 0.0
            
        total_con_descuento= monto_compra * (1-descuento)
        print(f"El total con descuento es: ${total_con_descuento:.2f}")
    except ValueError:
        print("Error: por favor, ingrese un monto válido.")
        
        
def despedida():
    print("Gracias por usar el programa. ¡Hasta Luego!")
    
def menu():
    while True: 
        print("\n--- Menú Principal ---")
        print("1. Presentación")
        print("2. Tienda de Zapatos")
        print("3. Supermercado")
        print("4. Despedida")
        
        try: 
            opcion =int(input("Seleccione una opción: "))
            
            if opcion == 1:
                presentacion()
            elif opcion == 2:
                tienda_zapatos()
            elif opcion == 3:
                supermercado()
            elif opcion == 4:
                despedida()
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

menu()