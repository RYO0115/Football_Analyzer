from shape_common import *
COURT_SIZE = [72.5, 45]


class FOOTBALL_COURT():
    def __init__(self):
        self.layout={}
        self.layout["xaxis"] = self.setXAxis()
        self.layout["yaxis"] = self.setYAxis()
        self.shapes=self.drawLines()
        self.shapes.extend(self.drawCircles())

    def setXAxis(self):
        axis = dict(
            autorange=False,
            range=[-COURT_SIZE[0],COURT_SIZE[0]],
            zeroline=False,
            showline=False,
            mirror='ticks',
            showgrid=False,

            #グラフを描く幅、複数のグラフを描きたいなら 0 ~ 1の範囲で範囲を指定すればその範囲で描画してくれる
            domain=[0.2,0.8],
            showticklabels=False,
        )
        return(axis)

    def setYAxis(self):
        axis = dict(
            autorange=False,
            range=[-COURT_SIZE[1], COURT_SIZE[1]],
            zeroline=False,
            showline=False,
            showgrid=False,
            scaleanchor="x",
            domain=[0.1,0.7],
            showticklabels=False,
        )
        return axis


    def drawLines(self):
        lines = [
        # タッチライン
        GetLineShapeDict(-COURT_SIZE[0],COURT_SIZE[0], COURT_SIZE[1], COURT_SIZE[1],  width=4),
        GetLineShapeDict(-COURT_SIZE[0],COURT_SIZE[0],-COURT_SIZE[1],-COURT_SIZE[1],  width=4),
        GetLineShapeDict(-COURT_SIZE[0],-COURT_SIZE[0],-COURT_SIZE[1], COURT_SIZE[1], width=4),
        GetLineShapeDict( COURT_SIZE[0], COURT_SIZE[0],-COURT_SIZE[1], COURT_SIZE[1], width=4),
        # センターライン
        GetLineShapeDict(0,0,-COURT_SIZE[1],COURT_SIZE[1], width=3),
        #ゴールエリア
        GetLineShapeDict( 67.0, 67.0,-9.16, 9.16, width=3),
        GetLineShapeDict(-67.0,-67.0,-9.16, 9.16, width=3),
        GetLineShapeDict( 67.0, COURT_SIZE[0], 9.16, 9.16, width=3),
        GetLineShapeDict( 67.0, COURT_SIZE[0],-9.16,-9.16, width=3),
        GetLineShapeDict(-67.0,-COURT_SIZE[0], 9.16, 9.16, width=3),
        GetLineShapeDict(-67.0,-COURT_SIZE[0],-9.16,-9.16, width=3),

        #ペナルティエリア
        GetLineShapeDict( 56.0, 56.0,-20.16, 20.16, width=3),
        GetLineShapeDict(-56.0,-56.0,-20.16, 20.16, width=3),
        GetLineShapeDict( 56.0, COURT_SIZE[0], 20.16, 20.16, width=3),
        GetLineShapeDict( 56.0, COURT_SIZE[0],-20.16,-20.16, width=3),
        GetLineShapeDict(-56.0,-COURT_SIZE[0], 20.16, 20.16, width=3),
        GetLineShapeDict(-56.0,-COURT_SIZE[0],-20.16,-20.16, width=3)
        ]
        return(lines)

    def drawCircles(self):
        circles = [
        #センターサークル
        GetCircleShapeDict( 0, 0, 9.150, fill=False),

        #ペナルティスポット
        GetCircleShapeDict(  61.5, 0, 0.5, fill=True, line_color="#000000", fill_color="#000000"),
        GetCircleShapeDict( -61.5, 0, 0.5, fill=True, line_color="#000000", fill_color="#000000")
            ]
        return(circles)
