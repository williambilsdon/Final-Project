import os
import shutil
import random

#source = '../slices/training data'
#dest = '../slices/test data'
destVal = '../wholepngs/validation data'

toMakeValidate = ['00000', '00043', '00012', '00077', '00093',
                '00076', '00099', '00063', '00021', '00055',
                '00017', '00002', '00006', '00030', '00024',
                '00068', '00041', '00085', '00070', '00024',
                '00019', '00088', '00065', '00023', '00031',
                '00034', '00026', '00059', '00084', '00005']


def extract(source, toMakeValidate, dest):
    for root, dirs, files in os.walk(source):
        for filename in files:
            #testImageID = random.randint(0,9)


            if(filename != '.DS_Store'):
                name = os.path.splitext(filename)[0]
                testTrack = name.split('_')

                if testTrack[1] in toMakeValidate:

                    originalFile = root + '/' + name + '.png'

                    destination = destVal + '/' + name + '.png'

                    shutil.move(originalFile, destination)


extract('../wholepngs/training data', toMakeValidate, destVal)
extract('../wholepngs/test data', toMakeValidate, destVal)

print('here')

#source = '../wholepngs/training data'
#dest = '../wholepngs/test data'

#extract(source, toMakeTest, dest)
