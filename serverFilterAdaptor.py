from ppmFliter import *
import string
import random
class serverFilterAdaptor:
    def __init__(self, width, imgType, locat, fname):
        self.width = width
        self.reader = ppmImageReader(locat+"/"+fname)
        self.imageType = imgType
        self.fName = fname
        self.locat = locat

    def convertToPPM(self):
        newName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

        return newName+".ppm"

    def convertToPNG(self, newPPM):
        newName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))      

        return newName + ".png"

    def process(self):
        newName = self.convertToPPM()
        print(newName)
        self.read(newName)
        self.doFilter(self.width, self.imageType)
        newPPM = self.write()
        return self.convertToPNG(newPPM)

    def read(self, nom):
        self.reader = ppmImageReader(self.locat + "/" + nom)
        self.img = self.reader.getImage()

    def doFilter(self, width, filterType):
        if (filterType == 1):
            self.filter = ppmMeanFilter(self.img, width, width)
        else:
            self.filter = ppmMedianFilter(self.img, width, width)
        self.filter.filter()

    def write(self):
        name = self.locat + "/filtered_" + self.fName
        self.writer = ppmImageWriter(self.filter.getFilteredImg())
        self.writer.writePPM(name)
        return "filtered_" + self.fName



