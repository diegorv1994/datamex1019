# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:17:49 2019

@author: diego
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import json 
df=pd.read_csv('Military expenditure.csv')
#print(df.columns)
#print(df.head()) 	
#print(df.isnull().sum().sum())
url = 'https://en.wikipedia.org/wiki/List_of_IMF_ranked_countries_by_GDP'
html=requests.get(url).content
soup = bs(html,"html.parser")
tablas=soup.find_all('table')
tabla0=tablas[-2]
#print(tablas)
#s= soup.find_all('tr')
#se=s.find_all('td')
med_paises=[]
for e in tabla0.find_all('tr'):
    fila=[f for f in e.find_all('td')]
    if len(fila)>0:
        pais={'Country':fila[0].find('a').text.strip(),
              'GDP A':str(fila[1].text),
              'GDP S':str(fila[2].text),
              'GDP D':str(fila[3].text),
              'GDP F':str(fila[4].text),
              'GDP G':str(fila[5].text),
              'GDP H':str(fila[6].text)}
        med_paises.append(pais)
df1=pd.DataFrame(med_paises)
df['PIB nominal'] = df1['GDP A']

URL='https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-religion.json'
res=requests.get(URL)
res

results=res.json()
results[0]

data=pd.DataFrame(results)
data.head()
df['Religion']=data['religion']
df=df.fillna('unknown')
"""Intento fallido
#URL1='https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-life-expectancy.json'
#res1=requests.get(URL1)
#res1

#results1=res1.json()
#results1[0]

#data1=pd.DataFrame(results1)
#data1.head()
#df['Life expectancy']=data['expectancy']

#with open('hdi.txt') as json_file:
#    data = json.load(json_file)
#dat=pd.DataFrame(data)
#dat.head()
#lst=[]               
#for i in range(len(a)):
 #   v = a[i]
  #  v2=v.get("href")
  #  lst.append(v2)
#lst

#ult=tablas[0]
#elm=ult.find_all('a')[0]
#elm
#elm.text
#elm.get('href')
#elm.attrs
#print(elm.attrs['title'])
#'Semi':fila[4].find('a').text.strip(),
   #           'Orbital':int(fila[5].text),
   #           'Discovered':int(fila[6].text)'Mass':
   #fila[3].find('a').text.strip()
   #'Planetary object':fila[2].find('a').text.strip()
#med_paises=[]
#for e in ult.find_all('tr'):
 #   fila=[f for f in e.find_all('td')]
 #   if len(fila)>0:
 #       pais={'Pulsar':fila[1].find('a').text.strip()}
  #      med_paises.append(pais)
#df1=pd.DataFrame(med_paises)
#df['Name of star'] = df1 
#url1="https://raw.githubusercontent.com/pirtleshell/constellations/master/constellations.json"
#res=requests.get(url1)
#res
#results=res.json()
#data=pd.DataFrame(results)
#data.head()
#   df['Name of galaxy'] = data['name']