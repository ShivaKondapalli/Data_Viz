from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import column, widgetbox
from bokeh.plotting import figure
import numpy as np


N = 300

source = ColumnDataSource(data={'x': np.random.random(N), 'y': np.random.random(N)})

plot = figure(title='Example')

plot.circle(x='x', y='y', source=source)

slider = Slider(start=10, end=1000, value=N, step=10, title='Number of Points')


def callback(attr, old, new):
    N = slider.value
    source.data = {'x': np.random.random(N), 'y': np.random.random(N)}


slider.on_change('value', callback)


layout = column(widgetbox(slider), plot)

curdoc().add_root(layout)