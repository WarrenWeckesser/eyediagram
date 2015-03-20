# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

from __future__ import division as _division, print_function as _print_function

import numpy as _np
import bokeh.plotting as _bp
from .core import grid_count as _grid_count

from ._common import _common_doc


__all__ = ['eyediagram']


def eyediagram(y, window_size, offset=0,
               color=None, cmap=None, alpha=1,
               filename='eyediagram.html'):
    """
    Plot an eye diagram using bokeh.
    <common>

    Either `color` or `cmap` may be given, but not both.

    If given, `color` must be a tuple of three integers, each between 0 and
    255.  This specifies the (R, G, B) values of the color of the traces.
    The colors of overlapping traces are blended towards white.

    `cmap` is expected to be a matplotlib colormap (e.g. matplotlib.cm.hot),
    or a callable that behaves like a matplotlib colormap.

    If neither `color` nor `cmap` are given, the default is
    `color=(192, 168, 0)` (yellowish traces).


    `filename` is the name of the bokeh output file.  The default is
    "eyediagram.html".

    """

    counts = _grid_count(y, window_size, offset)
    max_count = counts.max()

    tcounts = counts.T[::-1, :]

    img = _np.zeros_like(tcounts, dtype=_np.uint32)
    imgv = img.view(dtype=_np.uint8).reshape(img.shape + (4,))

    if cmap is None:
        if color is None:
            color = (192, 168, 0)
        for i in range(3):
            imgv[:, :, i] = (255-color[i]) * (tcounts / max_count)
            imgv[:, :, i] += color[i]
    else:
        for k in range(imgv.shape[0]):
            clr = 255*cmap(tcounts[k, :]/max_count)
            imgv[k, :, :] = clr

    imgv[:, :, 3] = alpha*255*(tcounts > 0)

    ymax = y.max()
    ymin = y.min()
    yamp = ymax - ymin

    _bp.output_file(filename)
    min_x = 0.0
    max_x = 2.0
    min_y = ymin - 0.05*yamp
    max_y = ymax + 0.05*yamp
    p1 = _bp.figure(title="Eye Diagram", plot_width=800, plot_height=500,
                    x_range=[min_x, max_x], y_range=[min_y, max_y],
                    background_fill='black')
    p1.grid.grid_line_color = '#484848'
    p1.grid.grid_line_dash = [5, 2]
    p1.image_rgba(image=[imgv.view(_np.uint32).reshape(img.shape)],
                  x=[min_x], y=[min_y],
                  dw=[max_x - min_x], dh=[max_y - min_y])
    return p1

eyediagram.__doc__ = eyediagram.__doc__.replace("<common>", _common_doc)
