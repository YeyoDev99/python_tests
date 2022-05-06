# conversion de dollares a pesos

dollar_value = input("digita el valor en dolares que quieres convertir a pesos: ")
dollar_value = float(dollar_value)
valor_peso_en_dolar = 0.0002580645
dollar_to_pesos_calculation = dollar_value / valor_peso_en_dolar
dollar_to_pesos_calculation = round(dollar_to_pesos_calculation, 2)
dollar_to_pesos_calculation = str(dollar_to_pesos_calculation)
print("el valor es de $" + dollar_to_pesos_calculation + " pesos colombianos")