# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.
#
# Use chaco to display the eye diagram computed by eyediagram.grid_count.

import numpy as np

# ETS imports...
from traits.api import HasTraits, Instance
from traitsui.api import Item, Group, View
from enable.api import Component, ComponentEditor
from chaco.api import ArrayPlotData, cool, Plot, PlotGrid
from chaco.tools.api import PanTool, ZoomTool

from eyediagram.demo_data import demo_data
from eyediagram.core import grid_count


def _create_plot_component():

    # Generate some data for the eye diagram.
    num_samples = 5000
    samples_per_symbol = 24
    y = demo_data(num_samples, samples_per_symbol)

    # Compute the eye diagram array.
    ybounds = (-0.25, 1.25)
    grid = grid_count(y, 2*samples_per_symbol, offset=16, size=(480, 480),
                      bounds=ybounds).T

    # Convert the array to floating point, and replace 0 with np.nan.
    # These points will be transparent in the image plot.
    grid = grid.astype(np.float32)
    grid[grid == 0] = np.nan

    #---------------------------------------------------------------------
    # The rest of the function creates the chaco image plot.

    pd = ArrayPlotData()
    pd.set_data("eyediagram", grid)

    plot = Plot(pd)
    img_plot = plot.img_plot("eyediagram",
                             xbounds=(0, 2),
                             ybounds=ybounds,
                             bgcolor=(0, 0, 0),
                             colormap=cool)[0]

    # Tweak some of the plot properties
    plot.title = "Eye Diagram"
    plot.padding = 50

    # Axis grids
    vgrid = PlotGrid(component=plot, mapper=plot.index_mapper,
                     orientation='vertical',
                     line_color='gray', line_style='dot')
    hgrid = PlotGrid(component=plot, mapper=plot.value_mapper,
                     orientation='horizontal',
                     line_color='gray', line_style='dot')
    plot.underlays.append(vgrid)
    plot.underlays.append(hgrid)

    # Add pan and zoom tools.
    plot.tools.append(PanTool(plot))
    zoom = ZoomTool(component=img_plot, tool_mode="box", always_on=False)
    img_plot.overlays.append(zoom)

    return plot


class EyeDiagramDemo(HasTraits):

    plot = Instance(Component)

    traits_view = \
        View(
            Group(
                Item('plot', editor=ComponentEditor(size=(700, 500)),
                     show_label=False),
                orientation="vertical",
            ),
            resizable=True, title="Eye Diagram",
        )

    def _plot_default(self):
        return _create_plot_component()


if __name__ == "__main__":
    demo = EyeDiagramDemo()
    demo.configure_traits()
