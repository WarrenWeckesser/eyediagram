eyediagram
==========

`eyediagram` is a python library for generating eye diagrams (a.k.a. eye patterns).

This is prototype-quality software.  The documentation is thin, and the API may
change.

cython is required to build the package.

To use the package, numpy and scipy must be installed.  Plots are generated with
either matplotlib or bokeh.

Example - matplotlib
--------------------

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


Example - bokeh
---------------

This is `bok_demo.py`.  It uses the `eyediagram` function from the
`eyediagram.bok` module to plot an eye diagram using `bokeh`.

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

![](https://github.com/WarrenWeckesser/eyediagram/blob/master/demo/bok_demo.png)
