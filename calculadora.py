numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador desejado (+, -, *, /)")

if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    resultado = numero1 / numero2
else:
    resultado = "Erro! Operador inválido!"


print (resultado)