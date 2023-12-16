def main():
    black_list = ["Juan", "Maria", "Pedro"]
    # consejo: puedes utilizar el condicional "if in" para verificar si un nombre està en la lista negra. Aquì te dejo la documentaciòn por si no sabes còmo usarlo https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/


    # Escribe acà el còdigo, suerte :)
    verificados = []

    while True:
        print("1. Editar lista negra.")
        print("2. Ver lista negra.")
        print("3. Verificar entrada.")
        print("4. Ver personas verificadas.")
        print("5. Número de personas que han entrado al bar")
        print("6. Terminar")
        accion = int(input("Ingrese el número de la accion que desea realizar: "))

        if accion == 1:
            edit = int(input("1. Agregar, 2. Eliminar: "))
            name = input("Nombre: ")
            if edit == 1:
                black_list.append(name)
            elif edit == 2:
                black_list.remove(name)

        elif accion == 2:
            print(black_list)
        
        elif accion == 3:
            nombre = input("Ingresa tu nombre: ")
            verificados.append(nombre)               
            if nombre in black_list:
                print("Lo siento, no puedes entrar. Estas en la lista negra.")
            else:
                edad = int(input("Ingresa tu edad: "))
                if edad < 18:
                    print("Lo siento, no puedes entrar. Debes ser mayor de 18 años.")
                else:
                    print("¡Bienvenido! Puedes entrar al bar.")

        elif accion == 4:
            print(verificados)

        elif accion == 5:
            print(len(verificados))

        elif accion == 6:
            break

main() 