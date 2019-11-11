# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:44:28 2019

@author: diego
"""
import pandas as pd
import requests
#from bs4 import BeautifulSoup as bs
URL='https://api.github.com/events'
resp=requests.get(URL)
resp

data=pd.DataFrame(resp.json())
data.head()

