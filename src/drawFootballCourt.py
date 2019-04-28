import matplotlib.pyplot as plt
import numpy as np


class DRAW_COURT():
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax

    def DrawCourt(self):
        self.ax.set_xlim( -72.5, 72.5)
        self.ax.set_ylim( -34, 34)
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
        circle = plt.Circle( xy=(0,0), radius=9.150, ec='w', fc='w', fill=False)
        self.ax.add_patch(circle)

        #ペナルティスポット
        circle = plt.Circle( xy=( 61.5, 0), radius=0.5, ec="k", fc="k", fill=True)
        self.ax.add_patch(circle)
        circle = plt.Circle( xy=(-61.5, 0), radius=0.5, ec="k", fc="k", fill=True)
        self.ax.add_patch(circle)

    def DrawCourtLine(self):
        #センターライン
        self.DrawLine( 0, 0,-34, 34)

        #ゴールエリア
        self.DrawLine( 67, 67,-9.16, 9.16)
        self.DrawLine(-67,-67,-9.16, 9.16)
        self.DrawLine( 67, 72.5, 9.16, 9.16)
        self.DrawLine( 67, 72.5,-9.16,-9.16)
        self.DrawLine(-67,-72.5, 9.16, 9.16)
        self.DrawLine(-67,-72.5,-9.16,-9.16)

        #ペナルティエリア
        self.DrawLine( 56,   56,-20.16, 20.16)
        self.DrawLine(-56,  -56,-20.16, 20.16)
        self.DrawLine( 56, 72.5, 20.16, 20.16)
        self.DrawLine( 56, 72.5,-20.16,-20.16)
        self.DrawLine(-56,-72.5, 20.16, 20.16)
        self.DrawLine(-56,-72.5,-20.16,-20.16)


    def DrawLine(self, x1, x2, y1, y2, color="w-"):
        line = plt.plot([x1,x2],[y1,y2],color,lw=2)
        #self.ax.add_patch(line)


    def Show(self):
        plt.show()


