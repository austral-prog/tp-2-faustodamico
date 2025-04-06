def change():
    expense = 23.75
    money = 100
    vuelto = money - expense

    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print("""Ingresar gasto:23.75
          Dinero recibido
          100""")

    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
