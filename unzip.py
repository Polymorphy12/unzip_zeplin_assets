import zipfile
import os
 
def unzip(source_file, dest_path):
    with zipfile.ZipFile(source_file, 'r') as zf:
        zf.extractall(path=dest_path)
        zf.close()

originDirectory = 'C:/Users/ty79450/Desktop/창업/이미지들/'
fileList = os.listdir('C:/Users/ty79450/Desktop/창업/이미지들/')

for file in fileList:
    print(file)
    if '.zip' not in file:
        print(False)
        continue
    unzip(originDirectory + file, originDirectory + file.split('.zip')[0])
    
