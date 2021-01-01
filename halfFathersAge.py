#!/usr/bin/env/python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Parameters
yearsToTest = 100
fathersAgeWhenBorn = int(input('How old was your father when you were born?'))
whatYearYouWereBorn = int(input('What year were you born?'))

#Construct the dataset
dataset = pd.DataFrame({'year':range(whatYearYouWereBorn,whatYearYouWereBorn+yearsToTest),'son':range(0,0+yearsToTest),'father':range(fathersAgeWhenBorn,fathersAgeWhenBorn+yearsToTest)})



# Extract the columns
year = dataset.iloc[:,0:1].values
son = dataset.iloc[:,1:2].values
father = dataset.iloc[:,2:3].values

answer = ''

#Paint each point and detect an interception
for i in range(0, len(year)):
    if(father[i] == son[i] * 2):
        answer = f'You will be half your fathers age at age: {son[i]} and your father will be: {father[i]} in the year: {year[i]}'
        print(f'You will be half your fathers age at age: {son[i]} and your father will be: {father[i]} in the year: {year[i]}')
        plt.scatter(year[i],father[i],color = 'red')
    else: 
        plt.scatter(year[i],father[i],color = 'blue')
        
#Contstruct the graph
if (len(answer)>1):
    plt.title(answer)
else:
    plt.title('You will probably never be half your fathers age')

plt.show()
