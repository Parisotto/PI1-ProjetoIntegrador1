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

x = 1
while x <= 3:
    print("   ***")
    x += 1

print(" *******")