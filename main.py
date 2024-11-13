import sqlite3

import requests as re
import selectorlib
import smtplib, ssl
import os
import time

connection = sqlite3.connect("data.db")


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
	row = extracted.split(", ")
	cursor = connection.cursor()
	cursor.execute("INSERT INTO events VALUES(?,?,?)", row)



# def store(extracted): ## STORE IN TEXT FILE
# 	with open("data.txt", 'a') as file:
# 		file.write(extracted + '\n')


# def read(): ##Read from text file
# 	with open("data.txt", 'r') as file:
# 		file_content = file.read()
# 	return file_content

def read(extracted):
	row = extracted.split(", ")
	# band, city, date = row[0], row[1], row[2]
	band, city, date = row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM events WHERE band=? AND city = ? AND date = ?", (band, city, date))
	rows = cursor.fetchall()
	print(rows)
	return rows

if __name__ == '__main__':
	while True:
		scraped = scrape(URL)
		extracted = extract(scraped)
		print(extracted)

		to_send = "Subject: Scrapped" + '\n'
		if extracted != "No upcoming tours":
			row = read(extracted)
			if not row:
				store(extracted)
				to_send = to_send + extracted
				send_email(to_send)
		time.sleep(5)
