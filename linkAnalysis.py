import requests
from bs4 import BeautifulSoup


def link_analysis(link):
    req = requests.get(link)
    page = BeautifulSoup(req.text)
    dict = {}
    #amount=page.select('span.amount')[0].text

    if (page.select('span.amount')[0].text):
        amount = page.select('span.amount')[0].text
        dict['Amount'] = amount
    else:
      #amount=0
        dict['Amount'] = 0
    dict['Link']=link

    defination= page.find_all('dt')
    illaboration= page.find_all('dd')

    #dict['Amount']=amount

    for defi,illa in zip(defination,illaboration):
        dict[defi.string]=illa.string

    standardDic={'Amount':11,'Fuel type:':1,'Model name:':2,'Engine capacity:':3,'Brand:':4,'Model year:':5,'Condition:':6,
                 'Transmission:':7,'Body type:':8,'Mileage:':9,'Registration year:':10, 'Link':12}
    diff =  set(standardDic.keys())- set(dict.keys())

    #----------------------------Extra conditions---------------------------------#
    diffextra = {e: 0 for e in diff}
    dict.update(diffextra)
    return dict
    #print dict

    maindict[link]=dict

link_analysis('http://bikroy.com/en/ad/toyota-fielder-silver-2011-for-sale-dhaka-4')