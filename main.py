from tkinter import *
from searchPattern import *

if __name__ == '__main__':
    matrix = createMatrix()

window = Tk()
window.title("IUM find Patterns")

M = 4
N = 4

boxes = []
boxVars = []

# Create all IntVars, set to 0

for i in range(M):
    boxVars.append([])
    for j in range(N):
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
                matrix[i][j]= boxVars[i][j].get()
    printMatrix(matrix)


for x in range(M):
    boxes.append([])
    for y in range(N):
        boxes[x].append(Checkbutton(window, variable = boxVars[x][y], command = lambda x = x: checkRow(x)))
        boxes[x][y].grid(row=x+1, column=y+1)

b = Button(window, text = "Find patterns", command = printMat, width = 10)
b.grid(row = 12)
mainloop()

