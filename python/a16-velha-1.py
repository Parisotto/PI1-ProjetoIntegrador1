v = [
    ' ',' ',' ',
    ' ',' ',' ',
    ' ',' ',' ']

linha = 1
i = 0
while linha <= 5:
    if linha % 2 == 0:
        print("---|---|---")
    else:
        print(f" {v[i]} | {v[i+1]} | {v[i+2]} ")
        i += 3

    linha += 1

