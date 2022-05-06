def run():
    LIMITE = 10000000
    exponente = 0
    numero_expuesto = 2**exponente
    while numero_expuesto < LIMITE:
        print("2 potenciado a " + str(exponente) + " es igual a " + str(numero_expuesto))
        exponente = exponente + 1
        numero_expuesto = 2**exponente


if __name__ == "__main__":
    run()