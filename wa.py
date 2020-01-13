import re

#_p = re.compile("\[.+\] (.+:)")
_p = re.compile("\[\d?\d\/\d?\d\/\d\d, \d?\d:\d\d:\d\d \wM\] (.+:)")
_array = []

with open('_chat.txt', 'r') as f:

	content = f.readlines()
	
	for _l in content:

		_r = _p.search(_l)
		
		if _r and _r.group(1): 
			_ll = _r.group(1)
			_ll =_ll.replace('\u202a', '')
			_ll =_ll.replace('\xa0', ' ')
			_ll =_ll.replace('\u202c', '')

			if _ll!= 'Class of 1983' not in _ll  : _array.append(_ll[:_ll.find(':')])
			


import collections

THRESHOLD = 50 

_aa = collections.Counter(_array)
_aa = {k: v for k, v in reversed(sorted(_aa.items(), key=lambda item: item[1])) if v> THRESHOLD }
#_aa = {k: v for k, v in _aa.items() if v> 50}
objs = [ k for k,v in _aa.items()]
performs = [ v for k,v in _aa.items()]

print (objs)
#print (performs)

import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.font_manager as mfm
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams.update({'font.size': 10})

fig, ax = plt.subplots()
y_pos = np.arange(len(objs))


plt.barh(y_pos, performs, align='center', alpha=0.5)
ax.set_yticks(y_pos)
ax.set_yticklabels(objs)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('# of Appearance (>50)')
ax.set_title('Group Chat Activity 10/7/18 - 10/1/20 (noon)')

plt.show()