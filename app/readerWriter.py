from imageRepr import *

class ppmImageWriter:
    def __init__(self, ppmImage):
        self.img = ppmImage

    def writePPM(self, path):
        fHandle = open(path, "w")
        self._writeHeaders(fHandle)
        for row in self.img.getImageArr():
            for col in row:
                fHandle.write("%d %d %d\n" % (col.r, col.g, col.b))

    def _writeHeaders(self, fh):
        fh.write("%s\n" % (self.img.getFmt()))
        fh.write("%s\n" % (self.img.getWbH()))
        fh.write("%d\n" % (self.img.getColorMax()))


class ppmImageReader:
    def __init__(self, path):
        self.__readImage(path)

    def __readImage(self, path):
        content = []
        with open(path) as f:
            for line in f:
                if not line.startswith("#"):
                    content.append(line)

        self.__createImageInternal(content)
    def __createImageInternal(self, content):
        fmt = content[0]
        dimW, dimH = int(content[1].split()[0]), int(content[1].split()[1])
        maxColor = int(content[2])
        self.image = ppmImage(fmt, dimW, dimH, maxColor)
        pix = []
        for i in range (3, len(content)):
            for word in content[i].split():
                if word.isdigit():
                    pix.append(int(word))
                    if(len(pix) == 3):
                        self.image.addImgData(pix[0], pix[1], pix[2])
                        pix = []
            
    def getImage(self):
        return self.image