import matplotlib
import matplotlib.pyplot as plt
import numpy as np

TTLCDM = np.loadtxt("output/LCDM_cl_lensed.dat") # l, C_l
TT0505 = np.loadtxt("output/MG0505_cl_lensed.dat") # l, C_l
TT11= np.loadtxt("output/MG11_cl_lensed.dat") # l, C_l
TTm1m1 = np.loadtxt("output/MGm1m1_cl_lensed.dat") # l, C_l
TT01 = np.loadtxt("output/MG01_cl_lensed.dat")

fig = plt.figure(figsize=(5, 5*6/8.))
# this should be changed for making a panel of multiple figures
ax = fig.add_subplot(111)
ax.set_xscale('log')
#ax.set_yscale('log')


plt.plot(TTLCDM[:,0],TTLCDM[:,0]*(TTLCDM[:,0]+1)/6.28*TTLCDM[:,5], color='black',ls='-', label=r'$\Lambda$CDM')
plt.plot(TT0505[:,0],TTLCDM[:,0]*(TTLCDM[:,0]+1)/6.28*TT0505[:,5], color='darkcyan',ls=':',label=r'$E_{11}=0.5\ E_{22}=0.5$')
plt.plot(TT11[:,0],TTLCDM[:,0]*(TTLCDM[:,0]+1)/6.28*TT11[:,5], color='blue',ls='-',label=r'$E_{11}=1\ E_{22}=1$')
plt.plot(TTm1m1[:,0],TTLCDM[:,0]*(TTLCDM[:,0]+1)/6.28*TTm1m1[:,5], color='cyan',ls='-.',label=r'$E_{11}=-1\ E_{22}=-1$')
plt.plot(TT01[:,0],TTLCDM[:,0]*(TTLCDM[:,0]+1)/6.28*TT01[:,5], color='navy',ls='--',label=r'$E_{11}=0\ E_{22}=1$')
#plt.plot(ell,lclBB2, color='navy', label='BB')
plt.xlabel(r"$\ell$"); plt.ylabel(r"$\ell(\ell+1)C_\ell^{\phi\phi}/2\pi$")
plt.legend(frameon=False,loc='upper right',ncol=1,fontsize='small')

#plt.show()
plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
plt.savefig('outplots/lens_MG.pdf', bbox_inches='tight', pad_inches=0.02)
