import os
import re
import string

def main():

    teamVector = []
    teamAbbreviationVector = []
    listOfWins = []

    allTeams = []

    fileString = open("schools.txt", 'r').read()
    allTeams = re.findall("(.*?),(.*)" , fileString)

    #use our master list of teams and abbreviations to create
    #lists that contain such data
    for i in range(len(allTeams)):
        teamVector.append(allTeams[i][0])
        teamAbbreviationVector.append(allTeams[i][1])

    #make wins for all teams 0
    for i in range(len(teamAbbreviationVector)):
        listOfWins.append(0)

    os.chdir("ScheduleDayCache")
    listOfFiles = os.listdir()

    #go through each file in directory
    for i in range(len(listOfFiles)):

        #grab all game scores for that day
        listOfAbbreviationsAndScores = re.findall('href="/mens-college-basketball/.*?gameId=\d+">(.*?) (\d+), (.*?) (\d+)', open(listOfFiles[i]).read())
        #print(listOfFiles[i])

        #go through each game that day
        for i in range(len(listOfAbbreviationsAndScores)):

            skipGame = False

            #if the game was suspended, skip it
            if listOfAbbreviationsAndScores[i][0][:9] == "Suspended":
                skipGame = True


            if skipGame == False:

                #assign teams and scores
                team1 = listOfAbbreviationsAndScores[i][0]
                team2 = listOfAbbreviationsAndScores[i][2]

                score1 = listOfAbbreviationsAndScores[i][1]
                score2 = listOfAbbreviationsAndScores[i][3]

                #find larger score and iterate team win
                if int(score1) > int(score2):

                    #if the team is not in the directory, skip
                    if team1 in teamAbbreviationVector:
                        winnerLocation = teamAbbreviationVector.index(team1)
                        listOfWins[winnerLocation] = listOfWins[winnerLocation] + 1

                else:
                    if team2 in teamAbbreviationVector:
                        winnerLocation = teamAbbreviationVector.index(team2)
                        listOfWins[winnerLocation] = listOfWins[winnerLocation] + 1

            #if skipGame == False


         #for i in range(len(listOfAbbreviationsAndScores)):  END

    #for i in range(len(listOfFiles)):  END

    #open file and change 'prints' to 'writes'

    #RFile = open("ncaapicks.R", 'w')

    #listOfGroups        list of groups for teams
    #listOfGroupRanks    list of ranks within group

    #for i in range(len(listOfGroups)):

        #RFile.write('teamsc("')
        #for k in range(len(listOfGroups[i])):

            #RFile.write(listOfGroups[i][k]
            #RFile.write(" (")
            #RFile.write(listOfGroupRanks[i][k])

            #if k != range(len(listOfGroups[i])) - 1:
                #RFile.write(')", "')

            #else:
                #RFile.write(')")')

        #print()


    #listOfGroupScoresAllRounds

    #for i in range(len(listOfGroupScoresAllRounds)):
        #RFile.write("correctvec")
        #RFile.write(i)
        #RFile.write("=NULL\n")
        
        #for k in range(len(listOfGroupScoresAllRounds[i])):
            #RFile.write("correctvec")
            #RFile.write(i)
            #RFile.write("=c(correctvec")
            #RFile.write(i)
            #RFile.write(",")

            #for j in range(len(listOfGroupScoresAllRounds[i][k]):
                #if j != range(len(listOfGroupScoresAllRounds[i][k])) - 1:
                    #RFile.write(listOfGroupScoresAllRounds[i][k][j])
                    #RFile.write(",")

                #else:
                    #RFile.write(listOfGroupScoresAllRounds[i][k][j])
                    #RFile.write(")\n")

        #RFile.write("")

    #Individual picks

    #RFile.write("allbracketnames=bracketnames")
    #RFile.write("rm(bracketnames)")
    #RFile.write("allbracketpicks=bracketpicks")
    #RFile.write("rm(bracketpicks)")
    #RFile.write("")
    #RFile.write("")
    #RFile.write('temp=read.csv("divisions.csv")')
    #RFile.write("divisionnames=colnames(temp)")
    #RFile.write("indiv=as.matrix(temp)")
    #RFile.write("rm(temp)")


    #create lines for file in list
    listOfFileLines = []
    for i in range(len(teamAbbreviationVector)):
        listOfFileLines.append(teamAbbreviationVector[i] + "," + str(listOfWins[i]) + '\n')

    #write lines to file
    os.chdir('..')
    outFile = open("winnerFile.txt", 'w')
    outFile.writelines(listOfFileLines)

main()