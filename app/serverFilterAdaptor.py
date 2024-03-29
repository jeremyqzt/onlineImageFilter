from ppmFliter import *
from removalThread import *
import string
import uuid
import os

class serverFilterAdaptor:
    def __init__(self, width, imgType, locat, fname):
        self.width = width
        self.imageType = imgType
        self.fName = fname
        self.locat = locat

    def __tryRemove(self, fullName):
        #TODO : Systemd job to clean out the directory...
        try:
            os.remove(fullName)
        except:
            pass #No worries...

    def convertToPPM(self):
        newName = str(uuid.uuid4())
        fullNewImage = "%s.ppm" % (newName)
        shell = "convert -compress none %s/%s %s/%s" % (self.locat, self.fName, self.locat, fullNewImage)
        if (0 != os.system(shell)):
            return None
        self.__tryRemove("%s/%s" % (self.locat, self.fName))
        return fullNewImage

    def convertToPNG(self, newPPM):
        newName = str(uuid.uuid4())
        fullNewImage = "%s.png" % (newName)
        shell = "convert -compress none %s/%s %s/%s" % (self.locat, newPPM, self.locat, fullNewImage)
        if( 0 != os.system(shell)):
            return None
        self.__tryRemove("%s/%s" % (self.locat, newPPM))
        th = removalThread("%s/%s" % (self.locat, fullNewImage), 60)
        th.start()
        return fullNewImage

    def process(self):
        newName = self.convertToPPM()
        if (newName == None):
            return None
        try:
            self.read(newName)
            self.doFilter(self.width, self.imageType)
            newPPM = self.write()
        except:
            return None

        return self.convertToPNG(newPPM)

    def read(self, nom):
        self.reader = ppmImageReader("%s/%s" % (self.locat, nom))
        self.img = self.reader.getImage()
        self.__tryRemove("%s/%s" % (self.locat, nom))

    def doFilter(self, width, filterType):
        if (filterType == 1):
            self.filter = ppmMeanFilter(self.img, width, width)
        else:
            self.filter = ppmMedianFilter(self.img, width, width)
        self.filter.filter()

    def write(self):
        newName = str(uuid.uuid4())
        name = "%s/%s.ppm" %(self.locat, newName)
        self.writer = ppmImageWriter(self.filter.getFilteredImg())
        self.writer.writePPM(name)
        return "%s.ppm" % (newName)



