

def GetLineShapeDict(x0, x1, y0, y1, width=6, color="#FFFFFF"):
    dict = {
            "type": "line",
            "x0": x0,
            "x1": x1,
            "y0": y0,
            "y1": y1,
            "line": {
                "color": color,
                "width":width
            }
    }
    return dict

def GetCircleShapeDict(x, y, r, width=3, line_color="#FFFFFF", fill_color="#89EF89", fill=False):
    dict = {
        "type": "circle",
        "x0": x-r,
        "y0": y-r,
        "x1": x+r,
        "y1": y+r,
        "line": {
            "color": line_color,
            "width": width,
        }
    }
    return dict
