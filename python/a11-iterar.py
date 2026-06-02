def funcao():
    listaNacoes = ["Brasil",'EUA','China','Canada','Inglaterra','EUA']

    for pais in listaNacoes:
        print(f"{pais}", end=", ")

    print()
    for caracter in "Projeto Integrador 1":
        print(caracter, end='')



    for menina in meninas:
        print(menina)
        for nome in menina:
            print(nome)

    # Range:
    for i in range(5):
        print(i)

    print("-------")
    for i in range(0,9):
        print(i)

    print("-------")
    for i in range(5, 17, 2):
        print(i)
print()
meninas = [
    ['Amelia', 'Ana Paula', 'Alice'],
    ['Gabrielle','Sarah','Thuanna','Marina'],
    ['Sofia','Tamires']
]
print(meninas[1][2])