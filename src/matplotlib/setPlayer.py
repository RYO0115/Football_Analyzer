
import sys,os
import math
import numpy as np

from DrawFootballCourt import *
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d, delaunay_plot_2d


COURT_SIZE = [72.5, 45]
POSITION_LIST = "positionName.json"

class PLAYER():
    def __init__(self):
        self.homeAway = None
        self.name = ""
        self.uniNum = 0
        self.playerPos = ""
        self.playerID = 0
        self.pos = [0,0]
        self.circle = None

    def UpdatePlayerPosition(self):
        a = 1.0
        if self.homeAway == "home":
            a = -1.0

        x_0  = self.pos[0]
        y_0  = self.pos[1]
        x, y = self.circle.center
        x *= a
        y *= a

        distance = math.sqrt(pow(x - x_0,2) + pow(y - y_0, 2))
        if distance > 1.0:
            self.pos[0] = x
            self.pos[1] = y

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
                self.member[memberIDNum].homeAway = self.homeAway
                memberIDNum += 1
            i += 1

    def GetMemberPositions(self):
        points = []
        for i in range(len(self.member)):
            point = self.member[i].pos
            points.append(point)
        return(points)

    def DrawDelaunay(self):
        points = self.GetMemberPositions()
        self.delaunay = Delaunay(points)
        return(self.delaunay)

    def DrawVolonoi(self):
        points = self.GetMemberPositions()
        self.voronoi = Voronoi(points)
        return(self.voronoi)



class DrawMemberList():
    def __init__(self, ax):
        self.ax = ax




class PLAYER_SERVER():
    def __init__(self, ax):
        #self.fig = fig
        self.ax = ax
        self.dc = DRAW_COURT(ax)
        self.dc.DrawCourt()

    def SetFullMember(self):
        self.teams = []
        self.teams.append(TEAM("home"))
        self.teams.append(TEAM("away"))

        self.teams[0].teamColor="red"
        self.teams[1].teamColor="blue"

        self.delaunay = []
        self.volonoi = []

    def DrawPlayers(self):
        players = []
        for team in self.teams:
            #for member in team.member:
            for i in range(len(team.member)):
                x = team.member[i].pos[0]
                y = team.member[i].pos[1]
                if(team.member[i].homeAway == "home"):
                    x *= -1
                    y *= -1
                team.member[i].circle = self.dc.DrawPlayerCircle(x,y,team.teamColor)
                players.append(team.member[i])
        return players

    def ResetLines(self):
        self.lines = []

    def CreateDelaunay(self, homeAway):
        delaunay = []
        for team in self.teams:
            delaunay.append(team.DrawDelaunay())

        return(delaunay)

    def CreateVolonoi(self):
        volonoi = []
        for team in self.teams:
            volonoi.append(team.DrawVolonoi())
        return(volonoi)

    def DrawDelaunay(self, delaunay):
        delaunay_plot_2d(delaunay, self.ax)

    def DrawVolonoi(self, voronoi):
        voronoi_plot_2d(voronoi, self,ax)

    def ChangeFormation(self, homeAway, formation):
        self.teams[homeAway].SetPlayerPosition(formation)


    def Show(self):
        self.dc.Show()




