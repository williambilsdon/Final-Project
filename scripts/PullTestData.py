import os
import shutil
import random

source = '../training data'

toMakeTest = ['00000', '00043', '00012', '00077', '00093', '00034', '00026', '00059', '00084', '00005']

for root, dirs, files in os.walk(source):
    for filename in files:
        testImageID = random.randint(0,9)


        if(filename != '.DS_Store'):
            name = os.path.splitext(filename)[0]
            testTrack = name.split('_')


            if testTrack[1] in toMakeTest:
                originalFile = root + '/' + name + '.png'

                destination = '../test data/' + testTrack[0] + '/' + name + '.png'

                shutil.move(originalFile, destination)
