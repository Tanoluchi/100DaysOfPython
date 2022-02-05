from operator import le
import random
from arte_ahorcado import stages, logo, gameover
from lista_palabras import list_words

random_word = random.choice(list_words)
hidden_word = []
letter_entered = []
lives = 6

for _ in range(len(random_word)):
    hidden_word += "_"

print(logo)

while True:
    # Verificamos si aun le quedan vidas, y si ya no hay guiones bajos en nuestra lista, si no se encuentra más significa que se descubrio la palabra.
    if lives > 0 and "_" in hidden_word:
        incorrect = True
        # Pedimos al usuario que ingrese una letra.
        while incorrect:
            chossen_letter = str.lower(input("Ingresa una letra: "))
            # Si el string ingresado por el usuario tiene una longitud mayor a 1 no es una letra.
            if len(chossen_letter) > 1:
                print(f"\nLo lamento {chossen_letter} no es una letra. Ingresa una letra para poder continuar!.")
            else:
                incorrect = False
                
        if not chossen_letter in letter_entered:
            # Añadimos la letra ingresada a una lista para luego verificar que no vuelva a ingresar la misma letra.
            letter_entered += chossen_letter
            # Verificamos si en la palabra se encuentra la letra.
            if random_word.find(chossen_letter) != -1:
                # Buscamos la posiciones en la que se encuentra la letra.
                positions = [pos for pos, char in enumerate(random_word) if char == chossen_letter]
                # Reemplazamos los guiones bajos en las posiciones donde se encuentra la letra.
                for pos in positions:
                    hidden_word[pos] = chossen_letter
                    
                discovered_word = str()   
                for letter in hidden_word:
                    discovered_word += letter
                print("\n" + discovered_word)
            else:
                print(f"{stages[lives]}")
                print(f"La letra {chossen_letter} no se encuentra en la palabra.")
                lives -= 1
        else:
            print(f"\nLo lamento, la letra '{chossen_letter}' ya fue ingresada anteriormente. Por favor ingresa una nueva letra. ")
    elif lives == 0:
        print(f"{stages[lives]}")
        print(f"{gameover}")
        print(f"\nLamentablemente has perdido!\nLa palabra era: {random_word}")
        break
    elif not "_" in hidden_word:
        print(f"\nFelicidades has ganado!\nLa palabra es: {random_word}")
        break
