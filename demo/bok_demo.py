# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

from eyediagram.demo_data import demo_data
from eyediagram.bok import eyediagram
from matplotlib.cm import coolwarm
from bokeh.plotting import show


# Get some data for the demonstration.
num_symbols = 5000
samples_per_symbol = 24
y = demo_data(num_symbols, samples_per_symbol)

p1 = eyediagram(y, 2*samples_per_symbol, offset=16, cmap=coolwarm,
                filename='bok_demo.html')

# If you don't want the dependency on matplotlib, replace `cmap=coolwarm`
# with, say, `color=(160, 145, 50)`.

show(p1)
