def main():
    black_list = ["Juan", "Maria", "Pedro"]
    # consejo: puedes utilizar el condicional "if in" para verificar si un nombre està en la lista negra. Aquì te dejo la documentaciòn por si no sabes còmo usarlo https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/


    # Escribe acà el còdigo, suerte :)
    nombre = input("Ingresa tu nombre: ")       
    if nombre in black_list:
        print("Lo siento, no puedes entrar. Estas en la lista negra.")
    else:
        edad = int(input("Ingresa tu edad: "))
        if edad < 18:
            print("Lo siento, no puedes entrar. Debes ser mayor de 18 años.")
        else:
            print("¡Bienvenido! Puedes entrar al bar.")
main() 