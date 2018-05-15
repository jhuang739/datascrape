import urllib2
from bs4 import BeautifulSoup
import csv

webpage = ["http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0171252"]
data = []
for pg in webpage:
	page = urllib2.urlopen(pg)
	parsedpage = BeautifulSoup(page, 'html.parser')  #contains html of webpage
	unref_title = parsedpage.find('h1', attrs = {'id': 'artTitle'})
	title = unref_title.text.strip()  #title of article		
	print title
	data.append((title))

"""Export to Excel file"""
with open('data.csv', 'a') as csv_file:  #syntax error
	writer = csv.writer(csv_file)
	writer.writerow("title")
	for title in data:
		writer.writerow([title])  #add column to excel file