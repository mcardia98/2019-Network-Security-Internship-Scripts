'''
Quick script to parse a .csv file containing vendor VPNs.
Input: csv export 
Output: .csv that contains active VPN users and active vendors within the specified time range
		that was chosen for the csv output

See writeup for how to use the script
'''

import csv
file_input = input("Enter name of file (include extension): ") 
if('.csv' not in file_input):
	print('Error, please include file extension')
	quit()
file_output = input("Enter name of output file (include extension): ")
if('.csv' not in file_output):
	print('Error, please include file extension')
	quit()	

user_list = []
vendor_list = []
active_vendors = [['Active Vendors']]
active_vendors_list = []
with open(file_input, mode = 'r') as f:
    csv_reader = csv.DictReader(f, delimiter=',')
    for row in csv_reader:
            if not(row["XXXX"] in user_list):
            	user_list.append(row["XXXX"])
            	vendor_list.append(row["XXXX"])
            	if not(row["XXXX"] in active_vendors_list):
            		active_vendors_list.append(row["XXXX"]) 

user_and_company = [['Active Users', 'User\'s Vendor']]
for users, vendors in zip(user_list, vendor_list):
	formmating = [users, vendors]
	user_and_company.append(formmating)

for vendors in active_vendors_list:
	formmating = [vendors]
	active_vendors.append(formmating)

with open(file_output, 'w', newline="") as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(user_and_company)
	writer.writerows('\n')
	writer.writerows(active_vendors) 
csvFile.close()
