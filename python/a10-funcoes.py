# FUNÇÕES e MÉTODOS

# len() -> tamanho de uma lista (lenght)
lista = [1, 2, 3, 4, 5, 6, 7, 10, 8, 9]
print(len(lista))
print(lista[len(lista) - 1] )

# max() -> o maior valor de uma lista
maior = max(lista)
print(maior)

# min() -> retorna o menor valor de uma lista
print(min(lista))

# sum() -> soma todos os elementos numéricos de uma lista
print(sum(lista))

notas = [9, 5, 7]
notas.append(7)
notas.append(2)
print(sum(notas) // len(notas))

print()
print("linha")

nomes = ["Sofia", "Amanda", "Asdrúbal", "Luciana", "Amanda", "Amanda"]
nomes.append("Maria")
nomes.insert(1, "Edson")
print(nomes)

nomes[1] = "Parisotto"
print(nomes)

print()
contador = 1
while "Amanda" in nomes:
    nomes.remove("Amanda")
    print(f"{contador}: {nomes}")
    contador += 1
print(f"Acabou {contador}")

valorRemovido = nomes.pop(3)
print(valorRemovido)

indiceRemover = nomes.index("Parisotto")
print(nomes.pop(indiceRemover))
print(nomes)


