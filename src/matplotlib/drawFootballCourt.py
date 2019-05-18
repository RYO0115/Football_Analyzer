import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseEvent
import numpy as np

COURT_SIZE = [72.5, 45]

class DRAW_COURT():
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax

    def DrawCourt(self):
        self.ax.set_xlim( -COURT_SIZE[0], COURT_SIZE[0])
        self.ax.set_ylim( -COURT_SIZE[1], COURT_SIZE[1])
        self.ax.set_aspect("equal")
        self.fig.set_facecolor("white")
        self.ax.set_facecolor("green")
        self.ax.set_alpha(0.7)
        plt.tick_params(labelbottom=False,
                        labelleft=False,
                        labelright=False,
                        labeltop=False)
        self.DrawCourtCircle()
        self.DrawCourtLine()

    def DrawCourtCircle(self):
        #センターサークル
        circle = plt.Circle( xy=(0,0), radius=9.150, ec='w', fc='w', fill=False, zorder=1)
        self.ax.add_patch(circle)

        #ペナルティスポット
        circle = plt.Circle( xy=( 61.5, 0), radius=0.5, ec="k", fc="k", fill=True, zorder=1)
        self.ax.add_patch(circle)

        circle = plt.Circle( xy=(-61.5, 0), radius=0.5, ec="k", fc="k", fill=True, zorder=1)
        self.ax.add_patch(circle)

    def DrawPlayerCircle(self, x, y, color):
        circle = plt.Circle( xy=(x,y), radius=2, ec="w", fc=color, fill=True, zorder=2)
        self.ax.add_patch(circle)
        return circle


    def DrawCourtLine(self):
        #センターライン
        self.DrawLine( 0, 0,-COURT_SIZE[1], COURT_SIZE[1], zo=1)

        #ゴールエリア
        self.DrawLine( 67.0, 67.0,-9.16, 9.16, zo=1)
        self.DrawLine(-67.0,-67.0,-9.16, 9.16, zo=1)
        self.DrawLine( 67.0, COURT_SIZE[0], 9.16, 9.16, zo=1)
        self.DrawLine( 67.0, COURT_SIZE[0],-9.16,-9.16, zo=1)
        self.DrawLine(-67.0,-COURT_SIZE[0], 9.16, 9.16, zo=1)
        self.DrawLine(-67.0,-COURT_SIZE[0],-9.16,-9.16, zo=1)

        #ペナルティエリア
        self.DrawLine( 56.0, 56.0,-20.16, 20.16, zo=1)
        self.DrawLine(-56.0,-56.0,-20.16, 20.16, zo=1)
        self.DrawLine( 56.0, COURT_SIZE[0], 20.16, 20.16, zo=1)
        self.DrawLine( 56.0, COURT_SIZE[0],-20.16,-20.16, zo=1)
        self.DrawLine(-56.0,-COURT_SIZE[0], 20.16, 20.16, zo=1)
        self.DrawLine(-56.0,-COURT_SIZE[0],-20.16,-20.16, zo=1)


    def DrawLine(self, x1, x2, y1, y2, color="w-", zo=3):
        line = plt.plot([x1,x2],[y1,y2],color,lw=2, zorder=zo)


    def Show(self):
        plt.show()


