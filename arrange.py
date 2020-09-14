# TP 
# writes alternating adquired expnos into a list of new continuous expnos

curdat = CURDATA()
n = INPUT_DIALOG("n experiment", "Insert the n of experiments")
n = int(n[0])
start = INPUT_DIALOG("start rw", "Insert starting point") 
st  = int(start[0])

WR([curdat[0], str(st), curdat[2], curdat[3]],"n")
exp = 1
while exp < n:
	RE_IEXPNO(show = "n")
	RE_IEXPNO(show = "n")
	WR([curdat[0], str(st+1), curdat[2], curdat[3]],"n")
	exp += 1 
	st += 1	
RE([curdat[0], str(st), curdat[2], curdat[3]])
