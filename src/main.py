
from setPlayer import *

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ps = PLAYER_SERVER(fig, ax)
    ps.SetFullMember()
    ps.teams[0].SetPlayerPosition("4231")
    ps.teams[1].SetPlayerPosition("343")
    ps.DrawPlayers()
    ps.Show()
