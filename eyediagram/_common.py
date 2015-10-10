# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

_common_doc = """
    `y` is the input data.  This is expected to be a uniform sampling of
    a signal.  A typical case is that the signal is the voltage measurements
    of an analog signal that represents a stream of bits (or "symbols").

    `window_size` is the number of samples to show horizontally.  This is
    typically twice the number of samples per symbol in `y`.

    `offset` is the number of initial samples to skip.  This can be used
    to center the "eye".
"""
