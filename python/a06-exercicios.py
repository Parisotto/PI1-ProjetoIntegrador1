# Faça um programa que imprima na tela a seguinte figura:
#
#     *
#    ***
#   *****
#  *******
# *********

x = 1
while x <= 5:
    # print((" " * (5 - x)) + ("*" * x) + ("*" * (x -1)))
    print((" " * (5 - x)), end="")
    print(("*" * x), end="")
    print(("*" * (x -1)))
    x += 1
    if x == 6:
        y = 1
        while y <= 3:
            print("   ***")
            y += 1

        print(" *******")

ast = 1
esp = 4
lin = 1
while lin <= 5:
    print( esp * " " + ast * "*")
    esp -= 1
    ast += 2
    lin += 1
    if lin == 6:
        y = 1
        while y <= 3:
            print("   ***")
            y += 1

        print(" *******")

x = 1
y = 4
while x <= 10:
    print( y * " " + x * "*")
    x += 2
    y -= 1