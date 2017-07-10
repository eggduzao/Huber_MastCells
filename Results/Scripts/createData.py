# Import
import os
import sys

# Input
promoterFileName = sys.argv[1]
outputLocation = sys.argv[2]

# Parameters
windowList = [200,500,1000]

# Iterating on inputFile
promoterName = promoterFileName.split("/")[-1].split(".")[0]
promoterFile = open(promoterFileName,"r")
outputFileList = [open(outputLocation+promoterName+"_"+str(e)+".bed","w") for e in windowList]
for line in promoterFile:
    ll = line.strip().split("\t")
    for i in range(0,len(windowList)):
        if(ll[4] == "+"):
            p1 = str(int(ll[1])-windowList[i])
            p2 = ll[1]
        else:
            p1 = ll[1]
            p2 = str(int(ll[1])+windowList[i])
        outputFileList[i].write("\t".join([ll[0],p1,p2])+"\n")

# Termination
promoterFile.close()
for e in outputFileList: e.close()

""" CREATE DATA OLD ###############################################################################
###################################################################################################

# Import
import os
import sys

# Input
inputFileName = sys.argv[1]
promoterFileName = sys.argv[2]
outputLocation = sys.argv[3]

# Parameters
windowList = [200,500,1000]

# Creating promoterDict
promoterDict = dict()
promoterFile = open(promoterFileName,"r")
for line in promoterFile:
    ll = line.strip().split("\t")
    promoterDict[ll[3]] = ll[0:3]+[ll[4]]
promoterFile.close()

# Iterating on inputFile
inputName = inputFileName.split("/")[-1].split(".")[0]
inputFile = open(inputFileName,"r")
outputFileList = [open(outputLocation+str(e)+"/"+inputName+".bed","w") for e in windowList]
outputErrorFile = open(outputLocation+inputName+"_error.txt","w")
for line in inputFile:

    # Reading gene
    gene = line.strip()
    if(gene not in promoterDict.keys()):
        outputErrorFile.write(gene+"\n")
        continue
    geneL = promoterDict[gene]
    
    # Writing different window lengths
    for i in range(0,len(windowList)):
        chrName = geneL[0]
        if(geneL[3] == "+"):
            p1 = str(int(geneL[1])-windowList[i])
            p2 = geneL[1]
        else:
            p1 = geneL[1]
            p2 = str(int(geneL[1])+windowList[i])
        outputFileList[i].write("\t".join([chrName,p1,p2])+"\n")

# Termination
inputFile.close()
for e in outputFileList: e.close()
outputErrorFile.close()
###################################################################################################
###################################################################################################
"""


