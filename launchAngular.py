# Author: Wayne Jessen

import os

curDir = os.getcwd()

#App Directory
appDir = str(curDir + "/app")

#App Sub Directories
shareDir = str(appDir + "/Shared")
compDir = str(appDir + "/Components")

#shareDir Sub directories
navDir = str(shareDir + "/Navigation")

#compDir Sub Directories
homeDir = str(compDir + "/home")

#assets directory
assestsDir = str(curDir + "/assets")

#asset dub dirs
imgDir = str(assestsDir + "/img")
cssDir = str(assestsDir + '/css')
jsDir = str(assestsDir + "/js")
libDir = str(assestsDir + "/libs")

#root folder files
index = "index.html"

#app files
appModule = str(appDir + '/app.module.js')
appRouters = str(appDir + '/app.routes.js')

#nav files
navDirective = str(navDir + "/navDirective.js")
navView = str(navDir + "/navView.html")

#component files
homeController = str(homeDir + "/homeController.js")
homeService = str(homeDir + "/homeService.js")
homeView = str(homeDir + "/homeView.html")

dirsToCreate = [curDir, appDir, compDir, navDir, homeDir,
		assestsDir, imgDir, cssDir, jsDir, libDir]

filesToCreate = [index, appModule, appRouters, navDirective, navView, 
				homeController, homeService, homeView]

def createDirs(listOfDirs):
	for dr in listOfDirs:
		if not os.path.exists(dr):
			os.makedirs(dr)

def createFiles(listOfFiles):
	for fl in listOfFiles:
		f = open(fl, 'w')
		f.close()

createDirs(dirsToCreate)
createFiles(filesToCreate)


