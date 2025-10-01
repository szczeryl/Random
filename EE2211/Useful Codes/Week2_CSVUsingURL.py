#print data from csv file found with a url; else dataset = read_csv(".csv", header = None) will do

import pandas as pd 
from pandas import read_csv

#used the link provided in tutorial 
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
dataset = read_csv(url, header=None) 
dataset.describe() #summary with quartiles --> () included. else, without displays raw data


#count number of zeroes in each column for the dataset 
(dataset[[1,2,3,4,5]] == 0).sum() #columns 1 to 5, essentially indexed as [0:5:1] 
#sum just tells them to add up using counter 



#replace data "x" with "y". Basically Ctrl F and replace all 
import numpy as np 
# mark zero values as missing or nan 
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, np.nan) 
# print the first 20rows of data 
dataset.head(20)



#number of NULL data in each column 
dataset.isnull().sum()
