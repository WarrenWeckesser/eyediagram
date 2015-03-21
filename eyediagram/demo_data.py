# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

import numpy as np
from scipy.signal import ellip, lfilter


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
