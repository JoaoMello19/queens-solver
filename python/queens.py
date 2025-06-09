import itertools


def compareCoords(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 and (x1 != x2 or y1 != y2)


def getBasicCombinations(length=8):
    if length <= 0:
        return []

    RANGE = list(range(length))
    rows = RANGE[:]

    for permuted_columns in itertools.permutations(RANGE):
        combination = []
        for i in RANGE:
            combination.append((rows[i], permuted_columns[i]))
        yield combination


def filterByProximity(combinations):
    length = len(combinations[0])
    for combs in combinations:
        isCloser = False
        for i in range(length):
            for j in range(i + 1, length):
                if compareCoords(combs[i], combs[j]):
                    isCloser = True
                    break
            if isCloser:
                break
        
        if not isCloser:
            yield combs
            

def filterByColor(table, combinations):
    for combination in combinations:
        colors = set([table[x][y]['color'] for x, y in combination])
        if len(colors) == len(table):   # todas as cores diferentes
            yield combination


def bruteForce1(table):
    combinations = getBasicCombinations(len(table))     # combinacoes de colunas/linhas diferentes
    combinations = filterByProximity(combinations)      # combinacoes sem proximidade
    combinations = filterByColor(table, combinations)   # combinacoes com cores diferentes
    
    for combination in combinations:
        print(combination)
    
    return "OK"