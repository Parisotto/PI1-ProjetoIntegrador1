# faça um código que imprima a seguinte figura:
#    |   |
# ---|---|---
#    |   |
# ---|---|---
#    |   |

#print("   |   |   ")
#print("---|---|---")
#print("   |   |   ")
#print("---|---|---")
#print("   |   |   ")

i = 1
c = 1
while i <= 5:
    if i % 2 == 1:
        print(f" {c} | {c+1} | {c+2} ")
        c += 3
    else:
        print("---|---|---")
    i += 1

