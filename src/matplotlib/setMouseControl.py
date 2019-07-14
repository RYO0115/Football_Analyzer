
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseEvent
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
import numpy as np
import math
from setPlayer import *

GRID_ROWS = 20
GRID_COLS = 20


home = 0
away = 1

class GUI_CONTROL():
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        self._dragging_player = []
        self._dragging_multi = None

        self.ps = PLAYER_SERVER(self.ax)
        self.ps.SetFullMember()
        self.ps.teams[home].SetPlayerPosition("4231")
        self.ps.teams[away].SetPlayerPosition("442")
        self._players = self.ps.DrawPlayers()



    def _update_plot(self):
        #self.delaunay = self.ps.DrawDelaunay()
        #self.volonoi = self.ps.DrawVolonoi()
        self.fig.canvas.draw()

    def _find_neighbor_player(self, event):
        distance_threshold = 3.0
        nearest_player = None
        min_distance = math.sqrt(2 * (100 ** 2))
        for i in range(len(self._players)):
            x,y = self._players[i].circle.center
            distance = math.hypot(event.xdata - x, event.ydata - y)
            if distance < min_distance:
                min_distance = distance
                nearest_player = i
        if min_distance < distance_threshold:
            return nearest_player
        return None

    def _move_player(self, player_id, event):
        self._players[player_id].circle.center = event.xdata, event.ydata
        self._players[player_id].UpdatePlayerPosition()

    def _on_click(self, event):
        # left click
        if event.button == 1 and event.inaxes in [self.ax]:
            player_id = self._find_neighbor_player(event)
            if player_id:
                self._dragging_player.append(player_id)
                self._dragging_multi = None
        # right click
        #elif event.button == 3 and event.inaxes in [self.ax]:
        #    player_id = self._find_neighbor_player(event)
        #    print(self._players[player_id].center)
        #    print("right click")



    def _on_release(self, event):

        if event.button == 1 and event.inaxes in [self.ax] and len(self._dragging_player):
            self._dragging_player = []
            self._update_plot()

    def _on_motion(self, event):
        if not len(self._dragging_player):
            return
        if event.xdata is None or event.ydata is None:
            return
        for player in self._dragging_player:
            self._move_player( player, event)
        self._update_plot()


