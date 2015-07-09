import matplotlib.pyplot as plt 
import dateutil.parser 
from pandas import *
import os

data = []

for file in os.listdir(os.getcwd()):
	if file.endswith('.xls'):
		try:
			# print dateutil.parser.parse(file[:-4])

			pd = pandas.ExcelFile(file)
			df = pd.parse('Sheet2')

			df['Name'].replace('', np.nan, inplace=True)
			df.dropna(subset=['Name'], inplace=True)
			sum = 0.0

			for name in df['Name']:
				if('232' in name):
					alarms = df.loc[df['Name'] == name]['# of Alarms']
					# print '%d' % alarms
					sum += int(alarms)
		
			# data[dateutil.parser.parse(file[:-4])] = sum
			data.append({'date' : dateutil.parser.parse(file[:-4]), 'value' : sum})
		except: 
			continue

# print data

df = DataFrame(data=data)
df['date'] = pandas.to_datetime(df['date'])
df.sort(['date'], inplace=True)

print df.head()

plt.figure()
plt.clf()

df.plot(x='date', y='value')
plt.show()










