#final version for automating an email that the team gets every day

#libraries
#web driver (need selenium because of Java Script)
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#html parser
from bs4 import BeautifulSoup as bs 
#ssh library
import paramiko
#date library
from datetime import datetime, timedelta
#email library
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#splunk libraries
import splunklib.client as splunk_client
from time import sleep
import time
import splunklib.results as results

#Java Script Table parser
#@@Functionality: 	Takes a web page that contains a Java Script table and parses the table.  Stores data in the table
#					in a list that is passed in by reference
#@@Params: 			Web page that has a Java Script table that we wish to parse
#					List that we wish to store table data in
#@@Return: 			None, pass by reference
def table_parser(page, infections):
	data = []
	soup = bs(page, 'html.parser')
	table = soup.find('table', attrs = {'class' : 'dashboard-table'})
	table_body = table.find('tbody')
	rows = table_body.find_all('tr')
	for row in rows:
		cols = row.find_all('td')
		for col in cols:
			data.append(col.get_text())
	for x in range(0, len(data), 2):
		name = data[x]
		name = name[2:]
		name = name.split(' -')
		name = name[0]
		string = data[x+1] + ' - ' + name
		infections.append(string)

#Splunk API searcher
#@@Functionality:	Takes a splunk search query and returns the result
#@@Params:			Search query that you wish to execute
#@@Return:			Search result
def splunk_search(search_query):
	kwargs_search = {'exec_mode': 'normal'}
	job = service.jobs.create(search_query, **kwargs_search)
	while True:
		while not job.is_ready():
			pass
		if job['isDone'] == '1':
			break
		sleep(2)
	for result in results.ResultsReader(job.results()):
		job.cancel()
		return result['count']
		
#file paths
driver_path = 'XXXX'
private_key_path = 'XXXX'
local_file_path = 'XXXX'
email_template_path = 'XXXX'
email_img_path = 'XXXX'
splunk_password = 'XXXX'
#variables that we are going to be using in order to construct the email 
num_infected = 0
malware_infections = []
ddos_attacks = 0
wip = 0
aepp = 0
waf = 0
iam = 0

#web scrape the new netguard box
#options for a headless browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
driver = webdriver.Chrome(executable_path=driver_path, options = chrome_options)
driver.get('XXXX')
username = driver.find_element_by_id('XXXX')
password = driver.find_element_by_id('XXXX')
username.send_keys('XXXX')
password.send_keys('XXXX')
driver.find_element_by_id('XXXX').click()

#@@DEBUG print('scraping table info')
#parse the table and collect data
table_parser(driver.page_source, malware_infections)
#@@DEBUG print('table scrapped')

#get daily number of infections
driver.find_element_by_id('XXXX').click()

#sometimes the data does not load right away, so delay until present 
delay = 5
time.sleep(2)
try:
	elem_present = EC.presence_of_element_located((By.ID, 'XXXX'))
	WebDriverWait(driver, delay).until(elem_present)
except:
	"Page Time Out"

#collect the total number of infected for the day
#@@DEBUG print('scraping total number of infected')
page = driver.page_source
soup = bs(page, 'html.parser')
num_infected = soup.select('XXXX')[0].text
num_infected = num_infected[XXXX:]
num_infected = num_infected.split(' ')
num_infected = num_infected[0]

#logout
driver.find_element_by_id('XXXX').click()

#use scp to get DDoS info from XXXX
key = paramiko.RSAKey.from_private_key_file(private_key_path)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname = 'XXXX', username = 'XXXX', pkey = key)

#day month year format
#@@DEBUG print('getting DDoS info')
date = datetime.today()# - timedelta(days = 1) #run today's count instead of yesterdays due to report not running on weekends
year = date.strftime('%Y')
day = date.strftime('%d%m')
year = year[2:]
date = day + year
file_name = 'XXXX' + date + 'XXXX'
remote_file_path = 'XXXX' + file_name
ftp_client = client.open_sftp()
ftp_client.get(remote_file_path, local_file_path)
ftp_client.close()
ddos_file = open(local_file_path, 'r')
ddos_string = ddos_file.read()
ddos_attacks = ddos_string.strip('XXXX')
#@@DEBUG print('starting splunk searches')
#get Splunk info
service = splunk_client.connect(host = 'XXXX', port = XXXX, username = 'XXXX', password = splunk_password)
searchquery = 'XXXX'
splunk1 = splunk_search(searchquery)
#@@DEBUG print('first splunk search')
searchquery = 'XXXX'
splunk2 = splunk_search(searchquery)
#@@DEBUG print('second splunk search')
searchquery = 'XXXX'
splunk3 = splunk_search(searchquery)
#@@DEBUG print('fourth splunk search')
searchquery = 'XXXX'
splunk4 = splunk_search(searchquery)
#@@DEBUG print('finished splunk searches')
#compose email
email_template = open(email_template_path, 'r')
email_template_string = email_template.read()
email_template.close()
email_template_string = email_template_string.replace('replace1', ddos_attacks, 1) #replace only once because was messing up replace10
email_template_string = email_template_string.replace('replace2', num_infected, 1)
email_template_string = email_template_string.replace('replace3', malware_infections[0], 1)
email_template_string = email_template_string.replace('replace4', malware_infections[1], 1)
email_template_string = email_template_string.replace('replace5', malware_infections[2], 1)
email_template_string = email_template_string.replace('replace6', malware_infections[3], 1)
email_template_string = email_template_string.replace('replace7', malware_infections[4], 1)
email_template_string = email_template_string.replace('replace8', splunk1, 1)
email_template_string = email_template_string.replace('replace9', splunk2, 1)
email_template_string = email_template_string.replace('replace10', splunk3, 1)
email_template_string = email_template_string.replace('replace11', splunk4, 1)

#send email
sender = 'XXXX'
recipient = 'XXXX'
msg = MIMEMultipart('related')
date = datetime.today().strftime('%m/%d/%Y')
msg['Subject'] = 'XXXX ' + date
msg['From'] = sender
msg['To'] = recipient
part = MIMEText(email_template_string, 'html')
msg.attach(part)
fp = open(email_img_path, 'rb')
msg_img =MIMEImage(fp.read())
fp.close()
msg_img.add_header('Content-ID', '<image1>')
msg.attach(msg_img)
server = smtplib.SMTP('XXXX')
server.sendmail(sender, recipient, msg.as_string())
server.quit()
#print('done')