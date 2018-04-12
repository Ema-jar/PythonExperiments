import Tkinter as tk


main_window = tk.Tk()
val = 0


#-- creo una textarea dentro una finestra
#text = tk.Text(main_window)
#text.grid()

#-- creo un pulsante dentro una finestra
def clicked():
    global val
    val += 1
    print "I've been clicked " + str(val) + " times!"

def close():
    main_window.quit()

buttonClick = tk.Button(main_window, text='Click me!', command=clicked)
buttonClick.grid()

buttonClose = tk.Button(main_window, text="Close me!", command=close)
buttonClose.grid()

tk.mainloop()
