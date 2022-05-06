def polindromo_validacion(word):
    word = word.replace(" ", "")
    word = word.lower()
    word_backwards = word[::-1]
    if word_backwards == word:
        return True
    else:
        return False    


def run():
    palabra_usuario = input("por favor escribe una palabra para saber si es un polindromo: ")
    validacion = polindromo_validacion(palabra_usuario)
    if validacion == True:
        print("si es un polindromo")
    else:
        print("no es un polindromo")    


if __name__ == "__main__":
    run()