import cv2
import os

imageX = 3200
numSlices = 10
xStride = imageX / numSlices

source = ('../tests')

for root, dirs, files in os.walk(source):
    for filename in files:
        if filename != '.DS_Store':
            xPos = 0
            newX = int(xPos) + int(xStride)

            trackNum = os.path.splitext(filename)[0]
            genre = trackNum.split(".")

            destination = source + '/' + genre[0] + '/slices/' +  trackNum
            #print(destination)
            #os.makedirs(destination)

            for i in range(0,10):
                location = root + '/' + filename
                original = cv2.imread(location)
                slice = original[0:2400, int(xPos):int(newX)]

                cv2.imwrite((destination + '/' + str(i) + '.png'), slice)

                xPos += xStride
                newX += xStride
