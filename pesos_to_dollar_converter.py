# conversion de pesos a dolares
def pesos_a_dolares_funcion(tipo_pesos, dolar_a_pesos):
    pesos_colombianos = input("digita los pesos " + tipo_pesos + " que quieres convertir en dolares: ")
    pesos_colombianos = float(pesos_colombianos)
    calculo_pesos_a_dolar = pesos_colombianos / dolar_a_pesos
    calculo_pesos_a_dolar = round(calculo_pesos_a_dolar, 5)
    calculo_pesos_a_dolar = str(calculo_pesos_a_dolar)
    print("el valor es de $" + calculo_pesos_a_dolar + " dolares")

menu = """
Bienvenido a money converter 😊,

las opciones de peso latinoamericano son:

1- pesos colombianos
2- pesos argentinos
3- pesos mexicanos

porfavor digite el numero de la opcion de los pesos que quieres convertir a dolar: """

pesos_option= int(input(menu))

if pesos_option == 1:
        pesos_a_dolares_funcion("colombianos", 3875)

elif pesos_option == 2:
        pesos_a_dolares_funcion("argentinos", 65)
elif pesos_option == 3:
        pesos_a_dolares_funcion("mexicanos", 24)
else:
    print("porfavor escribe un numero de opcion valido")


