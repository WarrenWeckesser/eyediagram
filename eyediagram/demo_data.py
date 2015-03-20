# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

import numpy as np
from scipy.signal import ellip, max_len_seq, lfilter


def demo_data(num_symbols, samples_per_symbol):
    b, a = ellip(4, 0.087, 30, 0.15)
    nbits = 15
    initial_state = np.random.randint(0, 2, size=nbits)
    bits, state = max_len_seq(nbits, length=num_symbols, state=initial_state)
    sig = np.repeat(bits, samples_per_symbol)
    r = min(5, samples_per_symbol // 2)
    sig = np.convolve(sig, [1./r]*r, mode='same')
    y = lfilter(b, a, sig + 0.075*np.random.randn(len(sig)))
    return y
