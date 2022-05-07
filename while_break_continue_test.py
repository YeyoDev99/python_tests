
def run():
    LIMITE = 500
    contador = 0
    result_operation = contador * 3
    while result_operation < LIMITE:
        contador += 1
        result_operation = contador * 3
        if result_operation % 2 != 0:
            continue  
        print(result_operation)      


if __name__ == "__main__":
     run()

# def run():
#     LIMITE = 1000
#     numero = 0
#     operacion = 3 + numero
#     print(operacion)
#     while operacion < LIMITE:
#         numero += 1
#         operacion = 3 + numero
#         if operacion > 500:
#             break
#         print(operacion)



# if __name__ == "__main__":
#     run()