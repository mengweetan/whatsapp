import re

#_p = re.compile("\[.+\] (.+:)")
_p = re.compile("\[(\d?\d\/\d?\d\/\d\d), (\d?\d:\d\d:\d\d \wM)\] (.+:)")
_array = []

import pandas as pd 
_data = []

with open('_chat.txt', 'r') as f:

	content = f.readlines()
	
	for _l in content:

		_r = _p.search(_l)
		
		if _r and _r.group(3): 
			_ll = _r.group(3)
			_ll =_ll.replace('\u202a', '')
			_ll =_ll.replace('\xa0', ' ')
			_ll =_ll.replace('\u202c', '')


			if _ll!= 'Class of 1983' : 
				_array.append(_ll[:_ll.find(':')])
				_data.append([_r.group(1),_r.group(2), _ll[:_ll.find(':')]])

df = pd.DataFrame(_data, columns = ['Date', 'Time', 'Person']) 

def weekday(x):
	return x.weekday()
	


df['Date'] =  pd.to_datetime(df['Date'], format='%d/%m/%y')
df['Time'] = pd.to_datetime(df['Time']).dt.strftime('%H:%M:%S')
df['Weekday'] = df.apply(lambda row: weekday(row['Date']), axis=1)
df['Hour'] = df['Time'].str[:2] 

print (df.info())
print (df.head())
print (df.tail())



g = df.groupby('Person')['Date'].count().reset_index(name='Msg').sort_values('Msg',ascending=False)

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np



fig, ax = plt.subplots()
ax.set_ylim([0,4000])
_dt = df.groupby('Weekday').count()['Date'].plot(ax=ax, kind='bar')

fig, ax = plt.subplots()
_dt = df.groupby('Date').count()['Person'].plot(ax=ax)
fig, ax = plt.subplots()
_dt = df.groupby('Hour').count()['Person'].plot.barh(ax=ax)
#print (_dt)
#ax = _dt.plot.hist(by="Time",bins=24)

import collections

THRESHOLD = 50 

_aa = collections.Counter(_array)
_aa = {k: v for k, v in reversed(sorted(_aa.items(), key=lambda item: item[1])) if v> THRESHOLD }
objs = [ k for k,v in _aa.items()]
performs = [ v for k,v in _aa.items()]

#print (objs)
#print (performs)




plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams.update({'font.size': 10})



fig, ax = plt.subplots()
y_pos = np.arange(len(objs))


plt.barh(y_pos, performs, align='center', alpha=0.5)
ax.set_yticks(y_pos)
ax.set_yticklabels(objs)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('# of Appearance (>'+str(THRESHOLD)+')')
ax.set_title('Group Chat Activity 10/7/18 - 10/1/20 (noon)')

plt.show()
