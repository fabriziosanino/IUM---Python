# Press the green button in the gutter to run the script.
from searchPattern import *
from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
mainloop()


if __name__ == '__main__':
    matrix = createMatrix()
    printMatrix(pattern)
