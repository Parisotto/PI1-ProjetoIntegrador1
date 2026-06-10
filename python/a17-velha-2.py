v = [
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' ']

def malha():
    linha = 1
    i = 0
    while linha <= 5:
        if linha % 2 == 0:
            print("---|---|---")
        else:
            print(f" {v[i]} | {v[i + 1]} | {v[i + 2]} ")
            i += 3

        linha += 1

def velha():
    if (
        (v[0] != ' ' and v[0] == v[1] == v[2]) or
        (v[3] != ' ' and v[3] == v[4] == v[5]) or
        (v[6] != ' ' and v[6] == v[7] == v[8]) or
        (v[0] != ' ' and v[0] == v[3] == v[6]) or
        (v[1] != ' ' and v[1] == v[4] == v[7]) or
        (v[2] != ' ' and v[2] == v[8] == v[9]) or
        (v[0] != ' ' and v[0] == v[4] == v[8]) or
        (v[2] != ' ' and v[2] == v[4] == v[6])
    ):
        return True

    return False

malha()

m = "X"
i = 0
while i < 9:
    lance = int(input(f"{m}: Escolha uma casa livre de 1 a 9: "))
    if v[lance-1] == ' ':
        v[lance-1] = m
        if velha():
            msg = f"VELHA! Deu {m}"
            break
        elif m == "X":
            m = "0"
        else:
            m = "X"
        i += 1
    malha()

print("\nGAME OVER!")