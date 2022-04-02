import os
from shutil import copyfile

originDir = 'C:/Users/username/Desktop/창업/이미지들/'

destPath = 'C:/Users/username/Desktop/2019Dev/newHaktal/assets/images'

folders = [name for name in os.listdir(originDir) if os.path.isdir(os.path.join(originDir,name))]


for folder in folders:
    hdpiPath = originDir + folder +'/drawable-hdpi/'
    mdpiPath = originDir + folder +'/drawable-mdpi/'
    xhdpiPath = originDir + folder +'/drawable-xhdpi/'
    xxhdpiPath = originDir + folder +'/drawable-xxhdpi/'
    xxxhdpiPath = originDir + folder +'/drawable-xxxhdpi/'
    
    for file in os.listdir(hdpiPath):
        os.rename(hdpiPath+ file, hdpiPath + folder + '.png')
        thisFile = hdpiPath + folder + '.png'
        destFile = destPath +'/drawable-hdpi/' + folder + '.png'
        copyfile(thisFile, destFile)
        print(destFile)

    for file in os.listdir(mdpiPath):
        os.rename(mdpiPath+ file, mdpiPath + folder + '.png')
        thisFile = mdpiPath + folder + '.png'
        destFile = destPath +'/drawable-mdpi/' + folder + '.png'
        copyfile(thisFile, destFile)
        print(destFile)
    
    for file in os.listdir(xhdpiPath):
        os.rename(xhdpiPath+ file, xhdpiPath + folder + '.png')
        thisFile = hdpiPath + folder + '.png'
        destFile = destPath +'/drawable-xhdpi/' + folder + '.png'
        copyfile(thisFile, destFile)
        print(destFile)

    for file in os.listdir(xxhdpiPath):
        os.rename(xxhdpiPath+ file, xxhdpiPath + folder + '.png')
        thisFile = hdpiPath + folder + '.png'
        destFile = destPath +'/drawable-xxhdpi/' + folder + '.png'
        copyfile(thisFile, destFile)
        print(destFile)

    for file in os.listdir(xxxhdpiPath):
        os.rename(xxxhdpiPath+ file, xxxhdpiPath + folder + '.png')
        thisFile = hdpiPath + folder + '.png'
        destFile = destPath +'/drawable-xxxhdpi/' + folder + '.png'
        copyfile(thisFile, destFile)
        print(destFile)
    

    
    
