
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as path_effects

from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

from fileReader import *
from plt_common import *

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
gs_homeEmblem = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_scoreboard[:, SIDE_MERGIN:HOMETEAMNAME_COL_END])
gs_awayEmblem = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_scoreboard[:, AWAYTEAMNAME_COL_START:-SIDE_MERGIN])

gs_homeTeamName = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_scoreboard[1:, SIDE_MERGIN:HOMETEAMNAME_COL_END])
gs_awayTeamName = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_scoreboard[1:, AWAYTEAMNAME_COL_START:-SIDE_MERGIN])
gs_score        = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_scoreboard[1:, HOMETEAMNAME_COL_END:AWAYTEAMNAME_COL_START])
gs_date         = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_scoreboard[:1, HOMETEAMNAME_COL_END:AWAYTEAMNAME_COL_START])

# Stats Table
gs_dataname     = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_master[STATS_ROW_START:, HOME_STATS_COL_END:AWAY_STATS_COL_START])
# No Compare Version
gs_homelist     = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_master[STATS_ROW_START:,  SIDE_MERGIN:HOME_STATS_COL_END])
gs_awaylist     = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_master[STATS_ROW_START:, AWAY_STATS_COL_START:-SIDE_MERGIN])

# Comparing Version
gs_comparelist  = GridSpecFromSubplotSpec(nrows=1, ncols=1, subplot_spec=gs_master[STATS_ROW_START:,  SIDE_MERGIN:-SIDE_MERGIN])



def IsStr(data):
    return(type(data) is str)


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

def GetNormalizedDataList(pdDataList):
    for i in range(len(pdDataList.index)):
        for j in range(len(pdDataList.columns)):
            pdDataList[pdDataList.columns[j]][i] /= pdDataList["Max"][i]

    return(pdDataList)


# Draws Horizontal Bar Graph
# data(row * col=["DataName","Home","Away"])
def DrawHorizontalBar( ax, data, labels = [], color="r"):
    left = np.arange(len(data))
    #labels = data["DataName"]

    height = 0.8

    ax.barh( left,  data, color=color, alpha = 0.6, height=height, align='center', tick_label=labels)
    label_pos = [ i for i in range(len(labels))]

    ax.set_yticks(label_pos)

def CreateDominantColorList( homeData, awayData):
    colorList = [[],[]]
    if len(homeData) != len(awayData):
        return(colorList)

    for i in range(len(homeData)):
        if homeData[i] > awayData[i]:
            colorList[0].append(0.8)
            colorList[1].append(0.3)
        elif homeData[i] < awayData[i]:
            colorList[0].append(0.3)
            colorList[1].append(0.8)
        else:
            colorList[0].append(0.5)
            colorList[1].append(0.5)

    return(colorList)

def DrawComparingHorizontalBar( ax, data, leftEnd_data, labels = [], color = [], alpha = []):
    x_array = np.arange(len(data))
    bar_list = ax.barh( x_array, data, left=leftEnd_data, edgecolor="White", linewidth=0.8, tick_label=labels, alpha = 0.8)

    for j in range(len(color)):
        bar_list[j].set_facecolor(color[j])

    for j in range(len(alpha)):
        bar_list[j].set_alpha(alpha[j])

    leftEnd_data += data

    return(leftEnd_data)

def DrawStatsWithComparingHorizontalBar(ax, pdDataList):
    homeAway_color = {"Home":"red", "Away":"blue"}
    #dominant_color = {"Big":"Blue", "small":"glay"}

    labels = pdDataList.index.to_list()
    leftEnd_data = pd.Series(np.zeros(len(pdDataList.index)), index=labels)
    for i in range(len(pdDataList.columns)):
        if pdDataList.columns[i] != "Max":
            color = [homeAway_color[pdDataList.columns[i]] for j in range(len(pdDataList.index))]
            alpha = CreateDominantColorList(pdDataList["Home"].values.tolist(), pdDataList["Away"].values.tolist())
            #leftEnd_data = DrawComparingHorizontalBar(ax, pdDataList[pdDataList.columns[i]], leftEnd_data, labels = labels, color=color)
            #leftEnd_data = DrawComparingHorizontalBar(ax, pdDataList[pdDataList.columns[i]], leftEnd_data, labels = labels, alpha=alpha[i])
            leftEnd_data = DrawComparingHorizontalBar(ax, pdDataList[pdDataList.columns[i]], leftEnd_data, labels = labels, color=color, alpha=alpha[i])



def WriteDataName(ax, dataNameList, color="black", size=6, pos="center"):
    ax.set_xlim([0,100])
    ax.set_ylim([100,0])
    dataNum = len(dataNameList)
    space = 94 / dataNum
    x = 50
    if pos == "top":
        y = 0
    elif pos == "bottom":
        y = space
    else:
        y = space/2

    y = space / 2
    for data in dataNameList:
        text = ax.text(x, y, data, size=size, ha="center", va="center", color=color)
        text.set_path_effects([path_effects.SimpleLineShadow(), path_effects.Normal()])
        y += space


