#!/usr/bin/env python3

import shutil
import psutil
import emails
import getpass
import socket

def send_system_mail(subject):
	sender = 'automation@example.com'
	receiver = getpass.getuser() + '@example.com'
	body = 'Please check your system and resolve the issue as soon as possible'
	message = emails.generate_email(sender, receiver, subject, body)
	emails.send_email(message)

if psutil.cpu_percent() > 80:
	subject = 'Error - CPU usage is over 80%'
	send_system_mail(subject)

disk_usage = shutil.disk_usage('/')
free_disk_space = disk_usage[2] * 100 / disk_usage[0]

if free_disk_space < 20:
	subject = 'Error - Available disk space is less than 20%'
	send_system_mail(subject)
	
memory = psutil.virtual_memory()
available_memory = ((memory[1] / 1024) / 1024)

if available_memory < 500:
	subject = 'Error - Available memory is less than 500MB'
	send_system_mail(subject)

try:
	localhost = socket.gethostbyname('localhost')
	if localhost != '127.0.0.1':
		raise socket.gaierror()
except socket.gaierror:
	subject = 'Error - localhost cannot be resolved to 127.0.0.1'
	send_system_mail(subject)
