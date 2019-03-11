import os
import shutil
import random

sourceWhole = '../wholepngs/training'
sourceSlice = '../slices/training'

destWhole = '../wholepngs/validation'
destSlice = '../slices/validation'


genres = ['classical', 'country', 'jazz', 'pop', 'hiphop', 'blues', 'rock', 'metal', 'reggae', 'disco']

def extract(source, dest):
    for genre in genres:

        paths = []
        counter = 0

        folder = source +'/'+genre

        for root, dirs, files in os.walk(folder):
            for filename in files:
                location = folder + '/' + filename
                paths.append(location)

        numFiles = len(paths)
        numToVal = (numFiles / 100) * 30
        numToVal = round(numToVal)
        maxIndex = numFiles - 1

        while counter < numToVal:
            index = random.randint(0, maxIndex)

            path = paths[index]
            split = path.split("/")
            name = split[4]

            destination = dest + '/' + genre + '/' + name

            shutil.move(path, destination)
            paths.pop(index)
            maxIndex-=1
            counter+=1




extract(sourceWhole, destWhole)
extract(sourceSlice, destSlice)
