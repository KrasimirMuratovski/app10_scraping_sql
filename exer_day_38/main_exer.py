from datetime import datetime
import time
import requests as re
import selectorlib
import sqlite3
connection = sqlite3.connect('exer_38.db')


URL = 'https://automated.pythonanywhere.com/'
HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
	repsonse = re.get(url, headers = HEADERS)
	source = repsonse.text
	return source


def extractor(source):
	extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
	value = extractor.extract(source)["tours"]
	return value

### WRITE IN FILE
# def write_in_file(content):
# 	with open("storage.txt", 'a') as f:
# 		f.write(content)

def write_db(content):
	cursor = connection.cursor()
	col1, col2 = content
	cursor.execute("INSERT INTO exer VALUES(?,?)",(col1,col2))
	connection.commit()

def read_from_file():
	with open("storage.txt", 'r') as f:
		content = f.read()
	return content

def time_stamp():
	today = datetime.now()
	stamp = today.strftime("%y-%m-%d %H-%M-%S")
	return stamp

if __name__ == "__main__":
	while True:
		scraped = scrape(URL)
		extracted = extractor(scraped)
		timestamp = time_stamp()
		content = (extracted, timestamp)
		# content = f"{extracted}, {timestamp}\n"
		col1, col2 = content
		print(col1, col2)
		# write_in_file(content)
		write_db(content)
		print(content)
		time.sleep(3)
