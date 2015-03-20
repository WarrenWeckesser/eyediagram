eyediagram
==========

`eyediagram` is a python library for generating eye diagrams (a.k.a. eye patterns).

This is prototype-quality software.  The documentation is thin, and the API may
change.

cython is required to build the package.

To use the package, numpy and scipy must be installed.  Plots are generated with
either matplotlib or bokeh.

Example
-------

This is `mpl_demo.py`.  It uses the `eyediagram` function from the
`eyediagram.mpl` module to plot an eye diagram using `matplotlib`.


    from eyediagram.demo_data import demo_data
    from eyediagram.mpl import eyediagram
    import matplotlib.pyplot as plt


    num_symbols = 5000
    samples_per_symbol = 24

    y = demo_data(num_symbols, samples_per_symbol)

    eyediagram(y, 2*samples_per_symbol, offset=16, cmap=plt.cm.coolwarm)

    plt.show()


![](https://github.com/WarrenWeckesser/eyediagram/blob/master/demo/mpl_demo.png)
