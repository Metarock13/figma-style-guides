import math

class FigmaColor(object):
    R = float(0)
    G = float(0)
    B = float(0)
    A = float(0)

    def __init__(self, tp, jsn, r, g, b, a):
        if tp == "init":
            self.R = float(0)
            self.G = float(0)
            self.B = float(0)
            self.A = float(0)
        if tp == "double":
            self.R = r
            self.G = g
            self.B = b
            self.A = a
        if tp == "str":
            self.R = float(r)
            self.G = float(g)
            self.B = float(b)
            self.A = float(a)
        if tp == "json":
            if jsn != '':
                jr = jsn["r"]
                self.R = float(jr)
                jg = jsn["g"]
                self.G = float(jg)
                jb = jsn["b"]
                self.B = float(jb)
                ja = jsn["a"]
                self.A = float(ja)

    def getrgb(self):
        iR = int(round(self.R * 255))
        iG = int(round(self.G * 255))
        iB = int(round(self.B * 255))
        return str("#" + '{:02x}'.format(iR) + '{:02x}'.format(iG) + '{:02x}'.format(iB)).upper()

    def getrgba(self):
        iR = int(round(self.R * 255))
        iG = int(round(self.G * 255))
        iB = int(round(self.B * 255))
        iA = int(round(self.A * 255))
        return str("#" + '{:02x}'.format(iR) + '{:02x}'.format(iG) + '{:02x}'.format(iB) + '{:02x}'.format(iA)).upper()

    def tohtml(self):
        iR = int(round(self.R * 255))
        iG = int(round(self.G * 255))
        iB = int(round(self.B * 255))
        iA = int(round(self.A * 255))
        ret = "<div class=\"col-6 col-md-3\" style=\"background-color: " + self.getrgb() + "; padding: 3rem 1.5rem;\">" \
              + self.getrgb() + "<br>rgba(" + str(iR) + ",&nbsp;" + str(iG) + ",&nbsp;" + str(iB) + ",&nbsp;" + \
              str(iA) + ")</div>\n"
        return ret

    def tohtml_c(self):
        iR = int(round(self.R * 255))
        iG = int(round(self.G * 255))
        iB = int(round(self.B * 255))
        iA = int(round(self.A * 255))
        br = math.sqrt(iR * iR * 0.241 + iG * iG * 0.691 + iB * iB * 0.068)
        contrast = "black"
        if br < 130:
            contrast = "white"
        ret = "<div class=\"col-6 col-md-3\" style=\"background-color: " + self.getrgb() + \
              "; color: " + contrast + "; padding: 3rem 1rem;\">" + self.getrgb() + \
              "<br>rgba(" + str(iR) + ",&nbsp;" + str(iG) + ",&nbsp;" + str(iB) + ",&nbsp;" + str(iA) + ")</div>\n"
        return ret
