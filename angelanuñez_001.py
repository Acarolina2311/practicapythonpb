'''
1) cambiar la linea 1 y que se ingrese el saldo inicial en el teclado
2) cambiar el nombre de la variable saldo por saldoInicial
'''
saldoInicial=1000

while True:
    print("\n--- Cajero Automatico---")
    print("1. Condultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Seleccionar una opción: ")
    
    if opcion =="1":
        print(f"tu saldo actual es: S/. {saldoInicial}")
    elif opcion == "2":
        monto == float(input("ingrese el monto a depositar: "))
        if monto>0:
            #saldo+=monto
            saldo=saldoInicial+monto
            print(f"Has depositado S/.{monto}. Saldo Actual: S/.{saldo}")
        else:
            print("monto invalido")
    elif opcion == "3":
        monto=float(input=("ingresa monto a retirar: "))
        if 0 < monto <= saldo:
            #saldo-=monto
            saldo= saldoInicial-monto
            print(f"has retirado S/.{monto}. Saldo actual es: S/. {saldo}")
        else:
            print("monto invalido o saldo insuficiente")
    elif opcion =="4":
        print ("Gracias por usar el cajero. ¡Hasta luego!")
        break
    else:
        print("Opeción no válida. Intenta de nuevo.")
print("======FINALIZÓ EL PROGRAMA ======")