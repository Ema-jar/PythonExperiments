import Tkinter as tk
import ttk

main_window = tk.Tk()


tree = ttk.Treeview(main_window)
ysb = ttk.Scrollbar(main_window, orient='vertical', command=tree.yview)
xsb = ttk.Scrollbar(main_window, orient='horizontal', command=tree.xview)
tree.configure(yscroll=ysb.set, xscroll=xsb.set)
tree.heading('#0', text="esempio", anchor='w')


first = tree.insert('', 'end', text="ciao", open=False)
second = tree.insert(first, 'end', text="ciao2", open=True)

def OnClick(event):
    print "ciao"
tree.bind('<<TreeviewSelect>>', OnClick)


tree.grid(row=0, column=0)
ysb.grid(row=0, column=1, sticky='ns')
xsb.grid(row=1, column=0, sticky='ew')
tree.grid()

tk.mainloop()