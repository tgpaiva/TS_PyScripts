### Zips all expno and procno under the same dataset and saves the file in user desktop
### TP

import shutil
import os 
import sys.argv as argv
from os.path import expanduser


Desktoppath = expanduser('~/Desktop/')
curdat = CURDATA()

if len(argv) == 1:

	os.chdir(curdat[3]+"/"+curdat[0])
	out = Desktoppath + curdat[0]
	shutil.make_archive(out, 'zip', os.getcwd())

else:
	
	os.chdir(curdat[3]+"/"+curdat[0])
	out = argv[1] + curdat[0]
	shutil.make_archive(out, 'zip', os.getcwd())

