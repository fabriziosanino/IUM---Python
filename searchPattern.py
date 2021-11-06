from random import seed
from random import randint
from termcolor import colored

pattern = [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]


def createMatrix(rows, columns):
    seed(1)

    return [[randint(0, 1) for x in range(columns)] for y in range(rows)]


def createMatrixEmpty(rows, columns):
    return [[0 for x in range(columns)] for y in range(rows)]


def printMatrix(matrix):
    for row in range(0, len(matrix)):
        val = ""
        for column in range(0, len(matrix[0])):
            if matrix[row][column] == 5:
                val += colored(str(matrix[row][column]), "green") + " "
            else:
                val += str(matrix[row][column]) + " "
        print(val)


def truncatePattern(matrix):
    maxM = maxN = 0
    minM = minN = float('inf')
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[row])):
            if matrix[row][column] == 1:
                if column < minN:
                    minN = column
                if column > maxN:
                    maxN = column
                if row < minM:
                    minM = row
                if row > maxM:
                    maxM = row

    return maxM, maxN, minM, minN


def createPattern(matrix, width, heigth, minM, minN):
    mat = createMatrixEmpty(heigth, width)

    for rows in range(0, heigth):
        for columns in range(0, width):
            mat[rows][columns] = matrix[rows + minM][columns + minN]

    return mat


def rotateMatrix90Degree(matrix):  # senso anti orario di 90 gradi
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]
    #                                    |                           |
    #                                    ----------------------------->matrix[0] in quando l'altezza diventa come la grandezza e viceversa.


def findPattern(patternMatrix, matrixToFindIn, height, width):
    for row in range(0, len(matrixToFindIn) + 1 - height):
        for column in range(0, len(matrixToFindIn[row]) + 1 - width):
            allTrue = False
            for i in range(0, height):
                for j in range(0, width):
                    if ((matrixToFindIn[row + i][column + j] == patternMatrix[i][j]) or (
                            matrixToFindIn[row + i][column + j] == 5 and patternMatrix[i][j] == 1)):
                        allTrue = True
                    else:
                        allTrue = False
                        break
                if (allTrue == False):
                    break

            if allTrue:
                for i in range(0, height):
                    for j in range(0, width):
                        if matrixToFindIn[row + i][column + j] == 1:
                            matrixToFindIn[row + i][column + j] = 5


def searchPattern(patternMatrixToTruncate, matrixToFindIn):
    maxM, maxN, minM, minN = truncatePattern(patternMatrixToTruncate)

    width = (maxN - minN) + 1  # gli indici partono da 0
    height = (maxM - minM) + 1

    patternMatrix = createPattern(patternMatrixToTruncate, width, height, minM, minN)

    findPattern(patternMatrix, matrixToFindIn, height, width)

    patternMatrix = rotateMatrix90Degree(patternMatrix)
    findPattern(patternMatrix, matrixToFindIn, width, height)

    patternMatrix = rotateMatrix90Degree(patternMatrix)
    findPattern(patternMatrix, matrixToFindIn, width, height)

    patternMatrix = rotateMatrix90Degree(patternMatrix)
    findPattern(patternMatrix, matrixToFindIn, width, height)

    printMatrix(matrixToFindIn)
