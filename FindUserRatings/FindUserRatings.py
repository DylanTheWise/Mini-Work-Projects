from math import floor
import urllib.request
import html
import re


f = open('userList.txt', 'r')

userList = []

#read in user list
userList = f.read().splitlines()

f.close()

# user,movieID,userRating,IMDBrating

#read in list of entries already done
entries = []

#the file train.csv is expected
f = open('dataList.txt','r')
for line in f:
    entries.append(line.strip().split(','))

f.close()

#grab all user names already done
usersAlreadyDone = []
for i in range(len(entries)):
    usersAlreadyDone.append(entries[i][0])

usersAlreadyDone = usersAlreadyDone[1:]

#convert into a set of unique elements
userList = set(userList)
usersAlreadyDone = set(usersAlreadyDone)

#do set subtraction
userList = userList - usersAlreadyDone

#convert back into list
userList = list(userList)


baseString = 'http://www.imdb.com/user/'

#eachPage contains 250 entires
iterateStringA =  '/ratings?start='
iterateStringB = '&view=compact&sort=ratings_date:desc'


for i in range(len(userList)):

    #open ratings page for user
    urlRequest = urllib.request.Request(baseString + 'ur' + userList[i] + iterateStringA + '1' + iterateStringB)
    urlRequest.add_header('User-Agent', 'Mozilla/5.0')
    firstPage = str(urllib.request.urlopen(urlRequest).read())

    print('Opening page number 1 for user ', end='')
    print(userList[i])

    #gather amount of ratings
    findNumOfRatings = re.findall('listSize: (\d+)', firstPage)

    #get all ratings on first page
    listOfMovieRatings = re.findall('class="title"><a href="/title/(\w+)/">.*?id="\w+\|your\|(\d+)\|(.*?)\|list"', firstPage, re.DOTALL)

    with open('dataList.txt', 'a') as f:
        for k in range(len(listOfMovieRatings)):
            f.write(userList[i] + ',' + listOfMovieRatings[k][0] + ',' + listOfMovieRatings[k][1] + ',' + listOfMovieRatings[k][2] + '\n')

    findNumOfPages = floor(int(findNumOfRatings[0])/250)

    #account for edge case
    if int(findNumOfRatings[0]) % 250 == 0:
        findNumOfPages = findNumOfPages - 1

    for k in range(findNumOfPages):

        #open rest of pages
        urlRequest = urllib.request.Request(baseString + 'ur' + userList[i] + iterateStringA + str(((k+1)*250)+1) + iterateStringB)
        urlRequest.add_header('User-Agent', 'Mozilla/5.0')
        newPage = str(urllib.request.urlopen(urlRequest).read())

        print('Opening page number ', end='')
        print(k+2, end=' ')
        print('for user ', end='')
        print(userList[i])

        listOfMovieRatings = re.findall('class="title"><a href="/title/(\w+)/">.*?id="\w+\|your\|(\d+)\|(.*?)\|list"', newPage, re.DOTALL)

        with open('dataList.txt', 'a') as f:
            for j in range(len(listOfMovieRatings)):
                f.write(userList[i] + ',' + listOfMovieRatings[j][0] + ',' + listOfMovieRatings[j][1] + ',' + listOfMovieRatings[j][2] + '\n')
