# This scripts plots the stacked, observed EB power spectrum of the 
# polarized frequency bands of the High Frequency Instrument of Planck.

import numpy as np
import matplotlib.pyplot as plt

c_l_EB_o_mean_std = np.load('HFI_f_sky_092_EB_o.npy')

# c_l_EB_o_mean_std[:, 0] gives the central values for the binned observed stacked EB power spectrum
# c_l_EB_o_mean_std[:, 1] gives the corresponding error bars

# EB is binned starting at ell_min = 51, ell_max = 1490 and delta ell = 20
# For more details see the article.
ell_min = 51
ell_max = 1490
delta_ell = 20
ell = np.arange(ell_min, ell_max+1, delta_ell)
plt.figure()
plt.errorbar(ell, c_l_EB_o_mean_std[:, 0], yerr=c_l_EB_o_mean_std[:, 1], fmt='.', color='black')

plt.axhline(0, linestyle='--', color='black', alpha=0.5)
plt.xlabel(r'$\ell$')
plt.ylabel(r'$C^{EB}_{\ell}$ [$\mu K^2$]')
plt.xlim([0, 1500])
plt.title('Stacked EB power spectrum')
plt.savefig('plot_eb_o_hfi_f_sky_092.pdf')