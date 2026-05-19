linhas = 5
i = 1

while i <= linhas:
    # espaços à esquerda
    espacos = linhas - i
    while espacos > 0:
        print(" ", end="")
        espacos -= 1

    # asteriscos
    estrelas = 2 * i - 1
    while estrelas > 0:
        print("*", end="")
        estrelas -= 1

    print()  # quebra de linha
    i += 1