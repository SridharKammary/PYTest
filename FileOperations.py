import os
srcDir="C:\DEVELOPMENT_WORKSPACES\COPY_TESTING\SRC"
DstDir="C:\DEVELOPMENT_WORKSPACES\COPY_TESTING\DST"

listOfFiles=os.listdir(srcDir)
filePaths=list([])

def extractListOfFiles(srcDir : str)->None:
 if os.path.isfile(srcDir):
     filePaths.append(srcDir)
 else:
    listOfFiles=os.listdir(srcDir)
    for file in listOfFiles:
        if os.path.isfile(file):
            filePaths.append(file)
        else:
            extractListOfFiles(os.path.join(srcDir,file))
 
extractListOfFiles(srcDir)
sorted(filePaths,reverse=True)
for k in filePaths:
   print(k)