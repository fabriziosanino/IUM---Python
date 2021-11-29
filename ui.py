import tkinter.font as tkFont
import tkinter as tk
from tkinter import messagebox
import searchPattern

def checkRow(arg):
    boxVars = arg['box']
    i = arg['row']
    row = boxVars[i]
    deselected = []

    for j in range(len(row)):
        if row[j].get() == 0:
            deselected.append(j)

def find(arg):
    patternMatrix = arg['pattern']
    matrixToFindIn = arg['matrix']
    buttonList = arg['list']
    boxVars = arg['box']
    findOne = False
    for i in range(len(boxVars)):
        for j in range(len(boxVars[i])):
            if boxVars[i][j].get() == 1:
                findOne = True
            patternMatrix[i][j] = boxVars[i][j].get()

    if not findOne:
        tk.messagebox.showerror("Errore", "Hai inserito un pattern vuoto!")
    else:
        matrixToFindIn = searchPattern.searchPattern(patternMatrix, matrixToFindIn)
        printResult(matrixToFindIn, buttonList)

def createUi(root, boxVars, patternMatrix, matrixToFindIn):
    #setting title
    root.title("PROGETTO Python")
    #setting window size
    width=800
    height=700
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    lblTitoloProgetto=tk.Label(root)
    ft = tkFont.Font(family='Times',size=20)
    lblTitoloProgetto["font"] = ft
    lblTitoloProgetto["fg"] = "#333333"
    lblTitoloProgetto["justify"] = "center"
    lblTitoloProgetto["text"] = "PROGETTO IUM"
    lblTitoloProgetto.place(x=10,y=10,width=580,height=30)

    lblInserisciPattern=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    lblInserisciPattern["font"] = ft
    lblInserisciPattern["fg"] = "#333333"
    lblInserisciPattern["justify"] = "center"
    lblInserisciPattern["text"] = "Inserisci il pattern da cercare"
    lblInserisciPattern.place(x=0,y=90,width=202,height=31)

    for row in range(len(patternMatrix)):
        for column in range(len(patternMatrix[0])):
            checkbox = tk.Checkbutton(root)
            ft = tkFont.Font(family='Times', size=10)
            checkbox["font"] = ft
            checkbox["fg"] = "#333333"
            checkbox["justify"] = "center"
            checkbox["text"] = ""
            checkbox.place(x=50 + (20 * column), y=120 + (20 * row), width=30, height=30)
            checkbox["variable"] = boxVars[row][column]
            checkbox["command"] = lambda arg={'row':row, 'box': boxVars}: checkRow(arg)

    startX = 360 - (len(matrixToFindIn[0]) / 2) * 20
    buttonList = [[0 for x in range(len(matrixToFindIn))] for y in range(len(matrixToFindIn[0]))]
    for row in range(len(matrixToFindIn)):
        for column in range(len(matrixToFindIn[0])):
            button = tk.Button(root)
            button["bg"] = "#efefef",
            ft = tkFont.Font(family='Times', size=10)
            button["font"] = ft
            button["fg"] = "#333333"
            button["justify"] = "center"
            button["text"] = matrixToFindIn[row][column]
            button["state"] = "disabled"
            button.place(x= startX + (20 * column), y= 210 + (20 * row) , width=20, height=20)
            buttonList[row][column] = button

    btnFind = tk.Button(root)
    btnFind["bg"] = "#efefef"
    ft = tkFont.Font(family='Times', size=10)
    btnFind["font"] = ft
    btnFind["fg"] = "#333333"
    btnFind["justify"] = "center"
    btnFind["text"] = "Cerca"
    btnFind.place(x=210, y = 90, width=70, height=25)
    btnFind["command"] = lambda arg = {'pattern': patternMatrix, 'matrix': matrixToFindIn, 'box': boxVars, 'list': buttonList}: find(arg)

    root.mainloop()

def printResult(matrix, buttonList):
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[0])):
            if matrix[row][column] == 5:
                buttonList[row][column].configure(bg = "#7CFC00")
