# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

from __future__ import division as _division, print_function as _print_function

import numpy as _np
from scipy.interpolate import interp1d as _interp1d
from _brescount import bres_curve_count as _bres_curve_count


__all__ = ['grid_count']


def grid_count(y, window_size, offset=0, size=None, fuzz=True):
    """
    size : tuple of two integers
        Size of the array of counts, (height, width).
        Default is (800, 640).

    Returns a numpy array of integers.
    """
    if size is None:
        size = (800, 640)
    height, width = size
    dt = width / window_size
    counts = _np.zeros((width, height), dtype=_np.int32)
    ymin = y.min()
    yamp = y.ptp()

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
        iyd = (height*(0.9*(yd - ymin)/yamp + 0.05)).astype(_np.int32)
        _bres_curve_count(xx.astype(_np.int32), iyd, counts)

        start = end
    return counts
