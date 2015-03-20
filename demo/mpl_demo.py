# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

from eyediagram.demo_data import demo_data
from eyediagram.mpl import eyediagram
import matplotlib.pyplot as plt


# Get some data for the demonstration.
num_symbols = 5000
samples_per_symbol = 24
y = demo_data(num_symbols, samples_per_symbol)

eyediagram(y, 2*samples_per_symbol, offset=16, cmap=plt.cm.coolwarm)

plt.show()
