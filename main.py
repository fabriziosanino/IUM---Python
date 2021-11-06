from tkinter import *
from searchPattern import *

window = Tk()
window.title("IUM find Patterns")

rows = 4
columns = 4

boxes = []
boxVars = []

# Create all IntVars, set to 0

if __name__ == '__main__':
    matrixToFindIn = createMatrix(30, 30)
    printMatrix(matrixToFindIn)

    patternMatrix = createMatrixEmpty(rows, columns)

    print("Start...")

for i in range(rows):
    boxVars.append([])
    for j in range(columns):
        boxVars[i].append(IntVar())
        boxVars[i][j].set(0)


def checkRow(i):
    global boxVars, boxes
    row = boxVars[i]
    deselected = []

    for j in range(len(row)):
        if row[j].get() == 0:
            deselected.append(j)


def printMat():
    for i in range(len(boxVars)):
        temp = []
        for j in range(len(boxVars[i])):
            patternMatrix[i][j] = boxVars[i][j].get()

    searchPattern(patternMatrix, matrixToFindIn)


for x in range(rows):
    boxes.append([])
    for y in range(columns):
        boxes[x].append(Checkbutton(window, variable=boxVars[x][y], command=lambda x=x: checkRow(x)))
        boxes[x][y].grid(row=x + 1, column=y + 1)

b = Button(window, text="Find pattern", command=printMat, width=10)
b.grid(row=12)
mainloop()
