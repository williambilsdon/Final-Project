import cv2
import os

def imageSlice(source, sliceDest):

    imageX = 3200
    numSlices = 10
    xStride = imageX / numSlices

    if os.path.splitext(source)[1] != '.DS_Store':
        xPos = 0
        newX = int(xPos) + int(xStride)
                #print(destination)
                #os.makedirs(destination)

        filename = os.path.splitext(source)[0]

        for i in range(0,10):
            location = source
            original = cv2.imread(location)
            slice = original[0:2400, int(xPos):int(newX)]

            name = filename.split('/')

            cv2.imwrite((sliceDest + '/' + name[3] + '_' + str(i) + '.png'), slice)

            #print(sliceDest + '/' + name[3] + '_' + str(i) + '.png')

            xPos += xStride
            newX += xStride
