# copies current dataset name to clipboard

import subprocess 
curdat = CURDATA()
name = (curdat[0])

slice=curdat[3]+"/"+curdat[0] + "/"+curdat[1]+"/pdata/1000"

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|pbcopy'
    return subprocess.check_call(cmd, shell=True)
 
copy2clip(name)

RSR("1","1000",show = "n")
RE_PATH(slice,show = "y")
EFP()
APKS()
XCMD(".int")
