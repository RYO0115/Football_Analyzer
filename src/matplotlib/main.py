
import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
#from SetPlayer import *
from SetMouseControl import *

home = 0
away = 1

GRID_ROWS = 20
GRID_COLS = 20

gs_master = GridSpec(nrows=GRID_ROWS, ncols=GRID_ROWS)
gs_main = GridSpecFromSubplotSpec(nrows=16, ncols=12, subplot_spec=gs_master[-14:-2, 4:16])
#gs_homelist = GridSpecFromSubplotSpec(nrows=2, ncols=16, subplot_spec=gs_master[4:,  :2])
#gs_awaylist = GridSpecFromSubplotSpec(nrows=2, ncols=16, subplot_spec=gs_master[4:, -2:])

root = tkinter.Tk()
root.wm_title("Football Analyzer")
root.geometry("800x450")

def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


# for drawing player formation
if __name__ == '__main__':


    fig = plt.figure()

    ax = fig.add_subplot(gs_main[:,:])
    GUI =  FORMATION(fig, ax)

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.mpl_connect('button_press_event',   GUI._on_click)
    canvas.mpl_connect('button_release_event', GUI._on_release)
    canvas.mpl_connect('motion_notify_event',  GUI._on_motion)
    canvas.mpl_connect("key_press_event", on_key_press)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()

    button = tkinter.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tkinter.BOTTOM)

    tkinter.mainloop()
    #plt.show()
