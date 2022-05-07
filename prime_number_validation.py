def validation(number):
    raiz_cuadrada= number ** 0.5
    raiz_cuadrada = int(raiz_cuadrada)
    contador = 0
    for i in range(1,raiz_cuadrada + 1):
        if number == 1:
            contador += 1
        elif i == number or i == 1:
            continue
        elif number % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False            


def run():
    numero = float(input("digita el numero que quieras para comprobar si es primo: "))
    if numero ==  0:
        print("no es un numero primo")
    elif validation(numero):
        print("si es un numero primo")
    else:
        print("no es un numero primo")    


if __name__ == "__main__":
    run()