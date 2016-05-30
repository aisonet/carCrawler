import requests
from bs4 import  BeautifulSoup
from linkAnalysis import link_analysis
from functions import csvwrite
import pandas as pd



r=requests.get('http://bikroy.com/en/ads/ads-in-dhaka-1211?query=toyota')
soup = BeautifulSoup(r.text)
page=soup.find_all(attrs={'class': 'ui-item'})
#print page

alllist=[]

for items in soup.find_all(attrs={'class': 'ui-item'}):
    link='http://www.bikroy.com'+items.find('a')['href']
    getDict=link_analysis(link)

    alllist.append(getDict)

dframe=pd.DataFrame(alllist)

print dframe
writer=pd.ExcelWriter('Cars.xls',engine='xlsxwriter')

dframe.to_excel(writer,'cars')


#csvwrite(alllist)
