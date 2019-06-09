
import sys,os
import numpy as np
from drawFootballCourt import *

class HOME_AWAY():
    def __init__(self):
        self.Home = 0
        self.Away = 1

HA = HOME_AWAY()

COURT_SIZE = [72.5, 45]
POSITION_LIST = "positionName.json"

class PLAYER():
    def __init__(self):
        self.name = ""
        self.uniNum = 0
        self.x_pos = 0
        self.y_pos = 0
        self.playerID = 0
        self.pos = [0,0]
        self.circle = ""

    def SetPlayerPosition(self, x, y):
        self.x_pos = x
        self.y_pos = y


class TEAM():
    def __init__(self, homeAway):
        self.homeAwayDirection = homeAway
        if homeAway == HOME_AWAY().Home:
            self.homeAwayDirection = -1
        self.member = [PLAYER() for i in range(11)]
        dir = os.path.abspath(__file__)
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
                #self.member[memberIDNum].pos = [x,y]
                self.member[memberIDNum].SetPlayerPosition(x,y)
                memberIDNum += 1
            i += 1

    def ChangePlayerPosition(self, player_id, x_pos, y_pos):
        self.member[player_id].SetPlayerPosition(x_pos, y_pos)

    def GetPlayerPositionArray(sefl):
        pos_array = []
        for i in range(11):
            pos = [self.member[i].x_pos, self.member[i].y_pos]
            pos_array.append(pos)
        return pos

    def GetPlayerXPositionArray(self):
        x_array = []

        for i in range(11):
            x_array.append(self.homeAwayDirection * self.member[i].x_pos)

        return(x_array)

    def GetPlayerYPositionArray(self):
        y_array = []
        for i in range(11):
            y_array.append(self.homeAwayDirection * self.member[i].y_pos)

        return(y_array)

    def GetPlayerNumberArray(self):
        number_array = []
        for i in range(11):
            number_array.append(self.member[i].uniNum)

        return(number_array)

    def GetPlayerNameArray(self):
        name_array = []
        for i in range(11):
            name_array.append(self.member[i].name)
        return(name_array)

    def GetTeamColor(self):
        return(self.teamColor)




class PLAYER_SERVER():
    def __init__(self):
        self.SetFullMember()
    def SetFullMember(self):
        self.teams = []
        self.teams.append(TEAM(HOME_AWAY().Home))
        self.teams.append(TEAM(HOME_AWAY().Away))
        self.teams[0].teamColor="red"
        self.teams[1].teamColor="blue"

    def ChangeTeamColor(self, homeAway, color):
        self.teams[homeAway].teamColor = color


    def SetTeamFormation(self, homeAway, formation):
        self.teams[homeAway].SetPlayerPosition(formation)


    def ChangePlayerPosition(self, homeAway, player_id, x_pos, y_pos):
        self.teams[homeAway].ChangePlayerPosition(player_id,x_pos,y_pos)

    def GetTeamPlayerPositionArray(self, homeAway):
        return(self.teams[homeAway].GetPlayerPositionArray())

    def GetTeamPlayerXPositionArray(self, homeAway):
        return(self.teams[homeAway].GetPlayerXPositionArray())

    def GetTeamPlayerYPositionArray(self, homeAway):
        return(self.teams[homeAway].GetPlayerYPositionArray())

    def GetTeamPlayerUniNumberArray(self, homeAway):
        return(self.teams[homeAway].GetPlayerNumberArray())

    def GetTeamPlayerNameArray(self, homeAway):
        return(self.teams[homeAway].GetPlayerNameArray())

    def GetTeamColor(self, homeAway):
        return(self.teams[homeAway].GetTeamColor())








