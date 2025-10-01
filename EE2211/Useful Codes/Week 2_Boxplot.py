#Boxplot 
#only final command line will be printed. ie if you want plot.show(), comment out stats line/add them in a separate cell 

#Libraries 
import numpy as np
import pandas as pd
import seaborn as sns
import statistics 
import matplotlib.pyplot as plt


#add data in the lists 
dataPointsWOoutliers = [] 
dataPointsWoutliers = []

df_combined = pd.DataFrame()
df_combined['normal'] = dataPointsWOoutliers
df_combined['outliers'] = dataPointsWoutliers


#outliers outside the box for boxplot
ax1 = sns.boxplot(data=df_combined, orient="v", palette="Set2")
ax1 = sns.swarmplot(data=df_combined, orient="v", color=(".25"))
plt.show()

#median for each boxplot
statistics.median(dataPointsWOoutliers), statistics.median(dataPointsWoutliers)

#other stuff like mean work too with this code 
