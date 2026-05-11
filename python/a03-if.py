# Controle de fluxo condicional 'if'

print("INÍCIO\n")

habilitado = False
print(habilitado)

habilitado = input("Você está habilitado?: ")

if habilitado == "sim":
    print("Habilitado")
    print("Pode dirigir e fazer barbaridades a vontade.")
    habilitado = True

print(habilitado)

if habilitado == "sim":
    print("Plenamente Habilitado")
else:
    print("Largue este volante, irresponsável!")

media = 0
if media >= 6:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
elif media >= 4:
    print("Trabalho de recuperação")
else:
    print("Reprovado")

if habilitado:
    if media >= 6:
        print("Teste")
    else:
        print("Não teste")
else:
    print("Não habilitado")

print("\nFIM")
