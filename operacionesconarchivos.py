import os

nombre_archivo = "registro.txt"

while True:
    print("MENU")
    print("1. crear archivo")
    print("2. guardar registros")
    print("3. leer archivo")
    print("4. actualizar nombre")
    print("5. cerrar")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        archivo = open(nombre_archivo, "w")
        archivo.write("NOMBRE:\n")
        archivo.write("MATRICULA:\n")
        archivo.write("CORREO:\n")
        archivo.write("TELEFONO:\n")
        archivo.close()
        print("Archivo creado\n")

    elif opcion == "2":
        archivo = open(nombre_archivo, "w")
        nombre = input("Ingresa nombre: ")
        matricula = input("Ingresa matricula: ")
        correo = input("Ingresa correo: ")
        telefono = input("Ingresa telefono: ")

        archivo.write("NOMBRE: " + nombre + "\n")
        archivo.write("MATRICULA: " + matricula + "\n")
        archivo.write("CORREO: " + correo + "\n")
        archivo.write("TELEFONO: " + telefono + "\n")
        archivo.close()
        print("Datos guardados\n")

    elif opcion == "3":
        if os.path.exists(nombre_archivo):
            archivo = open(nombre_archivo, "r")
            print("\nContenido del archivo:")
            print(archivo.read())
            archivo.close()
        else:
            print("El archivo no existe\n")

    elif opcion == "4":
        if os.path.exists(nombre_archivo):
            archivo = open(nombre_archivo, "r")
            lineas = archivo.readlines()
            archivo.close()

            buscar = input("Nombre que deseas cambiar: ")
            nuevo = input("Nuevo nombre: ")

            archivo = open(nombre_archivo, "w")
            for linea in lineas:
                if "NOMBRE:" in linea and buscar in linea:
                    archivo.write("NOMBRE: " + nuevo + "\n")
                else:
                    archivo.write(linea)
            archivo.close()

            print("Nombre actualizado\n")
        else:
            print("El archivo no existe\n")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida\n")
