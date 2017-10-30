import matplotlib
import matplotlib.pyplot as plt
import numpy as np

LCDM = np.loadtxt("output/LCDM_cl_lensed.dat") # l, C_l
BBmu = np.loadtxt("output/BB_mu_cl_lensed.dat") # l, C_l
BBeta = np.loadtxt("output/BB_eta_cl_lensed.dat") # l, C_l

fig = plt.figure(figsize=(5, 5*6/8.))
# this should be changed for making a panel of multiple figures
ax = fig.add_subplot(111)
ax.set_xscale('log')
#ax.set_yscale('log')
plt.add_y_marker(0)


plt.plot(LCDM[:,0],(BBeta[:,8]-LCDM[:,8])/LCDM[:,8], color='black',ls='-', label=r'$z=0.1$')
plt.plot(LCDM[:,0],(BBeta[:,9]-LCDM[:,9])/LCDM[:,9], color='darkred',ls='-', label=r'$z=1$')
plt.plot(LCDM[:,0],(BBeta[:,10]-LCDM[:,10])/LCDM[:,10], color='navy',ls='-', label=r'$z=2$')
plt.plot(LCDM[:,0],(BBeta[:,11]-LCDM[:,11])/LCDM[:,11], color='green',ls='-', label=r'$z=3$')

plt.legend(frameon=False,loc='upper right',ncol=1,fontsize='small')
plt.title(r'BB parametrization $\mu_0=0\ \eta_0=0.1$')
plt.xlabel(r"$\ell$"); plt.ylabel(r"$\Delta C_\ell/C_\ell^{\rm GR}$")


#plt.show()
plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
plt.savefig('outplots/BBeta_MG.pdf', bbox_inches='tight', pad_inches=0.02)
