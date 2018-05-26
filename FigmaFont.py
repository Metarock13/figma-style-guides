import json
import FigmaColor

class FigmaFont(object):
    fontFamily = ''
    fontPostScriptName = ''
    fontWeight = 0
    fontSize = 0
    letterSpacing = 0.0
    lineHeightPx = 0.0
    lineHeightPercent = 0.0
    color = ''
    styleOverrideTable = []
    mjson = ''

    def __init__(self, index, jfills):
        if index == 0:
            pjson = json.loads(jfills)
            self.mjson = pjson
            style = pjson['style']

            if "fontFamily" in style:
                self.fontFamily = style["fontFamily"]
            else:
                self.fontFamily = ''

            if "fontPostScriptName" in style:
                self.fontPostScriptName = style["fontPostScriptName"]
            else:
                self.fontPostScriptName = ''

            if "fontWeight" in style:
                self.fontWeight = style["fontWeight"]
            else:
                self.fontWeight = ''

            if "fontSize" in style:
                self.fontSize = style["fontSize"]
            else:
                self.fontSize = ''

            if "letterSpacing" in style:
                self.letterSpacing = style["letterSpacing"]
            else:
                self.letterSpacing = ''

            if "lineHeightPx" in style:
                self.lineHeightPx = style["lineHeightPx"]
            else:
                self.lineHeightPx = ''

            if "lineHeightPercent" in style:
                self.lineHeightPercent = style["lineHeightPercent"]
            else:
                self.lineHeightPercent = ''

            if "styleOverrideTable" in pjson:
                styleOverrideTable = pjson["styleOverrideTable"]
                if len(styleOverrideTable) > 0:
                    self.styleOverrideTable = []
                    # print("font2 ",len(styleOverrideTable))
                    for temp in styleOverrideTable.items():
                        # print("temp[1] ",temp[1])
                        font = FigmaFont(1, temp[1])
                        self.styleOverrideTable.append(font)
                        del font
            else:
                self.styleOverrideTable = ''

            jcolor = pjson["fills"]
            if len(jcolor) == 1:
                self.color = FigmaColor.FigmaColor("json", jcolor[0]["color"], 0, 0, 0, 0)
            else:
                self.color = FigmaColor.FigmaColor("json", jcolor[0]["color"], 0, 0, 0, 0)
        if index == 1:
            style = jfills
            self.mjson = jfills

            if "fontFamily" in style:
                self.fontFamily = style["fontFamily"]
            else:
                self.fontFamily = ''

            if "fontPostScriptName" in style:
                self.fontPostScriptName = style["fontPostScriptName"]
            else:
                self.fontPostScriptName = ''

            if "fontWeight" in style:
                self.fontWeight = style["fontWeight"]
            else:
                self.fontWeight = ''

            if "fontSize" in style:
                self.fontSize = style["fontSize"]
            else:
                self.fontSize = ''

            if "letterSpacing" in style:
                self.letterSpacing = style["letterSpacing"]
            else:
                self.letterSpacing = ''

            if "lineHeightPx" in style:
                self.lineHeightPx = style["lineHeightPx"]
            else:
                self.lineHeightPx = ''

            if "lineHeightPercent" in style:
                self.lineHeightPercent = style["lineHeightPercent"]
            else:
                self.lineHeightPercent = ''
            if "fills" in style:
                jcolor = style["fills"]
                if len(jcolor) == 1:
                    self.color = FigmaColor.FigmaColor("json", jcolor[0]["color"], 0, 0, 0, 0)
                else:
                    self.color = FigmaColor.FigmaColor("json", jcolor[0]["color"], 0, 0, 0, 0)
        if index == 3:
            self.fontFamily = ''
            self.styleOverrideTable = ''
            self.fontPostScriptName = ''
            self.fontWeight = 0
            self.fontSize = 0
            self.letterSpacing = 0.0
            self.lineHeightPx = 0.0
            self.lineHeightPercent = 0.0
            self.color = ''
            self.styleOverrideTable = []

    def tostring(self):
        try:
            ret = self.fontFamily + " - " + str(self.fontPostScriptName) + " - " + str(self.fontWeight) + " - " + str(
                self.fontSize) + " - " + str(self.letterSpacing) \
                  + " - " + str(self.lineHeightPx) + " - " \
                  + str(self.lineHeightPercent) + " - " + self.color.getrgba()
            return ret
        except Exception:
            print("error: " + str(self.mjson))
        return ""
