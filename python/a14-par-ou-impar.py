# Faça um código que peça um inteiro ao usuário e imprima no terminal se o número é par ou impar

while True:
    numero = int(input("Digite um número inteiro: "))
    par_ou_impar = numero % 2
    if par_ou_impar == 0:
        print(f"O número {numero} é par!")
    else:
        print(f"O número {numero} é impar!")
    c = input("Deseja continuar? [s/n] ")
    if c == "n":
        break

print("Programa finalizado com sucesso!")

# Crie um código que peça dois número inteiros, um de cada vez,
# e mostre o maior deles.
# Exemplo:
# n1 = 4
# n2 = 9
# O maior é 9

numero1 = int(input("Digite um inteiro: "))
numero2 = int(input("Digite outro inteiro: "))
if numero1 > numero2:
    print(f"O maior é o número {numero1}!")
else:
    print(f"O maior é o número {numero2}!")





