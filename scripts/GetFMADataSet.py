import csv
from SortTestData import specgram

csvLocation = '../../tracks.csv'
source = '../../fma_medium'
csvFile = csv.reader(open(csvLocation, 'r'))
trackDest = ("../wholepngs/training data")
sliceDest= ("../slices/training data")

genreValues = ['rock', 'classical', 'country', 'jazz', 'reggae', 'disco', 'pop', 'hiphop', 'metal', 'blues']


for row in csvFile:
    genres = row[41]
    genreSplit = genres.split(",")

    if row[40].lower() in genreValues:
        print(row[0])

        split = list(row[0])

        folder = split[0] + split[1] + split[2]

        source = source + '/' + folder + '/' + row[0]
        trackDest = trackDest + '/' + row[40].lower() + '/' +row[0] + '.png'
        sliceDest = sliceDest + '/' + row[40].lower()

        spegram(trackDest, source, sliceDest)
