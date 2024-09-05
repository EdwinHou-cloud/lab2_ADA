from math import log
salida=False
while not salida:
    print('(1) valor acumulado')
    print('(2) Depósito mensual')
    print('(3) Número de depósitos')
    print('(4) Salir')
    opc = input('Elija una opción: ')
    if opc=='1':
        p=float(input('valor del depósito mensual:'))
        n=int(input('número depósitos mensuales:'))
        x=float(input('Interés anual en porcentaje:'))
        m=0.01*x/12
        a=p*((1+m)**n-1)/m
        print('valor acumulado:',a)
    elif opc=='2':
        a=float(input('valor acumulado:'))
        n=int(input('número depósitos mensuales:'))
        x=float(input('Interés anual en porcentaje:'))
        m=0.01*x/12
        p=a*m/((1+m)**n-1)
        print('cuota mensual:', p)
    elif opc=='3':
        a=float(input('valor acumulado:'))
        p=float(input('valor del depósito mensual:'))
        x=float(input('Interés anual en porcentaje:'))
        m=0.01*x/12
        n=log (a*m/p+1)/log(1+m)
        print('Numero de depósitos:', n)
    elif opc=='4':
        salida=True
