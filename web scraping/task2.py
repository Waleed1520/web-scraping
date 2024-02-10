#imports
from bs4 import BeautifulSoup
import requests
import pandas as pd

Name =[]
Price=[]
Rating=[]
Ratingcount=[]
Dealername=[]

for i in range(1,11):
    website = 'https://www.cars.com/shopping/results/?list_price_max=&makes[]=mercedes_benz&maximum_distance=20&models[]=&page=' +str(i)+ '&stock_type=new&zip='

    #get request

response = requests.get(website)

#status code

response.status_code

#soup object
soup = BeautifulSoup(response.content,'html.parser')
#print(soup)

#results

results = soup.find_all('div',{'class':'vehicle-card'})
print(len(results))

for result in results:
    Name.append(result.find('h2').get_text())
    
    Price.append(result.find('span',{'class':'primary-price'}).get_text())

    Rating.append(result.find('span',{'class':'sds-rating__count'}))

    Ratingcount.append(result.find('span',{'class':'sds-rating__link'}).get_text())

    Dealername.append(result.find('div',{'class':'dealer-name'}).get_text().strip())

    #ceeate pandas dataframe

cardealer = pd.DataFrame({'Name':Name,'Price':Price,'Rating':Rating,'Ratingcount':Ratingcount,'Dealername':Dealername}) 

print(cardealer)

#output in csv file

cardealer.to_csv('multiplepage.csv',index=False)