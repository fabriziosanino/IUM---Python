import tkinter as tk
from searchPattern import *
import ui

rowsPattern = 10
columnsPattern = 10

rowsFind = 10
columnsFind = 10

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

    ui.createStaticUi(root)

    ui.createDynamicUi(root, boxVars, patternMatrix, matrixToFindIn)


