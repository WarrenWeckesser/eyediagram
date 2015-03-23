# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.
#
# Use pyqtgraph to display the eye diagram computed by eyediagram.grid_count.

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

from eyediagram.demo_data import demo_data
from eyediagram.core import grid_count


def colorize(counts, color1, color2=None):
    """
    Convert the integer array `counts` to an array of RGBA values.
    The colors assigned to the values 1 to counts.max() vary linearly
    from `color1` to `color2`.  If `color2` is not given, (255, 255, 255)
    is used.  The color assigned to the value 0 is (0, 0, 0), with an
    alpha value of 0.
    """
    if color2 is None:
        color2 = (255, 255, 255)
    m = counts.max()
    colors = np.zeros((m+1, 4), dtype=np.uint8)
    r = np.linspace(color1[0], color2[0], m)
    g = np.linspace(color1[1], color2[1], m)
    b = np.linspace(color1[2], color2[2], m)
    colors[1:, 0] = r
    colors[1:, 1] = g
    colors[1:, 2] = b
    colors[1:, 3] = 255
    colors[0, 3] = 0
    img = colors[counts]
    return img


# Generate image data
y = demo_data(5000, 24)
ybounds = (-0.25, 1.25)

# Compute the eye diagram image data.
counts = grid_count(y, 48, offset=16, size=(480, 480), bounds=ybounds)

# Convert counts to an array of RGBA values.
yellow = (224, 192, 48)
img_data = colorize(counts, yellow)

#-------------------------------------------------------------------------
# The rest of this script uses pyqtgraph to create a plot
# of the eye diagram.

pg.mkQApp()

win = pg.GraphicsLayoutWidget()
win.setWindowTitle('Eye Diagram')

# A plot area with axes for displaying the image.
p1 = win.addPlot()

# ImageItem for displaying the eye diagram as an image.
img = pg.ImageItem()
img.setImage(img_data.astype(np.float64))
img.setBorder(10)
p1.addItem(img)

# Set position and scale of image.
dy = ybounds[1] - ybounds[0]
img.scale(2./counts.shape[0], dy/counts.shape[1])
h = counts.shape[1]
p0 = h * ybounds[0]/dy
img.translate(0, p0)

# Show the grid lines in the plot.
ax = p1.getAxis('left')
ax.setGrid(192)
ax = p1.getAxis('bottom')
ax.setGrid(192)

win.resize(640, 480)
win.show()
#-------------------------------------------------------------------------


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
