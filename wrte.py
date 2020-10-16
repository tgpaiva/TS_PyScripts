# TP
# Writes TE values from a vtlist to a series of successive expno
# User is prompted at start to insert vtlist name

import os 
curdat = CURDATA()

TS_Path = os.path.dirname(os.path.dirname(os.path.dirname(curdat[3])))
fexp =int(curdat[1])

start = INPUT_DIALOG("vtlist", "Insert vtlist")
list = start[0]
vtlistpath = TS_Path + "/exp/stan/nmr/lists/vt/" + list

f = open(vtlistpath, 'r')
vt= f.readlines()
f.close()

for i in range (0,len(vt)):
	RE ([ curdat[0],str (fexp),curdat[1],curdat[3] ],"n")
	PUTPAR ("TE",str(vt[i]))
	fexp += 1