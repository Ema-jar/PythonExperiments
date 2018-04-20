from Tkinter import *
import ttk


main_window = Tk()


def compute(inputString):
    print "Input is " + inputString


content = ttk.Frame(main_window, padding=(3, 3, 12, 12))
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)
compute = ttk.Button(content, text="Compute", command=compute)
separator = ttk.Separator(content, orient=HORIZONTAL)
output_text = Text(content)



content.grid(column=1, row=0, sticky=(N, S, E, W))
namelbl.grid(column=0, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=0, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
compute.grid(column=0, row=2, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
separator.grid(column=0, row=3, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
output_text.grid(column=0, row=3, columnspan=2)

main_window.mainloop()
