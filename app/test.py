from ppmFliter import *
reader = ppmImageReader("testImg/orig2.ppm")
img = reader.getImage()
imgFilter = ppmMedianFilter(img, 6, 6)
imgFilter.filter()
writer = ppmImageWriter(imgFilter.getFilteredImg())
writer.writePPM("median13.ppm")