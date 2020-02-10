
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
#from setPlayer import *
from setMouseControl import *

home = 0
away = 1

gs_master = GridSpec(nrows=GRID_ROWS, ncols=GRID_ROWS)
gs_main = GridSpecFromSubplotSpec(nrows=16, ncols=12, subplot_spec=gs_master[-14:-2, 4:16])
gs_homelist = GridSpecFromSubplotSpec(nrows=2, ncols=16, subplot_spec=gs_master[4:,  :2])
gs_awaylist = GridSpecFromSubplotSpec(nrows=2, ncols=16, subplot_spec=gs_master[4:, -2:])

# for drawing player formation
if __name__ == '__main__':
    fig = plt.figure(figsize=(12,10))

    ax = fig.add_subplot(gs_main[:,:])
    GUI =  GUI_CONTROL(fig, ax)
    fig.canvas.mpl_connect('button_press_event',   GUI._on_click)
    fig.canvas.mpl_connect('button_release_event', GUI._on_release)
    fig.canvas.mpl_connect('motion_notify_event',  GUI._on_motion)

    plt.show()
