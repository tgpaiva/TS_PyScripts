# TP 
# writes a set of experiments to another dataset

curdat = CURDATA()
n = INPUT_DIALOG("n experiment", "Insert the n of experiments")
n = int(n[0])
newdataset = INPUT_DIALOG("Name of new folder", "Insert the name for new folder")
newdataset = newdataset[0]
st  = int(curdat[2])

WR([newdataset, str(st), curdat[2], curdat[3]],"n")
exp = 1
while exp < n:
	RE_IEXPNO(show = "n")
	WR([newdataset, str(st+1), curdat[2], curdat[3]],"n")
	exp += 1 
	st += 1	
RE([newdataset, str(st), curdat[2], curdat[3]])
