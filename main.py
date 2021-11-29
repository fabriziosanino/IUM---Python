import tkinter as tk
from searchPattern import *
import ui

rowsPattern = 4
columnsPattern = 4

rowsFind = 20
columnsFind = 20

if __name__ == '__main__':
    root = tk.Tk()

    boxes = []
    boxVars = []

    for i in range(rowsPattern):
        boxVars.append([])
        for j in range(columnsPattern):
            boxVars[i].append(tk.IntVar())
            boxVars[i][j].set(0)

    matrixToFindIn = createMatrix(rowsFind, columnsFind)

    patternMatrix = createMatrixEmpty(rowsPattern, columnsPattern)

    app = ui.createUi(root, boxVars, patternMatrix, matrixToFindIn)


