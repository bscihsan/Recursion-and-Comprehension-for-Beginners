import sys


def printDiamonds(index, howMany):
    if index < howMany:
        print(' ' * (howMany - index + 1) + '*' * (2 * index - 1))
    elif index < 2 * howMany:
        print(' ' * (index - howMany + 1) + '*' * (2 * (2 * howMany - index) - 1))
    else:
        return
    return printDiamonds(index + 1, howMany)

printDiamonds(1, int(sys.argv[1]))  # The program printed diamond using recursion.

diamond = [('*' + '**'*i).center(2*int(sys.argv[1]) + 1) for i in range(int(sys.argv[1]))]
print("\n".join(diamond + diamond[::-1][1:]))  # The program printed diamond using comprehension.