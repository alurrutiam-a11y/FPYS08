def menu():
    print("menu programa")
    print("1.sumar")
    print("2.restar")
    print("3.saludar")
    print("4.salir")
    
    opcion = int(input("ingrese una opcion:"))
    if opcion == 1:
        print(">>> sumando")

    elif opcion == 2:
        print(">>> restando")

    elif opcion == 3:
        print(">>> saludando")

    elif opcion == 4:
        print(">>> saliendo")
        break
    else:
        print("opcion invalida (1,4)")

menu()