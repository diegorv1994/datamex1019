# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 08:51:02 2019

@author: diego
"""
#d= sharks.groupby('domain').nunique()
import pandas as pd
import matplotlib.pyplot as plt
from funcionesshark import clean_species,clean_fatal, clean_age, clean_year, clean_year2, clean_date
sharks =pd.read_csv("attacks.csv") 

#print(sharks.columns)
#print(sharks["Sex "])
sharks=sharks.fillna('unknown')
sharks["Type"]=sharks["Type"].str.replace('Boatomg','Boat')
sharks["Type"]=sharks["Type"].str.replace('Boating','Boat')
sharks["Type"]=sharks["Type"].str.replace('Invalid','unknown')
sharks["Type"]=sharks["Type"].str.replace('Questionable','unknown')
#print(sharks["Sex "])
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
n=sharks.isnull().sum()
#x=lambda y: if y=="Unprovoked" or y=="Provoked"
#print(n[n>0])
tipos=sharks["Type"].groupby([sharks.Type.str.strip("'")]).count()
#print(tipos)

#Task=tipos
#sumt=tipos[0]+tipos[1]+tipos[2]+tipos[3]+tipos[4]

#my_labels = 'Boating {}'.format(round(tipos[0]/sumt*100,2)),'Provoked {}'.format(round(tipos[1]/sumt*100,2)),'Sea disaster {}'.format(round(tipos[2]/sumt*100,2)),'Unprovoked {}'.format(round(tipos[3]/sumt*100,2)),'unknown {}'.format(round(tipos[4]/sumt*100,2))
#plt.pie(Task,labels=my_labels,autopct='%1.1f%%')
#plt.title('Type')

#size = [tipos[0]/sumt*100, tipos[1]/sumt*100,tipos[2]/sumt*100, 
 #       tipos[3]/sumt*100,tipos[4]/sumt*100]

#colors = ['yellowgreen', 'gold', 'lightskyblue','lightcoral','blue']
#patches, texts = plt.pie(size, colors=colors, shadow=True, startangle=90)
#plt.legend(patches, my_labels, loc="best")
#plt.axis('equal')
#plt.tight_layout()


#print(sharks.head())
sharks.rename(columns={'Sex ':'Sex'},inplace=True)
sharks.rename(columns={'Species ':'Species'},inplace=True)
sharks["Sex"]=sharks["Sex"].str.replace('lli','unknown')
sharks["Sex"]=sharks["Sex"].str.replace('N','unknown')
sharks["Sex"]=sharks["Sex"].str.replace('.','unknown')
sharks["Sex"]=sharks["Sex"].str.replace('M ','M')
sexos=sharks["Sex"].groupby([sharks.Sex.str.strip("'")]).count()
#print(sexos)
speciesn=sharks["Species"].groupby([sharks.Species.str.strip("'")]).count()
#print(speciesn)
low=lambda x: x.lower()
sharks["Species"]=sharks["Species"].apply(low)
sharks["Species"]=sharks["Species"].str.replace('unconfired','unconfirmed')
sharks["Species"]=sharks["Species"].str.replace('zambezi','zambesi')
#print(sharks["Species"])

sharks["Species"]=sharks["Species"].apply(clean_species)
#print(sharks["Species"])
speciesn=sharks["Species"].groupby([sharks.Species.str.strip("'")]).count()
#print(speciesn)
#wh=sharks["Species"].value_counts()

sharks.rename(columns={'Fatal (Y/N)':'Fatal'},inplace=True)

sharks["Fatal"]=sharks["Fatal"].apply(clean_fatal)
fataln=sharks["Fatal"].groupby([sharks.Fatal.str.strip("'")]).count()
#print(fataln)

# Create a list of colors (from iWantHue)
#Tasks = fataln

#my_labels = 'N','Y','unknown'
#plt.pie(Tasks,labels=my_labels,autopct='%1.1f%%')
#plt.title('If fatal or not')
#plt.axis('equal')
#plt.show()

#Tasks = sexos

#my_labelss = 'F','M','unknown'
#plt.pie(Tasks,labels=my_labelss,autopct='%1.1f%%')
#plt.title('Sex')
#plt.axis('equal')
#plt.show()

#sharks["Year"]=sharks["Year"].apply(clean_year)
#year=sharks.Year.value_counts()
#print(year)
#print(sharks["Year"])
#print(sharks.columns)
sharks["Age"]=sharks["Age"].str.replace('40s','40')
sharks["Age"]=sharks["Age"].str.replace('50s','50')
sharks["Age"]=sharks["Age"].str.replace('20s','20')
sharks["Age"]=sharks["Age"].str.replace('60s','60')
sharks["Age"]=sharks["Age"].str.replace('30s','30')
sharks["Age"]=sharks["Age"].str.replace('18 months','1')
sharks["Age"]=sharks["Age"].str.replace('28 & 26','unknown')
sharks["Age"]=sharks["Age"].str.replace('18 or 20','unknown')
sharks["Age"]=sharks["Age"].str.replace('12 or 13','unknown')
sharks["Age"]=sharks["Age"].str.replace('46 & 34','unknown')
sharks["Age"]=sharks["Age"].str.replace('28, 23 & 30','unknown')
rage=[e for e in range(1,101)]
a=["unknown","Teen","teen","Teens","36 & 26","8 or 10"]

sharks["Age"]=sharks["Age"].apply(clean_age)
Ages=sharks["Age"].groupby([sharks.Age.str.strip("'")]).count()
#print(Ages)

#Task = Ages
#sumAges=Ages[0]+Ages[1]+Ages[2]+Ages[3]+Ages[4]
#my_labels = 'Between 0 and 20 years {}'.format(round(Ages[0]/sumAges*100,2)),'Between 21 and 40 years {}'.format(round(Ages[1]/sumAges*100,2)),'Between 41 and 60 years {}'.format(round(Ages[2]/sumAges*100,2)),'Between 61 and 80 years {}'.format(round(Ages[3]/sumAges*100,2)),'More than 80 years {}'.format(round(Ages[4]/sumAges*100,2))
#plt.pie(Task,labels=my_labels,autopct='%1.1f%%')


#plt.title('Ages')
#sizes = [Ages[0]/sumAges*100, Ages[1]/sumAges*100, Ages[2]/sumAges*100, 
#         Ages[3]/sumAges*100,Ages[4]/sumAges*100]
#colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','blue']
#patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
#plt.legend(patches, my_labels, loc="best")
#plt.axis('equal')
#plt.tight_layout()

#plt.axis('equal')
#plt.show()


sharks["Year"]=sharks["Year"].apply(clean_year)

sharks["Year"]=sharks["Year"].apply(clean_year2)

year=sharks["Year"].groupby([sharks.Year.str.strip("'")]).count()

Task = year
sumyear=year[0]+year[1]+year[2]+year[3]+year[4]+year[5]+year[6]

my_labels = 'Between 1500 and 1600 {}'.format(round(year[0]/sumyear*100,2)),'Between 1600 and 1700 {}'.format(round(year[1]/sumyear*100,2)),'Between 1700 and 1800 {}'.format(round(year[2]/sumyear*100,2)),'Between 1800 and 1900 {}'.format(round(year[3]/sumyear*100,2)),'Between 1900 and 2000 {}'.format(round(year[4]/sumyear*100,2)),'More than 2000 {}'.format(round(year[5]/sumyear*100,2)),'unknown'
plt.pie(Task,labels=my_labels,autopct='%1.1f%%')
plt.title('Year')

size = [year[0]/sumyear*100, year[1]/sumyear*100,year[2]/sumyear*100, 
         year[3]/sumyear*100,year[4]/sumyear*100,year[5]/sumyear*100,
         year[6]/sumyear*100]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','blue','red','yellow']


activity=sharks["Activity"].groupby([sharks.Activity.str.strip("'")]).count()
#print(activity)

country=sharks["Country"].groupby([sharks.Country.str.strip("'")]).count()

#print(country)

#print(sharks["Injury"].groupby([sharks.Injury.str.strip("'")]).count())
sharks["Date"]=sharks["Date"].apply(clean_date)
daten=sharks["Date"].groupby([sharks.Date.str.strip("'")]).count()
#print(daten)
#sdate=daten[0]+daten[1]+daten[2]+daten[3]+daten[4]+daten[5]+daten[6]+daten[7]+daten[8]+daten[9]+daten[10]+daten[11]

#my_labels='Jan{}'.format(round(daten[0]/sdate*100,2)),'Feb {}'.format(round(daten[1]/sdate*100,2)),'Mar {}'.format(round(daten[2]/sdate*100,2)),'Apr {}'.format(round(daten[3]/sdate*100,2)),'May {}'.format(round(daten[4]/sdate*100,2)),'Jun {}'.format(round(daten[5]/sdate*100,2)),'Jul {}'.format(round(daten[6]/sdate*100,2)),'Aug {}'.format(round(daten[7]/sdate*100,2)),'Sep {}'.format(round(daten[8]/sdate*100,2)),'Oct {}'.format(round(daten[9]/sdate*100,2)),'Nov {}'.format(round(daten[10]/sdate*100,2)),'Dec {}'.format(round(daten[11]/sdate*100,2))
#plt.title('Months')

#size = [daten[0]/sdate*100,daten[1]/sdate*100,daten[2]/sdate*100, 
#         daten[3]/sdate*100,daten[4]/sdate*100,daten[5]/sdate*100,
 #        daten[6]/sdate*100,daten[7]/sdate*100,daten[8]/sdate*100, 
 #        daten[9]/sdate*100,daten[10]/sdate*100,daten[11]/sdate*100]

#colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','blue','red','yellow',
#          'black','brown','gray','white','orange']
#patches, texts = plt.pie(size, colors=colors, shadow=True, startangle=90)
#plt.legend(patches, my_labels, loc="best")
#plt.axis('equal')
#plt.tight_layout()



























