import os
from tkinter.filedialog import askopenfilename
from tkinter import *


root = Tk()
root.withdraw()
root.update()
imagename = askopenfilename()
root.destroy()


imagename = os.path.split(imagename)[-1]
