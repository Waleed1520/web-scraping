#imports
from bs4 import BeautifulSoup
import requests
import pandas as pd



#HTTP request
#store request in variable
website = 'https://www.udemy.com/course/beautiful-soup-in-action-web-scraping-a-car-dealer-website/learn/lecture/27992496#announcements'

#get request

response = requests.get(website)

#status code



#soup object
soup = BeautifulSoup(response.content,'html.parser')
print(soup)
#print(soup)

#results

results = soup.find_all('div',{'id':'intro'})
#print(results[0])

#TARGET NECESSARY DATA






