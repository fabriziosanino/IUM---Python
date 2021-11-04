from random import seed
from random import randint

pattern = [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]


def createMatrix(rows, columns):
    seed(1)

    return [[randint(0, 1) for x in range(rows)] for y in range(columns)]


def createMatrixEmpty(rows, columns):
    return [[0 for x in range(rows)] for y in range(columns)]


def printMatrix(matrix, rows, columns):
    for row in range(0, rows):
        val = ""
        for column in range(0, columns):
            val += str(matrix[row][column]) + " "
        print(val)


def truncatePattern(matrix):
    maxM = maxN = 0
    minM = minN = float('inf')
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[row])):
            if (matrix[row][column] == 1):
                if (column < minN):
                    minN = column
                elif (column > maxN):
                    maxN = column
                if (row < minM):
                    minM = row
                elif (row > maxM):
                    maxM = row

    return maxM, maxN, minM, minN


def createPattern(matrix, width, heigth, minM, minN):
    mat = createMatrixEmpty(heigth, width)

    for rows in range(0, heigth):
        for columns in range(0, width):
            mat[rows][columns] = matrix[rows + minM][columns + minN]

    return mat


def searchPattern(patternMatrixToTruncate, matrixToFindIn):
    maxM, maxN, minM, minN = truncatePattern(patternMatrixToTruncate)
    print("MIN e MAX", minM, maxM, minN, maxN)

    width = (maxN - minN) + 1  # gli indici partono da 0
    height = (maxM - minM) + 1

    print("WIDTH e HEIGHT", width, height)

    patternMatrix = createPattern(patternMatrixToTruncate, width, height, minM, minN)

    printMatrix(patternMatrix, height, width)

    count = 0
    for row in range(0, len(matrixToFindIn) - height):
        for column in range(0, len(matrixToFindIn[row]) - width):
            allTrue = True
            for i in range(0, height):
                for j in range(0, width):
                    if(matrixToFindIn[row + i][column + j] == patternMatrix[i][j]):
                        allTrue = True
                    elif(patternMatrix[i][j] == 1 and matrixToFindIn[row + i][column + j] == 5):
                        allTrue = True
                    else:
                        allTrue = False

            if(allTrue):
                count += 1


    print("")
    print("Corrispondenze: ", count)
    print("")
    printMatrix(matrixToFindIn, len(matrixToFindIn), len(matrixToFindIn[0]))
