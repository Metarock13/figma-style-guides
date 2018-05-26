class FigmaFonts(object):
    FontFamily = ''
    FontPostScriptName = ''
    FontSizes = []
    LineHeightPercents = []
    LetterSpacings = []

    def __init__(self):
        self.FontFamily = ''
        self.FontPostScriptName = ''
        self.FontSizes = []
        self.LineHeightPercents = []
        self.LetterSpacings = []

    def add(self, fontSize, lineHeightPercent, letterSpacing):
        est = False
        for item in self.FontSizes:
            if item == fontSize:
                est = True
        if not est:
            self.FontSizes.append(fontSize)
        self.FontSizes.sort()
        est1 = False
        for item in self.LineHeightPercents:
            if item == lineHeightPercent:
                est1 = True
        if not est1:
            self.LineHeightPercents.append(lineHeightPercent)

        est2 = False
        for item in self.LetterSpacings:
            if item == letterSpacing:
                est2 = True
        if not est2:
            self.LetterSpacings.append(letterSpacing)

    def tostring(self):
        retfont = "Font: " + self.FontFamily
        retstyle = "\nStyle: " + str(self.FontPostScriptName)
        retsize = "\nSize: " + ', '.join(str(x) for x in self.FontSizes)
        retLineheights = "\nLine heights: "
        j2 = []
        for item in self.LineHeightPercents:
            j2.append(item)
        retLineheights += ', '.join(str(x) for x in j2)

        return retfont + retstyle + retsize + retLineheights + "\n"

    def tohtml(self):
        ret = "<div class=\"col-md-6\" style=\"padding-bottom: 1rem;\">\n"
        ret += "<div class=\"card box-shadow\">\n"
        ret += "<div class=\"card-body\">\n"
        ret += "<h3 class=\"card-title\" style=\"padding: 1rem 1.5rem; text-align: center;\">" + str(
            self.FontFamily) + "</h3>\n"
        ret += "</div>\n"
        ret += "<ul class=\"list-group list-group-flush\">\n"
        ret += "<li class=\"list-group-item\">\n"
        ret += "<h6 class=\"card-title\">Style</h6>\n"
        ret += "<p>" + str(self.FontPostScriptName) + "</p>\n"
        ret += "</li>\n"
        ret += "<li class=\"list-group-item\">\n"
        ret += "<h6 class=\"card-title\">\n"
        ret += "Sizes\n"
        ret += "</h6>\n"
        ret += "<div class=\"container-fluid\">\n"
        ret += "<div class=\"row\">\n"
        for item in self.FontSizes:
            ret += "<div class=\"col\" style=\"text-align: center; padding-bottom: 1rem;\">" + \
                   str(item) + "&nbsp;pt</div>\n"
        ret += "</div>\n"
        ret += "</div>\n"
        ret += "</li>\n"
        ret += "<li class=\"list-group-item\">\n"
        ret += "<h6 class=\"card-title\">\n"
        ret += "Line&nbsp;heights\n"
        ret += "</h6>\n"
        ret += "<div class=\"container-fluid\">\n"
        ret += "<div class=\"row\">\n"
        for item in self.LineHeightPercents:
            ret += "<div class=\"col\" style=\"text-align: center; padding-bottom: 1rem;\">" + str(item) + "%</div>\n"
        ret += "</div>\n"
        ret += "</div>\n"
        ret += "</li>\n"
        ret += "<li class=\"list-group-item\">\n"
        ret += "<h6 class=\"card-title\">\n"
        ret += "Letter&nbsp;spacings\n"
        ret += "</h6>\n"
        ret += "<div class=\"container-fluid\">\n"
        ret += "<div class=\"row\">\n"
        for item in self.LetterSpacings:
            ret += "<div class=\"col\" style=\"text-align: center; padding-bottom: 1rem;\">" + str(
                item) + "&nbsp;px</div>\n"
        ret += "</div>\n"
        ret += "</div>\n"
        ret += "</li>\n"
        ret += "</ul>\n"
        ret += "</div>\n"
        ret += "</div>\n"

        return ret
