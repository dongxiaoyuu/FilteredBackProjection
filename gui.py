from tkinter.filedialog import askopenfilename
from tkinter import *

root = Tk()
root.withdraw()
root.update()
imagename = askopenfilename()  # get the picture file abstract path
root.destroy()
