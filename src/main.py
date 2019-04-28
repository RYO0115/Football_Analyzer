
from drawFootballCourt import *

if __name__ == '__main__':
    fig, ax = plt.subplots()
    dc = DRAW_COURT(fig, ax)
    dc.DrawCourt()
    dc.Show()
