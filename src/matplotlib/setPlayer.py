
import sys,os
import numpy as np
from drawFootballCourt import *



COURT_SIZE = [72.5, 45]
POSITION_LIST = "positionName.json"

class PLAYER():
    def __init__(self):
        self.name = ""
        self.uniNum = 0
        self.playerPos = ""
        self.playerID = 0
        self.pos = [0,0]
        self.circle = ""

class TEAM():
    def __init__(self, homeAway):
        self.homeAway = homeAway
        self.member = [PLAYER() for i in range(11)]
        dir = os.path.abspath(__file__)
        #self.positionList = json.loads(dir[:-len("setPlayer.py")] + "positionName.json")
        self.SetPlayerPosition("4231")
        self.teamColor = ""

    def SetPlayerPosition(self, formation):
        lineMemberNum = []
        lineMemberNum.append(1)
        for i in range(len(formation)):
            lineMemberNum.append(int(formation[i]))

        #コートの端からペナルティスポットまでを引いたもの
        verticalLength  = COURT_SIZE[0] - 6.0
        verticalRes     = (verticalLength-5) / (len(lineMemberNum)-1)

        horizontalLength = COURT_SIZE[1] * 2

        i = 0
        memberIDNum = 0
        for memberNum in lineMemberNum:
            horizontalRes = horizontalLength / (memberNum+1)
            x = verticalLength - verticalRes * i
            for j in range(memberNum):
                y = COURT_SIZE[1] - horizontalRes * (j+1)
                self.member[memberIDNum].pos = [x,y]
                memberIDNum += 1
            i += 1


class PLAYER_SERVER():
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        self.dc = DRAW_COURT(fig, ax)
        self.dc.DrawCourt()

    def SetFullMember(self):
        self.teams = []
        self.teams.append(TEAM("home"))
        self.teams.append(TEAM("away"))

        self.teams[0].teamColor="red"
        self.teams[1].teamColor="blue"

    def DrawPlayers(self):
        for team in self.teams:
            for member in team.member:
                x = member.pos[0]
                y = member.pos[1]
                if(team.homeAway=="home"):
                    x *= -1
                    y *= -1
                member.circle = self.dc.DrawPlayerCircle(x,y,team.teamColor)

    #def ChangeFormation(self):




    def Show(self):
        self.dc.Show()




