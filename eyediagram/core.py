# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

from __future__ import division as _division, print_function as _print_function

import numpy as _np
from scipy.interpolate import interp1d as _interp1d
from ._brescount import bres_curve_count as _bres_curve_count


__all__ = ['grid_count']


def grid_count(y, window_size, offset=0, size=None, fuzz=True, bounds=None):
    """
    Parameters
    ----------
    `y` is the 1-d array of signal samples.

    `window_size` is the number of samples to show horizontally in the
    eye diagram.  Typically this is twice the number of samples in a
    "symbol" (i.e. in a data bit).

    `offset` is the number of initial samples to skip before computing
    the eye diagram.  This allows the overall phase of the diagram to
    be adjusted.

    `size` must be a tuple of two integers.  It sets the size of the
    array of counts, (height, width).  The default is (800, 640).

    `fuzz`: If True, the values in `y` are reinterpolated with a
    random "fuzz factor" before plotting in the eye diagram.  This
    reduces an aliasing-like effect that arises with the use of
    Bresenham's algorithm.

    `bounds` must be a tuple of two floating point values, (ymin, ymax).
    These set the y range of the returned array.  If not given, the
    bounds are `(y.min() - 0.05*A, y.max() + 0.05*A)`, where `A` is
    `y.max() - y.min()`.

    Return Value
    ------------
    Returns a numpy array of integers.

    """
    if size is None:
        size = (800, 640)
    height, width = size
    dt = width / window_size
    counts = _np.zeros((width, height), dtype=_np.int32)

    if bounds is None:
        ymin = y.min()
        ymax = y.max()
        yamp = ymax - ymin
        ymin = ymin - 0.05*yamp
        ymax = ymax + 0.05*yamp
    else:
        ymin, ymax = bounds

    start = offset
    while start + window_size < len(y):
        end = start + window_size
        yy = y[start:end+1]
        k = _np.arange(len(yy))
        xx = dt*k
        if fuzz:
            f = _interp1d(xx, yy, kind='cubic')
            jiggle = dt*(_np.random.beta(a=3, b=3, size=len(xx)-2) - 0.5)
            xx[1:-1] += jiggle
            yd = f(xx)
        else:
            yd = yy
        iyd = (height * (yd - ymin)/(ymax - ymin)).astype(_np.int32)
        _bres_curve_count(xx.astype(_np.int32), iyd, counts)

        start = end
    return counts
