from tkinter import *
from searchPattern import *

rows = 4
columns = 4

def printMat():
    for i in range(len(boxVars)):
        for j in range(len(boxVars[i])):
            patternMatrix[i][j] = boxVars[i][j].get()

    searchPattern(patternMatrix, matrixToFindIn)

def checkRow(i):
    global boxVars, boxes
    row = boxVars[i]
    deselected = []

    for j in range(len(row)):
        if row[j].get() == 0:
            deselected.append(j)

if __name__ == '__main__':
    window = Tk()
    window.title("IUM find Patterns")
    b = Button(window, text = "Find pattern", command = printMat, width=10)

    boxes = []
    boxVars = []

    for i in range(rows):
        boxVars.append([])
        for j in range(columns):
            boxVars[i].append(IntVar())
            boxVars[i][j].set(0)

    for x in range(rows):
        boxes.append([])
        for y in range(columns):
            boxes[x].append(Checkbutton(window, variable=boxVars[x][y], command=lambda x=x: checkRow(x)))
            boxes[x][y].grid(row=x + 1, column=y + 1)

    b.grid(row=12)

    matrixToFindIn = createMatrix(5, 5)

    patternMatrix = createMatrixEmpty(rows, columns)

    print("Start...")

    mainloop()

