import Tkinter as tk
from PIL import Image


def open_img():
    print "entered"
    img = Image.open("panda.jpg")
    img.show()

main_window = tk.Tk()
button = tk.Button(main_window, text="Open img", command=open_img)
button.grid()

tk.mainloop()