from imageRepr import *
from readerWriter import *

class ppmFilter:
    def __init__(self, img):
        self.img = img
        #Same Meta
        self.filteredImage = ppmImage(self.img.fmt, self.img.width, self.img.height, self.img.colorMax)
        self.imgPixels = self.img.getImageArr()

    def fliter(self):
        pass

    def getFilteredImg(self):
        return self.filteredImage

    def getOriginaImg(self):
        return self.img
    

class ppmMeanFilter(ppmFilter):
    def __init__(self, img, filterWidth, filterHeight):
        super().__init__(img)
        self.filterWidth = filterWidth
        self.filterHeight = filterHeight
    def filter(self):
        for row in range(0, len(self.imgPixels)):
            for col in range(0, len(self.imgPixels[row])):
                newPix = self._getFilteredPixel(row, col, self.filterWidth, self.filterHeight)
                self.filteredImage.addImgDataPix(newPix)

    def _getFilteredPixel(self, row, col, filterWidth, filterHeight):
        sumPixel = ppmPixel(0, 0, 0)
        totalCount = 0
        for r in range (row - filterHeight, row + filterHeight + 1):
            for c in range (col - filterWidth, col + filterWidth + 1):
                otherPix = self.img.getPixel(r, c)
                if (otherPix!=None):
                    sumPixel = sumPixel + otherPix
                    totalCount += 1
        return sumPixel // totalCount


class ppmMedianFilter(ppmFilter):
    def __init__(self, img, filterWidth, filterHeight):
        super().__init__(img)
        self.filterWidth = filterWidth
        self.filterHeight = filterHeight
    def filter(self):
        for row in range(0, len(self.imgPixels)):
            for col in range(0, len(self.imgPixels[row])):
                newPix = self._getFilteredPixel(row, col, self.filterWidth, self.filterHeight)
                self.filteredImage.addImgDataPix(newPix)
            

    def _getFilteredPixel(self, row, col, filterWidth, filterHeight):
        rArr = []
        gArr = []
        bArr = []
        for r in range (row - filterHeight, row + filterHeight + 1):
            for c in range (col - filterWidth, col + filterWidth + 1):
                otherPix = self.img.getPixel(r, c)
                if (otherPix!=None):
                    rArr.append(otherPix.r)
                    gArr.append(otherPix.g)
                    bArr.append(otherPix.b)
        r, g, b = self._getMedianInt(rArr), self._getMedianInt(gArr), self._getMedianInt(bArr)
        return ppmPixel(r,g,b)

    def _getMedianInt(self, arr):
        arr.sort()
        mid = len(arr) // 2
        return (arr[mid] + arr[~mid]) // 2
