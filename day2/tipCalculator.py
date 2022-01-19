print("¡Bienvenido a la calculadora de propinas!")

# Input
check = float(input("¿Cuál fue la factura total?\n==> "))
tip = int(input("\n¿Cuánta propina te gustaría dar? (10, 12 o 15?)\n==> "))
amountPeoples = int(input("\n¿Cuántas personas son para dividir la cuenta?\n==> "))

# Output
print(f"\nCada persona debe pagar: {(check / amountPeoples) * ((check / 100) + 1)}")