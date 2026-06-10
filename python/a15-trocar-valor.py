# Faça um código que receba 2 números inteiros positivos e
# imprima os 2 usando o seguinte comando:

#   print(f"O n1 é {n1} e o n2 é {n2}")

# Em seguida inverta os valores de n1 e n2 e imprima novamente
# já com os números invertidos

# Exemplos de saída: Se n1 for 7 e n2 for 19:
# Primeiro print: O n1 é 7 e o n2 é 19
# Segundo print: O n é 19 e o n2 é 7

n1 = input("Digite um número inteiro positivo: ")
n2 = input("Digite outro número inteiro positivo: ")
print(f"O n1 é {n1} e o n2 é {n2}")

auxiliar = n1
n1 = n2
n2 = auxiliar
print(f"O n1 é {n1} e o n2 é {n2}")


