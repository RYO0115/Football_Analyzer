
import matplotlib.pyplot as plt
from setPlayer import *

home = 0
away = 1

# for drawing court
#if __name__ == '__main__':
#    fig, ax = plt.subplots()
#    dc = DRAW_COURT(fig, ax)
#    dc.DrawCourt()
#    dc.Show()

# for drawing player formation
if __name__ == '__main__':
    fig, ax = plt.subplots()
    ps = PLAYER_SERVER(fig, ax)
    ps.SetFullMember()

    ps.teams[home].SetPlayerPosition("4231")
    ps.teams[away].SetPlayerPosition("442")
    ps.DrawPlayers()
    ps.Show()
