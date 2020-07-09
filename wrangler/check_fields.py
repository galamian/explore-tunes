import sys
from dictionarize import abc_to_dictionary

tuid_from, tuid_to = 1, 1

if len(sys.argv)>1:
	tuid_from = int(sys.argv[1]) if sys.argv[1] else 1
	if len(sys.argv)>2:
		tuid_to = int(sys.argv[2]) if sys.argv[2] else tuid_from	
else:
	print('no tune_ids passed as parameter')

columnNames = []

for tuid in range(tuid_from, tuid_to):
    filename = '../data/raw/' + str(tuid) + '.abc'
    
    dic = abc_to_dictionary(filename)

    for key in dic.keys():
            if not key in columnNames:
                columnNames.append(key)

print(columnNames)