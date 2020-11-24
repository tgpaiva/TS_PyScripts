# copies current dataset name to clipboard

import subprocess 
curdat = CURDATA()
name = (curdat[0])


def copy2clip(txt):
    cmd='echo '+txt.strip()+'|pbcopy'
    return subprocess.check_call(cmd, shell=True)
 
copy2clip(name)

