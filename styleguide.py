# -*- coding: utf-8 -*-
import sys

import FigmaStyleLib

token = "< T O K E N >"

site = sys.argv[1]
fileid = FigmaStyleLib.get_file_id(site)
print("Start\nfileid: ", fileid)
if fileid:
    rez = FigmaStyleLib.load(token, fileid)
    arrFonts = FigmaStyleLib.fonts2(rez)
    arrFonts4 = FigmaStyleLib.razv(arrFonts)
    sortArreyFont2 = FigmaStyleLib.sort_font2(arrFonts4)
    sortArreyFont = FigmaStyleLib.sort_font3(sortArreyFont2)
    arrColors = FigmaStyleLib.colors(rez)
    otvet = ""
    with open("templ1.tml", "r") as file:
        otvet += file.read()
    otvet += "<div class=\"fonts-template\">\n"
    otvet += "<div class=\"container\">\n"
    otvet += "<h2 style=\"padding: 3rem 1.5rem;\">Font</h2>\n"
    otvet += "<div class=\"row\">\n"
    for item in sortArreyFont:
        otvet += item.tohtml() + "\n"
    otvet += "</div>\n"
    otvet += "</div>\n"
    otvet += "</div>\n"
    otvet += "<div class=\"colors-template\">\n"
    otvet += "<div class=\"container\">\n"
    otvet += "<h2 style=\"padding: 3rem 1.5rem;\">Font (Code)</h2>\n"
    otvet += "<div class=\"row\">\n"
    for item in sortArreyFont2:
        otvet += "<div class=\"col-6 col-md-3\" style=\"padding: 3rem 1rem;\">"
        otvet += "font-family: " + str(item.fontFamily) + ";<br>"
        otvet += "font-size: " + str(item.fontSize) + "px;<br>"
        otvet += "line-height: " + str(item.lineHeightPx) + "px;<br>"
        otvet += "letter-spacing: " + str(item.letterSpacing) + "px;<br>"
        otvet += "color: " + item.color.getrgb() + ";&nbsp;<b style=\"color: " + item.color.getrgb() + ";\">&#9632;</b><br>" + "</div>\n"
    otvet += "</div>\n"
    otvet += "</div>\n"
    otvet += "</div>\n"
    otvet += "<div class=\"colors-template\">\n"
    otvet += "<div class=\"container\">\n"
    otvet += "<h2 style=\"padding: 3rem 1.5rem;\">Color</h2>\n"
    otvet += "<div class=\"row\">\n"
    for item in arrColors:
        otvet += item.tohtml_c()
    otvet += "</div>\n"
    otvet += "</div>\n"
    otvet += "</div>\n"
    with open("templ2.tml", "r") as file:
        otvet += file.read()
    textfile0 = open(fileid + '.html', 'w', encoding='utf8')
    textfile0.write(otvet)
    textfile0.close()
print("FINISH ")
