#imports
from bs4 import BeautifulSoup
import requests
import pandas as pd



#HTTP request
#store request in variable
website = 'https://www.cars.com/shopping/results/?stock_type=new&makes%5B%5D=mercedes_benz&models%5B%5D=&list_price_max=&maximum_distance=20&zip='

#get request

response = requests.get(website)


#soup object
soup = BeautifulSoup(response.content,'html.parser')
#print(soup)

#results

results = soup.find_all('div',{'class':'vehicle-card'})



#TARGET NECESSARY DATA
#name
print(results[0].find('h2').get_text())
#price
print(results[1].find('span',{'class':'primary-price'}).get_text())
#rating
print(results[2].find('span',{'class':'sds-rating__count'}).get_text())
#ratingcount
print(results[3].find('span',{'class':'sds-rating__link'}).get_text())
#dealername
print(results[4].find('div',{'class':'dealer-name'}).get_text())

#put everything inside for loop
Name =[]
Price=[]
Rating=[]
Ratingcount=[]
Dealername=[]

for result in results:

    
    Name.append(result.find('h2').get_text())
    
    Price.append(result.find('span',{'class':'primary-price'}).get_text())

    Rating.append(result.find('span',{'class':'sds-rating__count'}))

    Ratingcount.append(result.find('span',{'class':'sds-rating__link'}).get_text())

    Dealername.append(result.find('div',{'class':'dealer-name'}).get_text())

 #ceeate pandas dataframe

cardealer = pd.DataFrame({'Name':Name,'Price':Price,'Rating':Rating,'Ratingcount':Ratingcount,'Dealername':Dealername}) 

print(cardealer)


#output in csv file

cardealer.to_csv('singlepage.csv',index=False)






