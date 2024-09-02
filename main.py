import random


def miniAhorcado():
    while True:
        print("\nAdivina la palabra secreta!")
        palabras = ["casa", "carro", "perro", "gato", "zorro", "sapo", "caspa", "arma"]
        palabraSecreta = random.choice(palabras)
        intentos = 4
        palabraAdivinada = False

        cantLetras = len(palabraSecreta)
        print(f"Cantidad de letras: {cantLetras}: " + ("_" * cantLetras))
        print(f"Intentos: {intentos}")
        while not palabraAdivinada and intentos > 0:
            palabra = input("\nIngrese una palabra: ")

            if palabra == palabraSecreta:
                print(f"\nLa palabra '{palabra}' es la correcta")
                palabraAdivinada = True
            else:
                intentos -= 1
                if intentos == 3:
                    print(f"La palabra '{palabra}' no es la correcta.")
                    print(f"Te quedan '{intentos}' intentos.")
                    letra = palabraSecreta[0]
                    print(f"Pista! La primera letra es: {letra}\n")
                elif intentos == 2:
                    print(f"La palabra '{palabra}' no es la correcta.")
                    print(f"Te quedan '{intentos}' intentos.")
                    letra = palabraSecreta[1]
                    print(f"Pista! La segunda letra es: {letra}\n")

        if intentos == 0:
            print(f"¡Perdiste! La palabra secreta era: {palabraSecreta}")
        while True:
            repetirPartida = input("¿Nueva partida? s/n: ").lower()
            if repetirPartida == "":
                continue
            elif repetirPartida not in "sn":
                continue
            else:
                break
        if repetirPartida[0] == "s":
            continue
        else:
            break

def encuentraNumero():
    while True:
        numRandom = random.randint(1,101)
        print("\nDescubre cual es el número secreto del 1 al 100")
        intentos = 0

        while True:
            num = int(input("Ingresa un número: "))
            if num == numRandom:
                print(f"\nMuy bien! Encontraste el número '{numRandom}' en {intentos + 1} intentos.")
                break
            elif num > numRandom:
                print("\nEl número es menor.")
                intentos += 1
            else:
                print("\nEl número es mayor")
                intentos += 1
        while True:
            repetirPartida = input("¿Nueva partida? s/n: ").lower()
            if repetirPartida == "":
                continue
            elif repetirPartida not in "sn":
                continue
            else:
                break
        if repetirPartida[0] == "s":
            continue
        else:
            break

def ahorcado():
    while True:
        print("\nAhorcado")
        palabrasAsar = ["casa","capa", "computador", 
        "calculadora", "moto", "perro", "pajaro", "mancha"]
        palabraSecreta = random.choice(palabrasAsar)
        palabra = []
        intentos = 5
        for letra in palabraSecreta:
            palabra.append("_")

        while True:
            print(f"\nIntentos restantes: {intentos}")
            print(f"Cantidad de letras: {len(palabraSecreta)}\n" + "".join(palabra))
            while True:
                letraUsuario = input("\nIngresa un letra: ").lower()
                if letraUsuario != "":
                    letraIn = letraUsuario[0]
                    break
                
            if letraIn in palabraSecreta:
                i = 0
                for letra in palabraSecreta:
                    if letraIn == palabraSecreta[i]:
                        palabra[i] = letraIn
                    i += 1
            else:
                 intentos -= 1
                 print(f"la letra '{letraIn}' no está!")     

            strListaPalabra = "".join(palabra)

            if palabraSecreta == strListaPalabra:
                print(f"\n¡Felicitaciones! Descubriste la palabra secreta. '{palabraSecreta}'\n")
                break
            
            if intentos == 0: 
                print("\n¡Perdiste! Te quedaste sin intentos.\n")
                break
        while True:
            repetirPartida = input("¿Nueva partida? s/n: ").lower()
            if repetirPartida == "":
                continue
            elif repetirPartida not in "sn":
                continue
            else:
                break
        if repetirPartida[0] == "s":
            continue
        else:
            break          

print("Esto es una prueba de conocimiento python")

while True:
    nombre = input("Ingresa un nombre: ").strip()
    if nombre == "":
        continue
    else:
        print(f"\nBienvenido {nombre}!")
        break


while True:
    print("\nElige un juego:\n")
    print("1. Mini Ahorcado\n2. Encuentra El Número\n3. Ahorcado\n4. Salir")

    opcion = int(input("\nPon el número del juego que quieres: "))
    if opcion == 1:
        miniAhorcado()
    elif opcion == 2:
        encuentraNumero()
    elif opcion == 3:
        ahorcado()
    elif opcion == 4:
        print("¡Adios!")
        break
    else:
        print("No pusiste la opción correcta!")
