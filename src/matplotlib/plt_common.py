import matplotlib.pyplot as plt
import numpy as np

from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
from PIL import Image

def GetFullSizeFigure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None):
    fig = plt.figure(num=num, figsize=figsize, dpi=dpi, facecolor=facecolor, edgecolor=edgecolor)
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

def DeleteAxesColor(ax):
    ax.patch.set_alpha(0.0)

def WriteTextFromCenterOfAxes(ax, str, size=12, color="black"):
    ax.set_xlim([0,100])
    ax.set_ylim([0,100])
    ax.text( 50, 50, str, size=size, ha="center", va="center")
