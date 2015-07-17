import matplotlib.pyplot as plt 
import dateutil.parser 
from pandas import *
import re
import os

data = dict()

for file in os.listdir(os.getcwd()):
	if file.endswith('.xls'):
		try:
			pd = pandas.ExcelFile(file)
			df = pd.parse(pd.sheet_names[0])

			df['Name'].replace('', np.nan, inplace=True)
			df.dropna(subset=['Name'], inplace=True)

			# print df.head		

			for index,row in df.iterrows():
				if('232' in row['Name']):
					# print row['Name']

					status = re.findall('Status:\s.\w\w.', row['Action'])[0]
					status = status[9:11]
					# print status

					if row['Name'] not in data.keys():
						data[row['Name']] = dict()
					if status not in data[row['Name']].keys():
						data[row['Name']][status] = 0 

					data[row['Name']][status] += 1


		except: 
			continue

df = DataFrame.from_dict(data=data).transpose()

plt.figure()
plt.clf()

df.plot(kind='bar', stacked=True)
plt.show()








