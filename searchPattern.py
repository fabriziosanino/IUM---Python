from random import seed
from random import randint


M = 4
N = 4

pattern = [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]

def createMatrix():
    seed(1)

    matrix = [[randint(0, 1) for x in range(M)] for y in range(N)] 
    return matrix


def printMatrix(matrix):
    for row in range(0, M):
        val = ""
        for column in range(0, N):
            val += str(matrix[row][column]) + " "
        print(val)
