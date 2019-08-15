'''
first attempt at automating a daily emaily that the team gates
for future reference - https://stackoverflow.com/questions/22813814/clearly-documented-reading-of-emails-functionality-with-python-win32com-outlook
'''
import win32com.client as win32
from unidecode import unidecode
from datetime import datetime

#open inbox
outlook = win32.Dispatch('Outlook.Application').GetNamespace('MAPI')
inbox_folder = outlook.GetDefaultFolder(6) #6 is inbox folder
num_attacks = 0
num_infected = 0
for messages in reversed(inbox_folder.Items):
	if messages.SenderEmailAddress == 'XXXX':
		html_text = messages.HTMLBody
		#get number of attacks from the new email
		attacks_start_string = 'XXXX' 
		attacks_start = html_text.find(attacks_start_string)
		attacks_start += (len(attacks_start_string))
		attacks_end_string = 'XXXX'
		attacks_end = html_text.find(attacks_end_string, attacks_start)
		num_attacks = html_text[attacks_start:attacks_end]
		#get the number of infected UE's from the new email
		malware_string = 'XXXX'
		malware_start = html_text.find(malware_string, attacks_end)
		malware_start += (len(malware_string))
		malware_end = html_text.find('XXXX', malware_start)
		num_infected = html_text[malware_start:malware_end]
		break

for messages in reversed(inbox_folder.Items):
	if messages.SenderName == 'XXXX':
		html_text = messages.HTMLBody
		#get the old number of attacks
		attacks_start_string = 'XXXX'
		attacks_start = html_text.find(attacks_start_string)
		attacks_start += (len(attacks_start_string))
		old_attacks_end = html_text.find('XXXX', attacks_start)
		old_num_attacks = html_text[attacks_start:old_attacks_end]
		#get the old number of infected UE's
		malware_string = 'XXXX'
		malware_start = html_text.find(malware_string, old_attacks_end)
		malware_start += (len(malware_string))
		malware_end = html_text.find('XXXX', malware_start)
		old_num_infected = html_text[malware_start:malware_end]
		#craft new attack string 
		old_attacks_string = attacks_start_string + old_num_attacks
		new_attacks_string = attacks_start_string + num_attacks
		#craft new malware string
		old_malware_string = malware_string + old_num_infected
		new_malware_string = malware_string + num_infected
		#replace the 
		new_html_msg = messages.HTMLBody.replace(old_attacks_string, new_attacks_string)
		new_html_msg_2 = new_html_msg.replace(old_malware_string, new_malware_string)
		#create a new email
		mail_send = win32.Dispatch('outlook.application')
		mail = mail_send.CreateItem(0)
		mail.Attachments.Add('XXXX') 
		#get name of image attachment
		img_start = new_html_msg_2.find('src="cid:')
		img_start += len('src="cid:')
		img_end = new_html_msg_2.find('"', img_start+1)
		img_name = new_html_msg_2[img_start:img_end]
		old_img_name = 'src="cid:' + img_name + '"'
		new_img_name = 'src="cid:test_img.jpg"'
		#replace image attachment with local image
		final_html_msg = new_html_msg_2.replace(old_img_name, new_img_name)
		mail.To = 'XXXX'
		date = datetime.today().strftime('%m/%d/%Y')
		mail.Subject = 'XXXX ' + date
		mail.BodyFormat = 2 #2 forces the body to be of html format
		mail.HTMLBody = final_html_msg
		mail.Send()
		break

