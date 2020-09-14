# copies current dataset path to clipboard

import subprocess 
curdat = CURDATA()
path = (curdat[3] + '/' + curdat[0] + '/'+ curdat[2] + '/' + curdat[1])

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|pbcopy'
    return subprocess.check_call(cmd, shell=True)
 
copy2clip(path)
