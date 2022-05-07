import random


def run():
    numero_random = random.randint(1, 100)
    numero_usuario = int(input(input_message))
    vidas = 5
    while numero_usuario != numero_random:
        if numero_usuario < numero_random:
            print("el numero es mas grande")
        else:
            print("el numero es mas pequeño")
        numero_usuario = int(input("te quedan " + str(vidas) + " vidas, " + " intenta con otro numero: "))
        vidas -= 1    
        if vidas == 0:
            print("perdiste, intentalo de nuevo")
            break
    if numero_usuario == numero_random:
        print("felicidades, ganaste!")            
        

input_message = """
Hola, bienvenido a number guessing

a continuacion debes adivinar el numero del 1 al 100 que la cpu a pensado

tienes 5 vidas, una vez adivines el numero ya habras ganado

ahora digita el numero inicial: """


if __name__  == "__main__":
    run()