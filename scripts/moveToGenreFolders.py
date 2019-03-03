import os
import shutil

genres = ['blues', 'rock', 'jazz', 'reggae', 'disco', 'pop', 'hiphop','country', 'metal', 'classical']
dir1 = '../slices/test data/'
dir2 = '../slices/training data/'
dir3 = '../slices/validation data/'


def moveFiles(source):
    for genre in genres:
        if not os.path.exists(dir1 + genre):
            os.mkdir(dir1 + genre)

        if not os.path.exists(dir2 + genre):
            os.mkdir(dir2 + genre)

        if not os.path.exists(dir3 + genre):
            os.mkdir(dir3 + genre)

    for filename in os.listdir(source):

        if os.path.splitext(filename)[1] == '.png':
            splitname = filename.split("_")

            originalFile = source + filename

            destination = source + splitname[0] + '/' + filename

            shutil.move(originalFile, destination)

moveFiles(dir1)
moveFiles(dir2)
moveFiles(dir3)
