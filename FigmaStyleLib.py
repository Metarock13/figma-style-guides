import json
import requests
import FigmaColor
import FigmaFont
import FigmaFonts


def get_file_id(url):
    d = url.split('/')
    if len(d) > 3:
        if d[2] == 'www.figma.com' and d[3] == 'file':
            return d[4]
        if d[0] == 'www.figma.com' and d[1] == 'file':
            return d[2]
    return ''


def load(token, fileid):
    site = "https://api.figma.com/v1/files/" + fileid
    header = {'X-FIGMA-TOKEN': token}
    r = requests.get(site, headers=header)
    r.encoding = 'utf-8'
    if r.status_code == 200:
        return r.text
    return ''


def fonts2(data):
    arr = []
    searchType = "TEXT"
    alll = m_find_token(data, searchType)
    for eee in alll:
        font = FigmaFont.FigmaFont(0, eee)
        arr.append(font)
        del font
    return arr


def m_find_token(text, searchType):
    rez = []
    ftext1 = text.split("\"" + searchType + "\"")
    indexstyle = len(ftext1)
    for i in range(1, indexstyle):
        scobLeft = ftext1[i - 1].rfind('{')
        rez1 = ftext1[i - 1][scobLeft:len(ftext1[i - 1])]
        sbr = -1
        poloz = -1
        for cr in ftext1[i]:
            poloz += 1
            if cr == '{':
                sbr += 1
            if cr == '}':
                sbr -= 1
                if sbr < -1:
                    break
        rez2 = ftext1[i][0:poloz + 1]
        bigrez = rez1 + '\"' + searchType + '\"' + rez2
        rez.append(bigrez)

    return rez


def razv(arr_fonts):
    ret = []
    for item in arr_fonts:
        if item.styleOverrideTable is not None:
            # ret.append(item)
            for item1 in item.styleOverrideTable:
                temp1 = FigmaFont.FigmaFont(3, 0)
                temp1.fontPostScriptName = item.fontPostScriptName
                temp1.fontFamily = item.fontFamily
                temp1.fontWeight = item.fontWeight
                temp1.fontSize = item.fontSize
                temp1.letterSpacing = item.letterSpacing
                temp1.lineHeightPx = item.lineHeightPx
                temp1.lineHeightPercent = item.lineHeightPercent
                temp1.color = item.color
                if item1.fontPostScriptName != '':
                    temp1.fontPostScriptName = item1.fontPostScriptName
                if item1.fontFamily != '':
                    temp1.fontFamily = item1.fontFamily
                if item1.fontWeight != '':
                    temp1.fontWeight = item1.fontWeight
                if item1.fontSize != '':
                    temp1.fontSize = item1.fontSize
                if item1.letterSpacing != '':
                    temp1.letterSpacing = item1.letterSpacing
                if item1.lineHeightPx != '':
                    temp1.lineHeightPx = item1.lineHeightPx
                if item1.lineHeightPercent != '':
                    temp1.lineHeightPercent = item1.lineHeightPercent
                if item1.color != '':
                    temp1.color = item1.color
                ret.append(temp1)
        else:
            ret.append(item)
    return ret


def sort_font2(data):
    ret = []
    for item in data:
        if len(ret) > 0:
            forh = len(ret)
            priz = False
            for i in range(0, forh):
                if ret[i].fontPostScriptName == item.fontPostScriptName and ret[i].fontFamily == item.fontFamily and \
                        ret[i].fontFamily == item.fontFamily and ret[i].fontWeight == item.fontWeight and \
                        ret[i].fontSize == item.fontSize and ret[i].letterSpacing == item.letterSpacing and \
                        ret[i].lineHeightPx == item.lineHeightPx and ret[i].color.getrgba() == item.color.getrgba():
                    priz = True
            if not priz:
                ret.append(item)
        else:
            ret.append(item)

    return ret


def sort_font3(data):
    ret = []
    for item in data:
        if len(ret) > 0:
            forh = len(ret)
            priz = False
            for i in range(0, forh):
                if ret[i].FontPostScriptName == item.fontPostScriptName and ret[i].FontFamily == item.fontFamily:
                    d1 = float(item.fontSize)
                    d2 = float(100)
                    if item.lineHeightPercent != '':
                        d2 = float(item.lineHeightPercent)
                    d3 = float(0)
                    if item.letterSpacing != '':
                        d3 = float(item.letterSpacing)
                    ret[i].add(d1, d2, d3)
                    priz = True
            if not priz:
                font = FigmaFonts.FigmaFonts()
                font.FontFamily = item.fontFamily
                font.FontPostScriptName = item.fontPostScriptName
                font.add(float(item.fontSize), float(item.lineHeightPercent), float(item.letterSpacing))
                ret.append(font)
                del font
        else:
            font = FigmaFonts.FigmaFonts()
            font.FontFamily = item.fontFamily
            font.FontPostScriptName = item.fontPostScriptName
            font.add(float(item.fontSize), float(item.lineHeightPercent), float(item.letterSpacing))
            ret.append(font)
            del font
    return ret


def colors(data):
    ftext1 = data.split("\"color\":")
    arr = []
    for i in range(1, len(ftext1)):
        temp1 = ftext1[i].find('}')
        temp2 = ftext1[i][0:temp1 + 1]
        jsn = json.loads(temp2)
        color = FigmaColor.FigmaColor("str", '', str(jsn["r"]), str(jsn["g"]), str(jsn["b"]), str(jsn["a"]))
        if len(arr) == 0:
            arr.append(color)
        else:
            est = False
            for item in arr:
                if item.R == color.R and item.G == color.G and item.B == color.B and item.A == color.A:
                    est = True
            if not est:
                arr.append(color)
    return arr
