from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, CategoricalColorMapper, Slider, HoverTool, Select
from bokeh.palettes import Spectral6
from bokeh.layouts import row, widgetbox
from bokeh.plotting import figure
import pandas as pd

file_path = "data/gapminder.csv"

df = pd.read_csv(file_path).drop('Unnamed: 0', axis=1)
df = df.set_index('Year')

regions_list = df.region.unique().tolist()
source = ColumnDataSource(data={"x": df.loc[1970, 'fertility'],
                                "y": df.loc[1970, 'life'],
                                'Country': df.loc[1970, "Country"],
                                'pop': df.loc[1970, 'population'],
                                'region': df.loc[1970, 'region']
                                })
color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)

xmin, xmax = min(df.fertility), max(df.fertility)
ymin, ymax = min(df.life), max(df.life)


plot = figure(title='Gapminder data for 1970', x_axis_label='Fertility(Children Per Woman)', y_axis_label='Life Expectancy(years)',
              x_range=(xmin, xmax), y_range=(ymin, ymax))

plot.circle(x='x', y='y', source=source, color=dict(field='region', transform=color_mapper), legend='region')
plot.legend.location = 'top_right'

hover = HoverTool(tooltips=[('Country', '@Country')])

plot.add_tools(hover)


def update_plot(attr, old, new):
    yr = slider.value
    x = x_select.value
    y = y_select.value

    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y

    new_data = {"x": df.loc[yr, x],
                                "y": df.loc[yr, y],
                                'Country': df.loc[yr, "Country"],
                                'pop': df.loc[yr, 'population'],
                                'region': df.loc[yr, 'region']}

    source.data = new_data

    plot.x_range.start = min(df[x])
    plot.x_range.end = max(df[x])
    plot.y_range.start = min(df[y])
    plot.y_range.end = max(df[y])

    plot.title.text = f'Gap minder data for {slider.value}'


x_select = Select(options=['fertility', 'life', 'child_mortality', 'gdp'], value='fertility',
                title='X-axis-data')

x_select.on_change('value', update_plot)

y_select = Select(options=['fertility', 'life', 'child_mortality', 'gdp'], value='life',
                title='Y-axis-data')

y_select.on_change('value', update_plot)

slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

slider.on_change('value', update_plot)

layout = row(widgetbox(slider, x_select,y_select), plot)

curdoc().add_root(layout)
curdoc().title = 'Gapminder'

