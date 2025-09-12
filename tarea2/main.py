from biblioteca import Biblioteca

def main():
    b = Biblioteca() #mal nombre de variable

    while True:
        print("\n=== MENÚ BIBLIOTECA ===")
        print("1. Agregar libro")
        print("2. Generar reporte")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1": #aqui se puede utilizar un switch
            b.agregar_libro()
        elif opcion == "2":
            b.generar_reporte()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
