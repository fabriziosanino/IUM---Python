from random import seed
from random import randint

def createMatrix(rows, columns):
    seed()

    return [[randint(0, 1) for x in range(columns)] for y in range(rows)]


def createMatrixEmpty(rows, columns):
    return [[0 for x in range(columns)] for y in range(rows)]


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


def findPattern(patternMatrix, matrixToFindIn):
    for row in range(0, len(matrixToFindIn) + 1 - len(patternMatrix)):
        for column in range(0, len(matrixToFindIn[row]) + 1 - len(patternMatrix[0])):
            allTrue = False
            for i in range(0, len(patternMatrix)):
                for j in range(0, len(patternMatrix[0])):
                    if (patternMatrix[i][j] == 1) and ((matrixToFindIn[row + i][column + j] == patternMatrix[i][j]) or (
                            matrixToFindIn[row + i][column + j] == 5)):
                        allTrue = True
                    elif patternMatrix[i][j] == 0:
                        allTrue = True
                    else:
                        allTrue = False
                        break
                if (allTrue == False):
                    break

            if allTrue:
                for i in range(0, len(patternMatrix)):
                    for j in range(0, len(patternMatrix[0])):
                        if matrixToFindIn[row + i][column + j] == 1:
                            matrixToFindIn[row + i][column + j] = 5


def searchPattern(patternMatrixToTruncate, matrixToFindIn):
    maxM, maxN, minM, minN = truncatePattern(patternMatrixToTruncate)

    width = (maxN - minN) + 1  # gli indici partono da 0
    height = (maxM - minM) + 1

    patternMatrix = createPattern(patternMatrixToTruncate, width, height, minM, minN)

    findPattern(patternMatrix, matrixToFindIn)

    patternMatrix = rotateMatrix90Degree(patternMatrix)
    findPattern(patternMatrix, matrixToFindIn)

    patternMatrix = rotateMatrix90Degree(patternMatrix)
    findPattern(patternMatrix, matrixToFindIn)

    patternMatrix = rotateMatrix90Degree(patternMatrix)
    findPattern(patternMatrix, matrixToFindIn)

    return matrixToFindIn
    #printMatrix(matrixToFindIn)
