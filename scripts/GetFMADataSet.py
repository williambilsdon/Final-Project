import csv
import os
import shutil

holder = "holder.wav"
csvLocation = '../../tracks.csv'
origin = '../../fma_medium'
csvFile = csv.reader(open(csvLocation, 'r'))
data = [row for row in csv.reader(csvLocation)]
trackDest = ("../wholepngs/training data")
trackValDest = ('../wholepngs/validation data')
sliceDest= ("../slices/training data")
sliceValDest = ('../slices/validation data')


numRock = 0
numHipHop = 0
numCountry = 0
numJazz = 0
numClassical = 0
numBlues = 0
numPop = 0

genreValues = ['classical', 'country', 'jazz', 'pop', 'hiphop', 'blues', 'rock']
genreQuants = [0, 0 ,0 ,0, 0, 0, 0]


for row in csvFile:
    split = list(row[0])

    while len(split) < 6:
        split.insert(0, '0')

        idExt = split

        idExt = ''.join(idExt)


    for root, dirs, files in os.walk(origin):
        for filename in files:
            trackNum = os.path.splitext(filename)[0]

            if trackNum == idExt:
                genre = row[40].lower()

                if genre == 'hip-hop':
                    genre = 'hiphop'

                if genre in genreValues:
                    index = genreValues.index(genre)

                    if all([ v == 50 for v in genreQuants ]) :
                        exit()
                    else:
                        if genreQuants[index] < 50:
                            source = root + '/' + filename

                            destination = '../../gtzan/gtzan_mp3/' + genre + '/' + filename

                            shutil.move(source, destination)
                            genreQuants[index] += 1
                        else:
                            os.remove(root + '/' + filename)
