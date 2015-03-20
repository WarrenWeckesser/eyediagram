# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

from __future__ import division as _division, print_function as _print_function

import numpy as _np
from .core import grid_count as _grid_count
import matplotlib.pyplot as _plt


from ._common import _common_doc


__all__ = ['eyediagram', 'eyediagram_lines']


def eyediagram_lines(y, window_size, offset=0, **plotkwargs):
    """
    Plot an eye diagram using matplotlib by repeatedly calling the `plot`
    function.
    <common>

    """
    start = offset
    while start < len(y):
        end = start + window_size
        if end > len(y):
            end = len(y)
        yy = y[start:end+1]
        _plt.plot(_np.arange(len(yy)), yy, 'k', **plotkwargs)
        start = end

eyediagram_lines.__doc__ = eyediagram_lines.__doc__.replace("<common>",
                                                            _common_doc)


def eyediagram(y, window_size, offset=0, colorbar=True, **imshowkwargs):
    """
    Plot an eye diagram using matplotlib by creating an image and calling
    the `imshow` function.
    <common>
    """
    counts = _grid_count(y, window_size, offset)
    counts = counts.astype(_np.float32)
    counts[counts == 0] = _np.nan
    ymax = y.max()
    ymin = y.min()
    yamp = ymax - ymin
    min_y = ymin - 0.05*yamp
    max_y = ymax + 0.05*yamp
    _plt.imshow(counts.T[::-1, :],
                extent=[0, 2, min_y, max_y],
                **imshowkwargs)
    ax = _plt.gca()
    ax.set_axis_bgcolor('k')
    _plt.grid(color='w')
    if colorbar:
        _plt.colorbar()

eyediagram.__doc__ = eyediagram.__doc__.replace("<common>", _common_doc)
