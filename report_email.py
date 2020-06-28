#!/usr/bin/env python3

import reports
import emails
from datetime import datetime
import os
import getpass

def get_paragraph():
	path = 'supplier-data/descriptions/'
	files = os.listdir(path)
	fruits = {}

	for file_name in files:
		with open(path + file_name) as file:
			fruit_name = file.readline()
			fruit_weight = file.readline()
			fruits[fruit_name] = fruit_weight
		file.close()

	table_data = []
	for k, v in fruits.items():
		table_data.append(['name: ' + k + 'weight: ' + v])

	return table_data

def main():
	attachment = "/tmp/processed.pdf"
	paragraph = get_paragraph()
	today = datetime.now().date()
	title = "Processed Update on {}".format(today.strftime("%B %d, %Y"))
	reports.generate_report(attachment, title, paragraph)

	sender = 'automation@example.com'
	receiver = getpass.getuser() + '@example.com'
	subject = 'Upload Completed - Online Fruit Store'
	body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

	email = emails.generate_email(sender, receiver, subject, body, attachment)
	emails.send_email(email)

if __name__ == "__main__":
	main()
