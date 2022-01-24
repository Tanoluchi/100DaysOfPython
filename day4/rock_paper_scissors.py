from platform import machine
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

arr = [rock, paper, scissors]
user_choice = arr[int(input("¿Que vas elegir? Escribe 0 para piedra, 1 para papel o 2 para tijeras.\n===> "))]
machine_choice = random.choice(arr)

if user_choice == rock:
    if machine_choice == scissors:
        print(f"Su elección fue la de piedra\n{user_choice}")
        print(f"La eleccion de la maquina fue la de tijeras\n{machine_choice}")
        print("Usted ha ganado!")
    elif machine_choice == paper:
        print(f"Su elección fue la de piedra\n{user_choice}")
        print(f"La eleccion de la maquina fue la de papel\n{machine_choice}")
        print("Usted ha perdido!")
    else:
        print(f"Su elección fue la de piedra\n{user_choice}")
        print(f"La eleccion de la maquina fue la de piedra\n{machine_choice}")
        print("Es un empate!")
elif user_choice == paper:
    if machine_choice == rock:
        print(f"Su elección fue la de papel\n{user_choice}")
        print(f"La eleccion de la maquina fue la de piedra\n{machine_choice}")
        print("Usted ha ganado!")
    elif machine_choice == paper:
        print(f"Su elección fue la de papel\n{user_choice}")
        print(f"La eleccion de la maquina fue la de papel\n{machine_choice}")
        print("Es un empate!")
    else:
        print(f"Su elección fue la de papel\n{user_choice}")
        print(f"La eleccion de la maquina fue la de tijeras\n{machine_choice}")
        print("Usted ha perdido!")
else:
    if machine_choice == rock:
        print(f"Su elección fue la de tijeras\n{user_choice}")
        print(f"La eleccion de la maquina fue la de piedra\n{machine_choice}")
        print("Usted ha perdido!")
    elif machine_choice == paper:
        print(f"Su elección fue la de tijeras\n{user_choice}")
        print(f"La eleccion de la maquina fue la de papel\n{machine_choice}")
        print("Usted ha ganado!")
    else:
        print(f"Su elección fue la de tijeras\n{user_choice}")
        print(f"La eleccion de la maquina fue la de tijeras\n{machine_choice}")
        print("Es un empate!")
