
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

from fileReader import *

import pandas as pd
from PIL import Image
import os

GRID_ROWS = 100
GRID_COLS = 100
#GRID_MERGIN = 1

#DataName Window Size
DATANAME_ROWS = int(GRID_ROWS * 0.8)
DATANAME_COLS = int(GRID_COLS * 0.3)

#ScoreTable Window Size
SCORETABLE_ROWS = int(GRID_ROWS * 0.2)
SCORETABLE_COLS = GRID_COLS
SCORE_COLS      = int(SCORETABLE_COLS * 0.4)


TEAMNAME_COLS  = int((SCORETABLE_COLS - SCORE_COLS)/2)

SCORETABLE_ROW_END = SCORETABLE_ROWS

HOMETEAMNAME_COL_END    = TEAMNAME_COLS
AWAYTEAMNAME_COL_START    = HOMETEAMNAME_COL_END + SCORE_COLS

SIDE_MERGIN     = int(0.1 * GRID_COLS)

#Team Stats Windows Size
STATS_ROW_START    = SCORETABLE_ROW_END
HOME_STATS_COL_END = int((GRID_COLS-DATANAME_COLS)/2)
AWAY_STATS_COL_START = int((GRID_COLS+DATANAME_COLS)/2)

gs_master = GridSpec(nrows=GRID_ROWS, ncols=GRID_ROWS)

#Score Board
gs_scoreboard   = GridSpecFromSubplotSpec(nrows=SCORETABLE_ROWS, ncols=SCORETABLE_COLS, subplot_spec=gs_master[:SCORETABLE_ROW_END, :])
gs_homeTeamName = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_scoreboard[1:, SIDE_MERGIN:HOMETEAMNAME_COL_END])
gs_awayTeamName = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_scoreboard[1:, AWAYTEAMNAME_COL_START:-SIDE_MERGIN])
gs_score        = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_scoreboard[1:, HOMETEAMNAME_COL_END:AWAYTEAMNAME_COL_START])
gs_date         = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_scoreboard[:1, HOMETEAMNAME_COL_END:AWAYTEAMNAME_COL_START])

# Stats Table
gs_dataname     = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_master[STATS_ROW_START:, HOME_STATS_COL_END:AWAY_STATS_COL_START])
gs_homelist     = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_master[STATS_ROW_START:,  :HOME_STATS_COL_END])
gs_awaylist     = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_master[STATS_ROW_START:, AWAY_STATS_COL_START:])


def IsStr(data):
    return(type(data) is str)

def GetFullSizeFigure():
    fig = plt.figure()
    fig.subplots_adjust(
        left=0.0,
        right=1.0,
        top=1.0,
        bottom=0.0
    )
    return(fig)

def DeleteSpines(ax):
    ax.tick_params(bottom=False,
                left=False,
                right=False,
                top=False)
    ax.spines["right"].set_color("none")  # 右消し
    ax.spines["left"].set_color("none")   # 左消し
    ax.spines["top"].set_color("none")    # 上消し
    ax.spines["bottom"].set_color("none")  # 下消し

def DeleteXTicks(ax):
    ax.set_xticks(ticks=[])

def DeleteYTicks(ax):
    ax.set_yticks(ticks=[])

def DeleteTicks(ax):
    DeleteXTicks(ax)
    DeleteYTicks(ax)

def DeleteAllOutlines(ax):
    DeleteSpines(ax)
    DeleteTicks(ax)

def Rounding(data):
    if data <= 4:
        return (0)
    else:
        return (1)

def RoundFloatToInt(data):
    s = str(data).split(".")
    newData = int(s[0])
    if len(s) > 1:
        newData += Rounding(int(s[1][0]))
    return(newData)



def GetDataNumAsLabel(dataList):
    label = dataList
    for i in range(len(dataList)):
        label[i] = str(RoundFloatToInt(dataList[i])).split(".")[0]
    return(label)

def GetDataWithoutNameAndScore(dataList):
    dataList = dataList.drop("TeamName")
    dataList = dataList.drop("Score")
    return(dataList)


def GetNormalizedDataList(dataList, maxList):
    if len(dataList) != len(maxList):
        return(dataList)

    normalizedDataList = []
    for i in range(len(dataList)):
        #normalizedDataList.append(dataList[i]/maxList[i]*100)
        data = dataList[i]/maxList[i] * 100
        if data > 100:
            data = 100
        normalizedDataList.append(data)

    return(normalizedDataList)

def WriteTextFromCenterOfAxes(ax, str, size=12, color="black"):
    ax.set_xlim([0,100])
    ax.set_ylim([0,100])
    ax.text( 50, 50, str, size=size, ha="center", va="center")



