import requests as re
import selectorlib
import smtplib, ssl
import os
import time

PASSWORD = os.getenv('PASSWORD')
URL = 'https://programmer100.pythonanywhere.com/tours/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
	"""Scrape the page source"""
	response= re.get(URL, headers = HEADERS )
	source = response.text
	return source

def extract(source):
	extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
	value = extractor.extract(source)["tours"]
	return value


def send_email(message):
	host = "smtp.gmail.com"
	port = 465

	username = "koynarecam@gmail.com"
	password = PASSWORD

	receiver = "fragmantica.django@gmail.com"
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL(host, port, context=context) as server:
		server.login(username, password)
		server.sendmail(username, receiver, message)

def store(extracted):
	with open("data.txt", 'a') as file:
		file.write(extracted + '\n')


def read(check):
	with open("data.txt", 'r') as file:
		file_content = file.readlines()
	return file_content

if __name__ == '__main__':
	while True:
		scraped = scrape(URL)
		extracted = extract(scraped)
		print(extracted)

		content = read(extracted)
		to_send = "Subject: Scrapped" + '\n'
		if extracted != "No upcoming tours":
			if extracted not in content:
				store(extracted)
				to_send = to_send + extracted
				send_email(to_send)

		time.sleep(5)
