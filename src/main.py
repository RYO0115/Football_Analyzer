
from setPlayer import *

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ps = PLAYER_SERVER(fig, ax)
    ps.SetFullMember()
    ps.DrawPlayers()
    ps.Show()
