# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ellip, lfilter, hann, freqs


def demo_data(num_symbols, samples_per_symbol):
    """
    Generate some data for demonstrations.

    `num_symbols` is the number of symbols (i.e. bits) to include
    in the data stream.

    `samples_per_symbol` is the number of samples per symbol.
    (For interesting demonstrations, this number should be at least 20.)

    The total length of the result is `num_symbols` * `samples_per_symbol`.

    Example
    -------
    Import matplotlib and demo_data:

    >>> import matplotlib.pyplot as plt
    >>> from eyediagram.demo_data import demo_data

    Generate and plot some data:

    >>> y = demo_data(16, 25)
    >>> plt.plot(y)

    """
    # A random stream of "symbols" (i.e. bits)
    bits = np.random.randint(0, 2, size=num_symbols)

    # Upsample the bit stream.
    sig = np.repeat(bits, samples_per_symbol)

    # Convert the edges of the symbols to ramps.
    r = min(5, samples_per_symbol // 2)
    sig = np.convolve(sig, [1./r]*r, mode='same')

    # Add some noise and pass the signal through a lowpass filter.
    b, a = ellip(4, 0.087, 30, 0.15)
    y = lfilter(b, a, sig + 0.075*np.random.randn(len(sig)))

    return y

def demo_ASK(num_symbols, samples_per_symbol, ask_order=2, rc=True, bandlimit=True, noise=0.0):
    bits = np.float16(np.random.randint(0, ask_order, size=num_symbols))/(ask_order-1)
    sig = np.repeat(bits, samples_per_symbol)
    if rc:
        # raised-cosine filter also known as Hann window (not to be confused with Hanning window!)
        win = hann(samples_per_symbol)
        sig = np.convolve(sig, win/np.sum(win), mode='same')
    # Add noise
    sig += noise*np.random.randn(len(sig))
    if bandlimit:
        # limit bandwidth to Nyquist bandwidth f_cutoff = f_sample/2
        f_cutoff = 2.0/np.float16(samples_per_symbol)
        print f_cutoff
        # we'll use a 4th order Cauer bandpass filter (realistic!)
        (b, a) = ellip(4, 0.05, 40, f_cutoff, 'low') # , analog=True)
        if False:
            (w, h) = freqs(b, a)
            print min(w), min(abs(h))
            plt.plot(w, 20*np.log10(abs(h)))
            plt.show()
        sig = lfilter(b, a, sig)
    
    return sig

