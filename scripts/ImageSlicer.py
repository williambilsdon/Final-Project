import cv2
import os

destination = '../slices/training'
sources = '../wholepngs/training'

def imageSlice(source, sliceDest):

    imageX = 3200
    numSlices = 10
    xStride = imageX / numSlices

    if os.path.splitext(source)[1] != '.DS_Store':
        xPos = 0
        newX = int(xPos) + int(xStride)
                #print(destination)
                #os.makedirs(destination)

        for i in range(0,10):
            location = source
            original = cv2.imread(location)
            slice = original[0:2400, int(xPos):int(newX)]

            cv2.imwrite((sliceDest + str(i) + '.png'), slice)

            xPos += xStride
            newX += xStride


for root, dirs, files in os.walk(sources):
    for filename in files:
        if filename != '.DS_Store':
            genre = root.split("/")

            if len(genre) == 4:
                genre = genre[3]

                source = root + '/' + filename
                sliceDest = destination + '/' + genre + '/' + os.path.splitext(filename)[0] + '_'

                imageSlice(source, sliceDest)
