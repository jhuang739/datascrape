import urllib2
from bs4 import BeautifulSoup
import csv

def create_html(link):
	page = urllib2.urlopen(link)
	html = BeautifulSoup(page, 'html.parser')
	return html

def get_title(link):
	html = create_html(link)
	unref_title = html.find('h1', attrs = {'id': 'artTitle'})
	title = unref_title.text.strip() 		
	return title

def get_DOI(link):
	html = create_html(link)
	unref_DOI = html.find('li', attrs = {'id': 'artDoi'}) 
	DOI = unref_DOI.text.strip() 
	ref_DOI = DOI[16: 23]
	return ref_DOI

def get_authors(link):
	num_authors = 0 
	final_author = '' 
	author_present = True
	html = create_html(link)

	while(author_present):
		unref_author = html.find('a', attrs = {'data-author-id': str(num_authors),'class': 'author-name'})
		if unref_author is None:					#if no further author found
			author_present = False
			break
		author = unref_author.text.strip()
		ref_author = ''
		for ch in author:
			if ch.isalpha() or ch.isspace():		#get rid of non-alpha chars, leave space between first/last name
				ref_author += ch
		if(num_authors != 0):
			final_author += ', ' + ref_author
		else:
			final_author = ref_author
		num_authors = num_authors + 1
	return final_author

def setup_data(link):
	data_row = []
	data_row.append(get_title(link))
	data_row.append(get_DOI(link))
	data_row.append(get_authors(link))
	return data_row

def print_article_info(links):						#@param: array of links
	headers = ['Paper Title', 'DOI', 'Author(s)']
	data = []
	for link in links:
		data.append(setup_data(link))

	with open('data.csv', 'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(headers)
		for row in data:
			writer.writerow(row)

"""-------- TEST --------"""
webpage = ["http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0171252"]
print_article_info(webpage)