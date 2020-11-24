# Takes first and second slice of a two step diffusion experiment
# shows the multiple display of the 5 % and maximum gradient spectra 
import sys.argv as argv

curdat = CURDATA()
XF2()
EXPPATH =curdat[3]+"/"+curdat[0] + "/"+curdat[1]+"/pdata/"+curdat[2]
firstslice =curdat[3]+"/"+curdat[0] + "/"+curdat[1]+"/pdata/1000"
secondslice =curdat[3]+"/"+curdat[0] + "/"+curdat[1]+"/pdata/1001"

if len(argv) <= 1:
	RSR("1","1000",show = "n")
	RE_PATH(firstslice, show = "n")
	EFP()
	APKS()
	RE_PATH(EXPPATH, show = "n")
	RSR("2","1001",show = "n")
	RE_PATH(secondslice, show = "y")
	EFP()
	APKS()
	XCMD(".md no load")
	RE_PATH(firstslice)
elif len(argv) == 2:
	RSR("1","1000",show = "n")
	RE_PATH(firstslice, show = "n")
	EFP()
	APKS()
	RE_PATH(EXPPATH, show = "n")
	RSR(str(argv[1]),"1001",show = "n")
	RE_PATH(secondslice, show = "y")
	EFP()
	APKS()
	XCMD(".md no load")
	RE_PATH(firstslice)