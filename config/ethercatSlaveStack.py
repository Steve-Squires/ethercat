# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""
global ORG_PATH
global sscListFile
global count
global sscPathParsing
global ethercatSSCDirMyPath
global createSSCFileSymbol
global clearFileSymbols
global mytcpipHttpNetComponent
global symbolList


#Disable all the file symbols
def clearFileSymbols():
	for symbol in symbolList:
		symbol.setEnabled(False)

#Return File symbols from the Symbol list.
def createSSCFileSymbol(count):
	return symbolList[count]

#Callback function which is called when there is a path configuration from MHC
def ethercatSSCMyPathVisible(sym, event):
	ORG_PATH = event["value"]
	sscPathParsing(ORG_PATH)

ethercatSSCDirMyPath = etherCatComponent.createStringSymbol("ETHERCAT_SLAVESTACK_DIRECTORY_MYPATH", None)
ethercatSSCDirMyPath.setLabel("Configure Slave Stack directory path")
ethercatSSCDirMyPath.setVisible(False)
ethercatSSCDirMyPath.setDescription("Configure Slave Stack directory path")
ethercatSSCDirMyPath.setDefaultValue(Module.getPath() + "slave_stack")
ethercatSSCDirMyPath.setDependencies(ethercatSSCMyPathVisible, ["ETHERCAT_SLAVESTACK_DIRECTORY_PATH"])

def sscPathParsing(path):
	import re
	import os
	import sys

	count = 0
	# Get the Root PATH 
	ORG_PATH = path
	clearFileSymbols()
	#split slave stack path details
	slaveStackPath = path.split("\\")
	#get the last directory from the given path
	lastDirectory = slaveStackPath[len(slaveStackPath)-1]
	#get the current root slave stack directory path
	slaveStackRootPath = ORG_PATH.split(lastDirectory)[0]
	for (root, dirs, fileNames) in os.walk(ORG_PATH):
		for fileName in fileNames:
			relativeFilePath = os.path.join(root,fileName)
			#Replace the module path from the Root path with empty string
			file = relativeFilePath.replace(slaveStackRootPath, "")
			sepSSCDir = file[file.find(os.path.sep):]
			htmFile = sepSSCDir.replace(os.path.sep, "",1)
			srcFile = htmFile.rfind(".c")
			headerFile = htmFile.rfind(".h")
			drvFile = htmFile.find("drv_",0,4)
			if drvFile !=  -1:
				continue
			if headerFile != -1:
				srcFileFound = 0
			elif srcFile != -1:
				srcFileFound = 1
			# Get the ssc file symbol and each symbol is for the each file
			sscListFile = createSSCFileSymbol(count)
			# To allow the web pages outside the EtherCAT repo
			sscListFile.setRelative(False)
			#Set the source path
			sscListFile.setSourcePath(relativeFilePath)
			sscListFile.setOutputName(htmFile)
			fileList = file.split(os.path.sep)
			#set the destination path , the location where the ssc file will be copied
			destPath = ".."+os.path.sep+".."+os.path.sep+"slave_stack"
			sscListFile.setDestPath(destPath)
			fileList = fileList[0:len(fileList)-1]
			fileList[0] = "slave_stack"
			folderPath = ""
			for fileStr in fileList:
				folderPath += fileStr+os.path.sep
			#set the project path , ssc diretory will be added to the project	
			sscListFile.setProjectPath(folderPath)
			if srcFileFound == 1:
				sscListFile.setType("SOURCE")
			else:
				sscListFile.setType("HEADER")
			sscListFile.setEnabled(True)
			count += 1



#ORG_PATH = "../src/web_pages"
ORG_PATH = Module.getPath() + "slave_stack"
etherCATSSCDirSymbol = etheercatSlaveStackcodeDirPath.getValue()
ORG_PATH = etherCATSSCDirSymbol
count = 0

#mytcpipHttpNetComponent = etherCatComponent
symbolList = []
fileCount = 0
MAX_NUMBER_ssc_FILES = 100
del symbolList[:]

#Create MAX_NUMBER_ssc_FILES file symbols during the instantiation . 
#use of createFileSymbol() is not possible during the dynamic configuration of ssc path configuration
#So due to that we create a max number of ssc files during componet instatiation

for fileCount in range(MAX_NUMBER_ssc_FILES):
	sscSymbolStr = "SSC_LIST_FILE"+str(fileCount)
	mySym = etherCatComponent.createFileSymbol(sscSymbolStr, None)
	mySym.setEnabled(False)
	symbolList.append(mySym)
	fileCount +=1

#default webapge path and diretory parsing
sscPathParsing(ORG_PATH)
