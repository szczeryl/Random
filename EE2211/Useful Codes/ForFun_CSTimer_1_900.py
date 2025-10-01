#Read something from CSV and plot graph 

import pandas as pd
import matplotlib.pyplot as plt 
import os #only need this if it's not in the same folder as code file 

df = pd.read_csv(r"C:\Users\Lenovo\Downloads\csTimerExport_20251001_114029.csv", delimiter=';') 
#replace with file name
#delimiter needed for files where everything is joined together. r is only included for os

time = df["P.1"].tolist() #y-axis
number = df["No."].tolist() #x-axis 

plt.plot(number,time)
plt.xlabel("n")
plt.ylabel("time")
plt.title("CSTimer Sesh 1 1 to 900")
plt.show() #needed to show graph. Else, nothing will be printed

