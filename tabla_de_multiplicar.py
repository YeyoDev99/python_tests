def tabla_calculo(numero):
    for tabla in range(11):
        numero = int(numero)
        tabla= int(tabla)
        calculo = numero * tabla
        numero = str(numero)
        tabla= str(tabla)
        calculo= str(calculo)
        print(numero + " por " + tabla + " es igual a " + calculo)


def run():
    numero_tabla = int(input("digita el numero que quieras y te enseñaremos su tabla de multiplicación: "))
    tabla_calculo(numero_tabla)
        

if __name__ == "__main__":
    run()