if __name__ == '__main__':
    dataArray = {   "Home": ["Arsenal", 2, 53.2, 10, 4, 2, 701, 87, 48],
                    "Away": ["Tottenham", 0, 46.8, 6, 3, 2, 350, 81, 58]}
                    #"Max":  ["None", 10, 100.0, 20, 20, 20, 1000, 100, 100]}
    data = pd.DataFrame( dataArray, index=[ "TeamName", "Score", "Possesion", "Shots", "Shots on Target", "Created Chances", "Passes", "Completed Passes", "Duels"] )

    fig = GetFullSizeFigure()
    ax_backimage = fig.add_subplot(1,1,1)
    backImageDir = os.path.dirname(os.path.abspath(__file__)) + "/../../image/backimage/"
    back_im = Image.open(backImageDir + "PremierLeagueTemplate002.jpeg")
    back_xlim = ax_backimage.get_xlim()
    back_ylim = ax_backimage.get_ylim()
    ax_backimage.imshow(back_im, extent=[*back_xlim, *back_ylim], aspect="auto", alpha=0.8)
    #fig.set_facecolor("lightblue")
    #ax_scoreboard = fig.add_subplot(gs_scoreboard[:,:])

    ax_homeTeamName = fig.add_subplot(gs_homeTeamName[:,:])
    ax_awayTeamName = fig.add_subplot(gs_awayTeamName[:,:])
    ax_score        = fig.add_subplot(gs_score[:,:])
    ax_date         = fig.add_subplot(gs_date[:,:])
    DeleteAllOutlines(ax_homeTeamName)
    DeleteAllOutlines(ax_awayTeamName)
    DeleteAxesColor(ax_homeTeamName)
    DeleteAxesColor(ax_awayTeamName)
    DeleteAllOutlines(ax_score)
    DeleteAllOutlines(ax_date)
    DeleteAxesColor(ax_score)
    DeleteAxesColor(ax_date)

    teamNameId  = data.index.get_loc("TeamName")
    scoreId     = data.index.get_loc("Score")

    WriteTextFromCenterOfAxes( ax_homeTeamName, data["Home"].iloc[teamNameId], size=15, color="White")
    WriteTextFromCenterOfAxes( ax_awayTeamName, data["Away"].iloc[teamNameId], size=15, color="White")

    scoreStr = str(data["Home"].iloc[scoreId]) + " - " + str(data["Away"].iloc[scoreId])
    WriteTextFromCenterOfAxes( ax_score, scoreStr, size=24, color="White")


    # ------------- Stats Setting ------------
    ax_home = fig.add_subplot(gs_homelist[:,:])
    ax_away = fig.add_subplot(gs_awaylist[:,:])
    ax_compare = fig.add_subplot(gs_comparelist[:,:])
    ax_dataname = fig.add_subplot(gs_dataname[:,:])
    DeleteSpines(ax_compare)
    DeleteAxesColor(ax_compare)
    DeleteAxesColor(ax_home)
    DeleteAxesColor(ax_away)
    DeleteAxesColor(ax_dataname)

    #DeleteAxesColor()
    #ax_compare.patch.set_alpha(0.0)
    #ax_dataname.patch.set_alpha(0.0)


    ax_home.yaxis.tick_right()
    ax_home.set_xlim([100,0])
    ax_home.set_ylim([GetDataWithoutNameAndScore(data).shape[0],-0.5])

    ax_away.set_xlim([0,100])
    ax_away.set_ylim([GetDataWithoutNameAndScore(data).shape[0],-0.5])

    ax_dataname.set_ylim([GetDataWithoutNameAndScore(data).shape[0],-0.5])

    DeleteSpines(ax_home)
    DeleteSpines(ax_away)
    DeleteAllOutlines(ax_dataname)

    homeLabel    = GetDataWithoutNameAndScore(data["Home"]).values.tolist()
    awayLabel    = GetDataWithoutNameAndScore(data["Away"]).values.tolist()

    data["Max"] = data["Home"] + data["Away"]

    homeData    = GetDataWithoutNameAndScore(data["Home"]).values.tolist()
    awayData    = GetDataWithoutNameAndScore(data["Away"]).values.tolist()
    maxData     = GetDataWithoutNameAndScore(data["Max"])
    indexData   = list(GetDataWithoutNameAndScore(data["Home"]).index)

    #normalizedHomeData =

    #DrawHorizontalBar(  ax_home, GetNormalizedDataList(homeData, maxData), labels=GetDataNumAsLabel(homeData), color="r")
    #DrawHorizontalBar(  ax_away, GetNormalizedDataList(awayData, maxData), labels=GetDataNumAsLabel(awayData), color="b")
    #WriteDataName( ax_dataname, indexData, size=10)

    vis_data = data.drop("TeamName")
    vis_data = GetNormalizedDataList(vis_data)
    DrawStatsWithComparingHorizontalBar( ax_compare, vis_data)
    ax_compare.set_ylim([len(vis_data.index),-0.5])

    WriteDataName( ax_dataname, vis_data.index, color="White", size=12, pos="top")


    DeleteXTicks(ax_home)
    DeleteXTicks(ax_away)
    DeleteAllOutlines(ax_home)
    DeleteAllOutlines(ax_away)
    DeleteAllOutlines(ax_dataname)
    DeleteAllOutlines(ax_compare)

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

