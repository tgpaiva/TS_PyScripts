# Multiplies all gp in gpnam list by 3 %
# DiffBB z gradient (1768 Gcm) conversion to regular HR probes 50 (Gcm) for HR pp sequences

gradient = [] #  variable creation

grad_HR = GETPAR("GPZ") # read gpnam array as a string
grad_HR = [float(x) for x in grad_HR.split()] # convert string to a list of floats

grad_diffbb = [grad_HR[x] * 0.03 for x in range (len(grad_HR))] # transform HR gradients  to diff gradients 53 / 1700 ~ 0.03 

for z in range (len(grad_diffbb)): # write gpz values to gpnam array
		gradient = "GPZ " + str(z)
		PUTPAR(gradient, str(grad_diffbb[z]))