# Laço de repetição while

x = 1
while x <= 5:
    print(x)
    x += 1

x = 1
while True:
    print(x)
    x -= 2
    if x < -100:
        break

linha = 1
while linha <= 5:
    coluna = 1
    while coluna <= linha:
        print("*", end=" ")
        coluna += 1
    print()
    linha += 1

print(f"Linha: {linha}")
print(f"Coluna: {coluna}")


print("\nFIM")