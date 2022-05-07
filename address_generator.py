import random


def generator():
    letters= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    characters = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    definitive_list = letters + numbers + characters + letters_lower
    contraseña_return = []
    for i in range(15):
        chosen = random.choice(definitive_list)
        contraseña_return.append(chosen)
    address = "".join(contraseña_return)
    return address    


def run():
    contraseña = generator()
    print("tu nueva contraseña es " + str(contraseña))


if __name__ == "__main__":
    run()