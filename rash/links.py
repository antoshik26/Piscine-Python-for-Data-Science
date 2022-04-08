import re
from collections import Counter
from enum import Enum
import urllib
import requests
from bs4 import BeautifulSoup
import ssl
class Links:
	"""
	Analyzing data from links.csv
	"""
	def __init__(self, path_to_the_file):
		"""
		Put here any fields that you think you will need.
		"""
		data = []
		# проверка на открытие файла
		with open(path_to_the_file, 'r') as f:
			str_data = (f.read().lower())
		data = str_data.split('\n')
		next_data = []
		for i in data[1:len(data) - 1]:
			data = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", i)
			# next_data.append(movieId, imdbId, tmdbId)
			next_data.append(data)
		# print(next_data)
		self.data_file = next_data

	def get_imdb(list_of_movies, list_of_fields):
		"""
		The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
		For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
		The values should be parsed from the IMDB webpages of the movies.
		Sort it by movieId descendingly.
		"""
		# for i in self.data_teg
		ssl._create_default_https_context = ssl._create_unverified_context
		url = f'https://www.imdb.com/title/tt{list_of_movies[0]}/'
		headers = {'User-Agent': 'My User Agent 1.0',
		'From': f'https://www.imdb.com/title/tt{list_of_movies[0]}/'
		}
		page = urllib.request.urlopen(urllib.request.Request(url=url, headers=headers)).read()
		# page_parsed = BeautifulSoup(page, 'html.parser')
		soup = BeautifulSoup(page, 'lxml')
		# presentation
		tags = soup.find_all('li', role='presentation', class_='ipc-metadata-list__item')
		# tags = soup.find_all('a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
		for tag in tags:
			print(" ".join(tag.text.split()))
		# ipc-metadata-list-item__list-content-item
		# ipc-metadata-list-item__list-content-item
		# ipc-metadata-list-item__list-content-item
		# return imdb_info
		
	def top_directors(self, n):
		"""
		The method returns a dict with top-n directors where the keys are directors and 
		the values are numbers of movies created by them. Sort it by numbers descendingly.
		"""
		return directors
		
	def most_expensive(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are their budgets. Sort it by budgets descendingly.
		"""
		return budgets
		
	def most_profitable(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are the difference between cumulative worldwide gross and budget.
		Sort it by the difference descendingly.
		"""
		return profits
		
	def longest(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are their runtime. If there are more than one version â€“ choose any.
		Sort it by runtime descendingly.
		"""
		return runtimes
		
	def top_cost_per_minute(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
	the values are the budgets divided by their runtime. The budgets can be in different currencies â€“ do not pay attention to it. 
		The values should be rounded to 2 decimals. Sort it by the division descendingly.
		"""
		return costs

link = Links("/goinfre/dmadelei/ml-latest-small/links.csv")
Links.get_imdb(['0114709'], ['0114709'])