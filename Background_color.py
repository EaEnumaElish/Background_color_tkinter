from tkinter import *
import colorsys

main = Tk()
main.title('Light spectre color control panel')
main.eval('tk::PlaceWindow . center')
main.geometry("700x500")
main.configure(background=('#000000000'))
main.resizable(False, False)

mainFrame = Frame(main)
mainFrame.pack(side=TOP)


def rgb_to_hex(r, g, b):
    return '#%02X%02X%02X' % (r, g, b)


def change_color(event):
    tuple = colorsys.hsv_to_rgb(var_R.get(), 1, var_Alpha.get())
    r, g, b = tuple
    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)
    main.configure(background=rgb_to_hex(r, g, b))


var_R = DoubleVar()
var_Alpha = DoubleVar()

Label(mainFrame, text='Set please value').pack(side=TOP)
Label(mainFrame, text='Set color').pack(side=LEFT)
scale_R = Scale(mainFrame, showvalue=0, variable=var_R, from_=0.01,
                to=0.88, resolution=0.01, orient=HORIZONTAL, command=change_color).pack(side=LEFT)

Label(mainFrame, text='Set window alpha').pack(side=LEFT)
scale_Alpha = Scale(mainFrame, showvalue=0, variable=var_Alpha, from_=0, to=1,
                    orient=HORIZONTAL, resolution=0.01, command=change_color).pack(side=LEFT)

main.mainloop()
