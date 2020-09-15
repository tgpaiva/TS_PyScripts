# plots 1D spectrum according to a layout file 
# takes default f1p and f2p unless they are specified in the cmd line

from sys import argv

curdat = CURDATA()

name=('/Users/Tiago/Desktop/' + curdat[0] +"_" + curdat[1]+"_" + curdat[2] + ".pdf")

if len(argv) == 3:
    f1p,f2p = argv[1],argv[2]
    PUTPAR("F1P",f1p)
    PUTPAR("F2P",f2p)
    PUTPAR("1 LAYOUT","+/TP_1DSpectrum.xwp")
    XCMD("autoplot -e {}".format(name))
else: 
    f1p,f2p = None,None
    PUTPAR("1 LAYOUT","+/TP_1DSpectrum.xwp")
    XCMD("autoplot -e {}".format(name))