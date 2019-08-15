#variable names simplified 

import csv

nist_path = 'XXXX'
output_path = 'XXXX'

ids = []
scores = []
id_list = []
subcats = []
nist_dict = {}
fp = open(nist_path, 'r')
csv_reader = csv.DictReader(fp, delimiter=',')
for row in csv_reader:
	ids.append(row['Question ID'])
	nist_dict.update({row['Question ID'] : row['XXXX']})
ids = sorted(ids)

for elem in ids:
	_id = elem.split('-')
	if(_id[0] not in id_list):
		id_list.append(_id[0])
	subcat = _id[0] + '-' + _id[1]
	if(subcat not in subcats):
		subcats.append(subcat)
#print(subcats)
fp.close()
categories = {}
start = 0
for subcat in subcats:
	count = 0
	score = 0
	for idx in range(start, len(ids)):
		if(subcat in ids[idx]):
			if(nist_dict.get(ids[idx]) != ''):
				count += 1
				score += int(nist_dict.get(ids[idx]))
			else:
				count += 1
				score += 1
		else:
			start = idx
			break
	if(count != 0):
		average = score / count
		categories.update({subcat : '{0:.2f}'.format(average)})
print(categories)
f = open(output_path, 'w')
for key,val in categories.items():
	string = key + '    ' + val
	f.write(string)
	f.write('\n')
