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
    while numero2 == 0:
        print ("Não é possível realizar divisão por zero.")
        numero2 = float(input("Digite um número diferente de zero: "))
        resultado = numero1 / numero2
else:
    resultado = "Erro! Operador inválido!"


print (resultado)