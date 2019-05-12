import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import style

excel_file = open('C:/Users/esteban/Documents/projects/AquacultureTradeFull.xls','rb')

#There will be a performance benefit for reading multiple sheets as
#the file is read into memory only once. (when you have to parse multimple sheets)


#creating list that will rename the columns in the df
#this following step creates a new list but it needs to be "better"
col_names = list(range(1989,2019))

#setting the key for this data frame: country-code and country-name
df = pd.read_excel(excel_file, sheetname ="Salmon_Q_Yearly-Full", index_col=[2])

#dropping the last 2 columns from df pertaining to the 2 dates with "weird" numbers and the country code
df = df.drop(['Unnamed: 33','Unnamed: 34', 'U.S. Atlantic salmon imports, volume by selected sources (1,000 pounds)'], axis=1)

#removing rows with an index "NaN"
#df = df.dropna(how='any',axis=0)
df = df.drop(['Unnamed: 1'],axis=1)

#assigning column names to cleaned data frame
df.columns = col_names
#df.index.name = ['country']

#
#Graphing data
#chiledata = df.iloc[1]

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

'''def animate(i):
	graph_data = df.iloc[1].at[]
	xs = []
	ys = []'''
