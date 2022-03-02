alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text: str, shift: int):    
    """Funcion que toma el mensaje a cifrar y los desplazamientos de las letras.
    Al finalizar se muestra por pantalla el texto cifrado.

    Args:
        plain_text (str): mensaje a cifrar
        shift (int): desplazamientos a realizar en el alfabeto
    """
    cipher_text = str()
    
    for letter in plain_text:
        if letter == " ":
            cipher_text += letter
        else:
            pos = alphabet.index(letter) + shift
            cipher_text += alphabet[pos]
        
    print(f"The enconded text is {cipher_text}")

def decrypt(cipher_text: str, shift: int):
    """Funcion que toma un mensaje cifrado y los desplazamientos de las letras.
    Al finalizar se muestra por pantalla el texto descifrado.

    Args:
        cipher_text (str): texto cifrado
        shift (int): desplamientos a realizar en el alfabeto
    """
    plain_text = str()
    
    for letter in cipher_text:
        if letter == " ":
            plain_text += " "
        else:
            pos = alphabet.index(letter) - shift
            plain_text += alphabet[pos]
        
    print(f"The decoded text is {plain_text}")


def request_data():
    """Pedimos los datos al usuario y verificamos si necesita cifrar o descifrar un mensaje.
    """
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == 'encode':
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            encrypt(text, shift)
            stop = input("Do you want to continue entering data? (True or false):\n").lower()
            if stop == "false":
                exit()
        elif direction == 'decode':
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            decrypt(text, shift)
            stop = input("Do you want to continue entering data? (True or false):\n").lower()
            if stop == "false":
                exit()
        else:
            print("Sorry, that function was not found. Try again!")

request_data()