import shutil
import os

curdat = CURDATA()
EXPPATH = (curdat[3]+"/"+curdat[0] + "/"+curdat[1]+"/pdata")
pdatafolder = os.listdir(EXPPATH)
for file in pdatafolder:
	if file != '1':
		shutil.rmtree(EXPPATH +'/' +file)	
	else:	
		continue
