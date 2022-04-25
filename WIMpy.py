import pandas as pd
import scipy as sp
from scipy import stats
from scipy.spatial import distance_matrix
import numpy as np
import sys
import random
import matplotlib.pyplot as pls
df = pd.read_csv(r'C:\Users\aweso\OneDrive\Desktop\work\WIM assignment\WIm Technologies Development task.csv')
tower = []
for i in df['Cell ID']:
    tower.append(i+'0')
print(len(tower))
df = df.drop(columns=['Cell ID'])
for column in df:
    df[column] = stats.zscore(df[column])
#df['Easting'] = stats.zscore(df['Easting'])
#df['Northing'] = stats.zscore(df['Northing'])
#df['Long'] = stats.zscore(df['Long'])
#df['Lat'] = stats.zscore(df['Lat'])
ndf = df.to_numpy()

dm = distance_matrix(df,ndf,p=2)
pls.style.use('seaborn')
big = np.array(dm)
big = big.tolist()
#print(big)
nbig = np.sort(big)
def freq():
    array = []
    array1 = []
    for i in tower:
        array.append(int(i[1]))
    for j in range(1,7):
        array1.append(array.count(j))
    return array1
def five(tower):
    array = []
    for i in range (19):
        array.append(chr(big[ord(tower) - 65].index(nbig[ord(tower) - 65][i])+65))
    return array
def furthest(tower):
    return chr(big[ord(tower) - 65].index(nbig[ord(tower) - 65][-1])+65)
def checkfeq(tower1, tower2): #given the cell ID's
    if tower[ord(tower1)-65][1] == tower[ord(tower2)-65][1]:
        return True
    else: 
        return False
def changefeq(towerID, freq):
    #print('beep')
    tower[ord(towerID)-65] = towerID + str(freq)
print(five("R"))
print(furthest('A'))
print(furthest('S'))
print(checkfeq('A','S'))
print(nbig)
#tower[0] = 'A1'
#tower[6] = 'G2'

for i in range(19):
    print(tower[i], tower[ord(five(tower[i][0])[-1])-65], freq())
    bigmax = []
    small = []
    tiny = []
    for k in range(1,7):
        bigmax.append(int(tower[ord(five(tower[i][0])[k])-65][1]))
    for m in range(1,7):
        if not (m in bigmax):
            small.append(m)
            #print(small, "hello")
            #if freq().index(min(freq()))+1 in small:
             #   tiny.append(freq().index(min(freq()))+1)
            tower[i] = tower[i][0] + str(m)
            break  
            
    for j in range(0,19-i):
        if int(tower[ord(five(tower[i][0])[-j-1])-65][1]) == 0:
            changefeq(five(tower[i][0])[-j-1],tower[i][1:])
            break    

del df["Easting"]
del df["Northing"]
#print(df[1])
#df.plot.scatter(x = 'Lat', y = 'Long', c = 'BLue')
colors = []
letters = []
for p in range(19):
    colors.append(int(tower[p][1]))
    letters.append(tower[p][0])
pls.scatter(df['Long'],df['Lat'], c = colors, cmap='Greens', edgecolor = 'black', linewidths= 1, alpha = 0.75)
cbar = pls.colorbar()
cbar.set_label('Frequency')
#ax = pls.subplots()
#ax.scatter(df['Long'],df['Lat'])
pls.xlabel('Longtitude')
pls.ylabel('Latitude')
for q, txt in enumerate(letters):
    pls.annotate(txt, (df['Long'][q],df['Lat'][q]))
pls.show()
for i in range(19):
    tower[i] = tower[i][0] + str(int(tower[i][1])+109)
    #print(n)
print(tower)
        #if max(bigmax) == 6:
         #   pass
        #else:
         #   tower[i] = tower[i][0] + str(max(bigmax)+1)
        #for j in range(0,19-i):
         #   if int(tower[ord(five(tower[i][0])[-j-1])-65][1]) != 0:
          #      changefeq(five(tower[i][0])[-j-1],tower[i][1])
           #     break

#tower[index(big[i][n])][1]
#tower[0] = "A1"
#tower[1] = 'B2'
#if tower[index(big[i][n])][1] == tower[index(big[i][-1])][1]: # or -2 or -3 ... or -5 need to check if the frequeny of the furthest one is different from the five closest to it
'''
def solve():
    for i in range(20):
        print("hi",tower[i])
        if tower[i][1] != 0:
            print("beep")
            for n in range(20):
                print(tower[big[i].index(nbig[i][n])][1], tower[big[i].index(nbig[i][-1])][1],'bepis')
                if tower[big[i].index(nbig[i][n])][1] == tower[big[i].index(nbig[i][-1])][1]: # or -2 or -3 ... or -5 need to check if the frequeny of the furthest one is different from the five closest to it
                    print("continue")
                    continue
                else:
                    print('twoer')
                    tower[i] = tower[i][0]+str(big[i][n])
                solve()
                tower[i][1] = 0
                return
        print(tower, "sanwhieces")
        input("MOre?")    
solve()
print(tower, tower[ord(five(tower[i][0])[-1])-65])
    if int(tower[i][1]) != 0:
        print('beep')
        for j in range(0,19-i):
            if int(tower[ord(five(tower[i][0])[-j-1])-65][1]) == 0:
                changefeq(five(tower[i][0])[-j-1],tower[i][1:])
                break
    else:
'''