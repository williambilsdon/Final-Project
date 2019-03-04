import os
import shutil
import random

source = '../slices/training data'
dest = '../slices/test data'
destVal = '../slices/validation data'

toMakeTest = ['00034', '00026', '00059', '00084', '00005']
toMakeValidate = ['00000', '00043', '00012', '00077', '00093']

def extract(source, toMakeTest, toMakeValidate, dest):
    for root, dirs, files in os.walk(source):
        for filename in files:
            testImageID = random.randint(0,9)


            if(filename != '.DS_Store'):
                name = os.path.splitext(filename)[0]
                testTrack = name.split('_')

                if testTrack[1] in toMakeTest:
                    print(testTrack[1])
                    originalFile = root + '/' + name + '.png'

                    destination = destVal + '/' + name + '.png'

                    shutil.move(originalFile, destination)
                elif testTrack[1] in toMakeValidate:

                    originalFile = root + '/' + name + '.png'

                    destination = destVal + '/' + name + '.png'

                    shutil.move(originalFile, destination)


extract('../slices/test data', toMakeTest, toMakeValidate, dest)

print('here')

#source = '../wholepngs/training data'
#dest = '../wholepngs/test data'

#extract(source, toMakeTest, dest)
