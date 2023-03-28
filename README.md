# Observed EB Power Spectrum of the High Frequency Instrument of Planck

This Github repo gives the beam-deconvolved, stacked, observed EB power spectrum of the High Frequency Instrument of Planck as described in [Eskilt et al. (2023)](https://arxiv.org/abs/2303.15369). The power spectrum was generated using the public data release 4 (NPIPE) of Planck using a mask of sky fraction 92% with PolSpice. See the paper for more information on how the EB power spectrum was created.

The power spectrum is stored in `HFI_f_sky_092_EB_o.npy` in the Numpy file format. To load it in Python:
```
import numpy as np
EB_power_spectrum = np.load('HFI_f_sky_092_EB_o.npy')
mean_values = EB_power_spectrum[:, 0]
std_values = EB_power_spectrum[:, 1]
```
where `mean_values` gives you the mean values and `std_values` gives you the error bars. See the script `plot_eb.py` on how to plot it.

## Citation

Feel free to use the EB power spectrum as you see fit, but if you use it for published results, please cite
* J. R. Eskilt et al. (2023), arXiv:2303.15369 [astro-ph.CO]
* Planck Collaboration Int. LVII, Astron. Astrophys. 643, A42 (2020), arXiv:2007.04997 [astro-ph.CO]
