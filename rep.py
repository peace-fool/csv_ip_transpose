import pandas as pd

#File Name
file = 'test.csv'
#col = 'Index'

#Importing file in panda dataframe as csv
data = pd.read_csv(file)

#Deleting the column
#data.drop(col, inplace=True, axis=1)

#Importing temperory file 'fin.csv' created by bash (the file contains list of original and transposed IPs)
df = pd.read_csv('fin.csv')

#Making a dictionary out of the 'fin.csv' file
lookup_dict = df.set_index(['FIND'])['REPLACE'].to_dict()

#Looping through te dictionary
for key, value in lookup_dict.items():
    #Replacing the files by finding the match in the dictionary
    data.replace({key: value}, regex=True, inplace=True)

#Saving the dataframe to a new.csv file
data.to_csv('new.csv', index=False)

