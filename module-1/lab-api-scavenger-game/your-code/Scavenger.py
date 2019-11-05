#Challenge 1
import numpy as np
import json
import requests
import pandas as pd
from pandas.io.json import json_normalize

URL='https://api.github.com/repos/ironhack-datalabs/datamex1019/forks'

with open('Token.txt', 'r') as f:
    ac=f.readlines()[0]
    acs=ac.split('')
    
u=acs[0]
k=acs[1].rstrip('\n')

res=requests.get(URL, auth=(u, k))

results=res.json()
flattened=json_normalize(results)

l = []
for i in flattened['language']:
    l.append(i)
arrayl = np.array(list(set(l)))
print(arrayl)

#Challenge 2
URL='https://api.github.com/repos/ironhack-datalabs/datamex1019/commits'
with open('Token.txt', 'r') as f:
    ac=f.readlines()[0]
    acs=ac.split('')
    
u=acs[0]
k=acs[1].rstrip('\n')

res=requests.get(URL, auth=(u, k))
results = res.json()

print(len(results[0]['commit'])

#Challenge 3
"""Tomado de Apuntes de Jonathan No pude hacerlo yo"""
url='https://api.github.com/repos/ironhack-datalabs/scavenger/contents/'

tree=res['tree']

archivos=[]
for i in range(len(tree)):
    if tree[i]['type']=='blob' and 'scavengerhunt' in tree[i]['path']:
        #obtengo el path y el contenido del archivo
        get_contenido=requests.get(url + tree[i]['path'])
        contenido=get_contenido.json()
        archivos.append((contenido['name'], contenido['content']))
        time.sleep(1)
print (archivos)

archivos.sort()

import base64
frase=''
for texto in archivos:
    frase+=str(base64.b64decode(texto[1]))

#La frase buscada es:
frase=frase.replace('b\'', '').replace('\\n\'', ' ')

frase





























