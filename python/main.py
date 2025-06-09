from queens import *

def readTable():
    table = []
    with open('input.txt', 'r') as f:
        for line in f:
            row = []
            for color in line.strip().split():
                row.append({'color': color, 'queen': False})
            table.append(row)
    return table


table = readTable()
# print(table)

print(bruteForce1(table))