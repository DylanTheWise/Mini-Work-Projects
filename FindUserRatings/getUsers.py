entries = []

#the file train.csv is expected
f = open('AppendMasterUserFile.txt','r')
for line in f:
    entries.append(line.strip().split(','))

f.close()

entriesCopy = []

for i in range(len(entries)):
	if int(entries[i][1]) >= 100 and int(entries[i][1]) <= 200:
		entriesCopy.append(entries[i][0] + '\n')


f = open('userList.txt', 'w')
f.writelines(entriesCopy)
f.close()
