'''
Sensitive information replaced with XXXX
Takes a .csv as input and outputs a .csv with information that the network security team can
use to determine health of various elements
'''

import csv
from datetime import datetime 
#for formatting purposes to make the output csv look pretty
def add_rows(num_rows, modify_list):
	rows = len(modify_list)
	row_dif = num_rows - rows
	if row_dif == 0:
		return
	while True:
		if rows == num_rows:
			break
		row = [' ', ' ']
		modify_list.append(row)
		rows += 1
	return

'''
file_input = 'input.csv'
file_output = 'output.csv'
'''
file_input = input("Enter name of file (include extension): ")
if('.csv' not in file_input):
    print('Error, please include file extension')
    quit()
file_output = input("Enter name of output file (include extension): ")
if('.csv' not in file_output):
    print('Error, please include file extension')
    quit()  
#variables names modified to be more general
element1_list = [['Header 1', ' '], ['Host', 'Last Seen']]
element2_list = [['Header 2', ' '], ['Host', 'Last Seen']]
element3_list = [['Header 3', ' '],['Host', 'Last Seen']]
element4_list = [['Header 4', ' '],['Host', 'Last Seen']]
element5_list = [['Header 5', ' '],['Host', 'Last Seen']]
element6_list = [['Header 6', ' '],['Host', 'Last Seen']]
element7_list = [['Header 7', ' '],['Host', 'Last Seen']]
element8_list = [['Header 8', ' '],['Host', 'Last Seen']]
element9_list = [['Header 9', ' '],['Host', 'Last Seen']]

with open(file_input, mode = 'r') as f:
    csv_reader = csv.DictReader(f, delimiter=',')
    for row in csv_reader:
    	log_host = row['Host']
    	if('XXXX' in log_host):
    		time = row['Last Message']
    		time = time.split(' ')
    		date = time[0]
    		formatting = [log_host, date]
    		element1_list.append(formatting)
    	if('XXXX-' in log_host):
    		time = row['Last Message']
    		time = time.split(' ')
    		date = time[0]
    		formatting = [log_host, date]
    		element2_list.append(formatting)
    	if('XXXX' in log_host or 'XXXX' in log_host):
    		time = row['Last Message']
    		time = time.split(' ')
    		date = time[0]
    		formatting = [log_host, date]
    		element3_list.append(formatting)
    	if('XXXX' in log_host):
    		time = row['Last Message']
    		time = time.split(' ')
    		date = time[0]
    		formatting = [log_host, date]
    		element4_list.append(formatting)
    	if('XXXX' in log_host):
    		time = row['Last Message']
    		time = time.split(' ')
    		date = time[0]
    		formatting = [log_host, date]
    		element5_list.append(formatting)
    	if('XXXX' in log_host):
    		time = row['Last Message']
    		time = time.split(' ')
    		date = time[0]
    		formatting = [log_host, date]
    		element6_list.append(formatting)
    	if('entdns' in log_host):
    		time = row['Last Message']
    		time = time.split(' ')
    		date = time[0]
    		formatting = [log_host, date]
    		element7_list.append(formatting)
    	if('XXXX' in log_host):
    		time = row['Last Message']
    		time = time.split(' ')
    		date = time[0]
    		formatting = [log_host, date]
    		element8_list.append(formatting)
    	if('XXXX' in log_host):
    		time = row['Last Message']
    		time = time.split(' ')
    		date = time[0]
    		formatting = [log_host, date]
    		element9_list.append(formatting)

element1_list[2:] = sorted(element1_list[2:], key = lambda x: x[1])
element2_list[2:] = sorted(element2_list[2:], key = lambda x: x[1])
element3_list[2:] = sorted(element3_list[2:], key = lambda x: x[1])
element4_list[2:] = sorted(element4_list[2:], key = lambda x: x[1])
element5_list[2:] = sorted(element5_list[2:], key = lambda x: x[1])
element6_list[2:] = sorted(element6_list[2:], key = lambda x: x[1])
element7_list[2:] = sorted(element7_list[2:], key = lambda x: x[1])
element8_list[2:] = sorted(element8_list[2:], key = lambda x: x[1])
element9_list[2:] = sorted(element9_list[2:], key = lambda x: x[1])

max_len = max(len(element1_list), len(element2_list), len(element3_list), len(element4_list), 
	len(element5_list), len(element6_list), len(element7_list), len(element8_list), len(element9_list))

list_of_lists = [element1_list, element2_list, element3_list, element4_list, element5_list, element6_list, 
				element7_list, element8_list, element9_list]

for x in list_of_lists:
	add_rows(max_len, x)

idx = 0
final_list = []
while idx != max_len:
	formatting = [element1_list[idx][0], element1_list[idx][1], element2_list[idx][0], element2_list[idx][1], 
	element3_list[idx][0], element3_list[idx][1], element4_list[idx][0], element4_list[idx][1], element5_list[idx][0], element5_list[idx][1],
	element6_list[idx][0], element6_list[idx][1], element7_list[idx][0], element7_list[idx][1], 
	element8_list[idx][0], element8_list[idx][1], element9_list[idx][0], element9_list[idx][1]]
	final_list.append(formatting) 
	idx += 1

with open(file_output, 'w', newline="") as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(final_list)
csvFile.close()
