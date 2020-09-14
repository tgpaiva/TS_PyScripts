# automatic processing of dosy spectra (or other pseudo 2D data)
# default lb value is 0.3, lb can be parced through the command line

import shutil
from sys import argv

lbvalue = argv

XF2()
curdat = CURDATA()
BC_mod=GETPAR("2 BC_mod")
XCMD("ABSF1 1000")
XCMD("ABSF2 -1000")
RSR("1","99")

if len(sys.argv) == 2:
  XCMD("lb {}".format(lbvalue[1])) 
else:
	XCMD("lb 0.3") 

EFP()
APK()
f1=GETPAR("PHC0")
f2=GETPAR("PHC1")
NEWWIN()
RE_PATH(curdat[3]+"/"+curdat[0] + "/"+curdat[1]+"/pdata/"+curdat[2])

if len(sys.argv) == 2:
  XCMD("lb {}".format(lbvalue[1])) 
else:
	XCMD("lb 0.3") 

PUTPAR("PHC0" , f1)
PUTPAR("PHC1" , f2)
XCMD("PH_mod pk")
XF2()
ABS2()
shutil.rmtree(curdat[3]+"/"+curdat[0] + "/"+curdat[1]+"/pdata/"+"99")
CLOSEWIN()