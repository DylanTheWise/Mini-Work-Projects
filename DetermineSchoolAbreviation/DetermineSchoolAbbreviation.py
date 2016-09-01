import os
import re


def main():

    mainDir = os.getcwd()

    scheduleDir = mainDir + "\\ScheduleDayCache\\"

    try: 
        os.makedirs(scheduleDir)
    except OSError:                    
        if not os.path.isdir(scheduleDir):
            raise

    os.chdir(scheduleDir)
    fileList = os.listdir(scheduleDir)

    listOfAbbreviations = []
    listOfSchools = []
    listOfLines = []

    for i in range(len(fileList)):

        fileString = open(fileList[i], 'r').read()

        matches = re.findall('href="/mens-college-basketball/team/_/id/\d+"><span>(.*?)</span> <abbr title=".*?">(.*?)</abbr></a></td><td', fileString)
        for k in range(len(matches)):
            skipEntry = False

            if matches[k][1] in listOfAbbreviations:
                skipEntry = True

            if skipEntry == False:
                listOfSchools.append(matches[k][0])
                listOfAbbreviations.append(matches[k][1])

    for i in range(len(listOfAbbreviations)):
        stringLine = listOfSchools[i] + "," + listOfAbbreviations[i] + "\n"
        listOfLines.append(stringLine)
    
    os.chdir(mainDir)
    outputFile = open('schools.txt', 'w')
    outputFile.writelines(listOfLines)

    return 0

main()