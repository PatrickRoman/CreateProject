#Make new folder in finder
#Make new file in folder
#Opens file in atom

from functions import newFolder, newFile, CopytoCLIP, openTE

nameF = input("What would you like to call your project folder? ")
path = input("Where would you like to create your folder (path)? ")
newFolder(path, nameF)
Path = path + "/" + nameF

nameM = input("What would you like to call your main file? ")
tFile = input("File extension? ")
newFile(Path, nameM, tFile)

CopytoCLIP(Path)
