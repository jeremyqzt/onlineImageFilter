class ppmPixel:
    def __init__(self, r,g,b):
        self.r = r
        self.g = g
        self.b = b
        
    def __str__(self):
        return ("r:%d g:%d b:%d" % (self.r,self.g,self.b))

    def __repr__(self):
        return ("Class ppmPixel r:%d g:%d b:%d" % (self.r,self.g,self.b))

    def __add__(self, other):
        return ppmPixel(self.r + other.r, self.g + other.g, self.b + other.b)

    def __floordiv__(self, other):
        return ppmPixel(self.r // other, self.g // other, self.b // other)

class ppmImage:
    def __init__(self, fmt, width, height, color):
        self.__addMeta( fmt, width, height, color)
        self._internalImageRepr = []
        self.curWArr = []
    def __addMeta(self, fmt, width, height, color):
        self.fmt = fmt
        self.width = width
        self.height = height
        self.colorMax = color
        self.curW = 0
        self.curH = 0

    def getFmt(self):
        return self.fmt.strip()
    def getWbH(self):
        return "%d %d" % (self.width, self.height)
    def getColorMax(self):
        return self.colorMax

    def addImgData(self, r, g, b):
        imgPix = ppmPixel(r,g,b)
        self.addImgDataPix(imgPix)

    def addImgDataPix(self, imgPix):
        self.curWArr.append(imgPix)
        self.curW += 1
        if (self.curW >= self.width):
            self.curW = 0
            self._internalImageRepr.append(self.curWArr)
            self.curWArr = []
            
    def getImageArr(self):
        return self._internalImageRepr

    def getPixel(self, row, col):
        if (row < self.height and row >= 0 and col >= 0 and col < self.width):
            return self._internalImageRepr[row][col]
        return None