# Draws Horizontal Bar Graph
# data(row * col=["DataName","Home","Away"])
def DrawHorizontalBar( ax, data, labels = [], color="r"):
    left = np.arange(len(data))
    #labels = data["DataName"]

    height = 0.8

    ax.barh( left,  data, color=color, alpha = 0.6, height=height, align='center', tick_label=labels)
    label_pos = [ i for i in range(len(labels))]

    ax.set_yticks(label_pos)

def WriteDataName(ax, dataNameList, color="black", size=6):
    ax.set_xlim([0,100])
    ax.set_ylim([100,0])
    dataNum = len(dataNameList)
    space = 94 / dataNum
    x = 50
    y = space / 2
    for data in dataNameList:
        ax.text(x, y, data, size=size, ha="center", va="center")
        y += space


if __name__ == '__main__':
    dataArray = {   "Home": ["Arsenal", 2, 53.2, 10, 4, 2, 701, 87, 48],
                    "Away": ["Tottenham", 0, 46.8, 6, 3, 2, 350, 81, 58],
                    "Max":  ["None", 10, 100.0, 20, 20, 20, 1000, 100, 100]}

    data = pd.DataFrame( dataArray, index=[ "TeamName", "Score", "Possesion", "Shots", "Shots on Target", "Created Chance", "Passes", "Completed Passes", "Duels"] )

    fig = GetFullSizeFigure()
    #ax_scoreboard = fig.add_subplot(gs_scoreboard[:,:])

    ax_homeTeamName = fig.add_subplot(gs_homeTeamName[:,:])
    ax_awayTeamName = fig.add_subplot(gs_awayTeamName[:,:])
    ax_score        = fig.add_subplot(gs_score[:,:])
    ax_date         = fig.add_subplot(gs_date[:,:])
    DeleteAllOutlines(ax_homeTeamName)
    DeleteAllOutlines(ax_awayTeamName)
    DeleteAllOutlines(ax_score)
    DeleteAllOutlines(ax_date)

    teamNameId  = data.index.get_loc("TeamName")
    scoreId     = data.index.get_loc("Score")

    WriteTextFromCenterOfAxes( ax_homeTeamName, data["Home"].iloc[teamNameId], size=15)
    WriteTextFromCenterOfAxes( ax_awayTeamName, data["Away"].iloc[teamNameId], size=15)

    scoreStr = str(data["Home"].iloc[scoreId]) + " - " + str(data["Away"].iloc[scoreId])
    WriteTextFromCenterOfAxes( ax_score, scoreStr, size=24)


    # ------------- Stats Setting ------------
    ax_dataname = fig.add_subplot(gs_dataname[:,:])
    ax_home = fig.add_subplot(gs_homelist[:,:])
    ax_away = fig.add_subplot(gs_awaylist[:,:])

    ax_home.yaxis.tick_right()
    ax_home.set_xlim([100,0])
    ax_home.set_ylim([GetDataWithoutNameAndScore(data).shape[0],-0.5])

    ax_away.set_xlim([0,100])
    ax_away.set_ylim([GetDataWithoutNameAndScore(data).shape[0],-0.5])

    ax_dataname.set_ylim([GetDataWithoutNameAndScore(data).shape[0],-0.5])

    DeleteSpines(ax_home)
    DeleteSpines(ax_away)
    DeleteAllOutlines(ax_dataname)

    #DrawScoreBoard( ax_scoreboard)
    homeData    = GetDataWithoutNameAndScore(data["Home"]).values.tolist()
    awayData    = GetDataWithoutNameAndScore(data["Away"]).values.tolist()
    maxData     = GetDataWithoutNameAndScore(data["Max"]).values.tolist()
    indexData   = list(GetDataWithoutNameAndScore(data["Home"]).index)

    #normalizedHomeData =

    DrawHorizontalBar(  ax_home, GetNormalizedDataList(homeData, maxData), labels=GetDataNumAsLabel(homeData), color="r")
    DrawHorizontalBar(  ax_away, GetNormalizedDataList(awayData, maxData), labels=GetDataNumAsLabel(awayData), color="b")
    WriteDataName( ax_dataname, indexData, size=10)
    #DrawHorizontalBar(  ax_dataname, [], labels=indexData)
    DeleteXTicks(ax_home)
    DeleteXTicks(ax_away)
    DeleteAllOutlines(ax_dataname)

    imageDir = os.path.dirname(os.path.abspath(__file__)) + "/../../image/"
    home_im = Image.open(imageDir + "Arsenal_FC.png")
    away_im = Image.open(imageDir + "Tottenham_Hotspur.png")
    home_xlim = ax_home.get_xlim()
    home_ylim = ax_home.get_ylim()
    away_xlim = ax_away.get_xlim()
    away_ylim = ax_away.get_ylim()
    ax_home.imshow(home_im, extent=[*home_xlim, *home_ylim], aspect="auto", alpha = 0.5)
    ax_away.imshow(away_im, extent=[*away_xlim, *away_ylim], aspect="auto", alpha = 0.5)

    # ---------------------------------------------------------------- #

    plt.show()

