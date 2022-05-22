# -- coding: utf-8 --

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(my_style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'djando', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'httpie'},
    {'value': 15028, 'label': 'djando'},
    {'value': 14798, 'label': 'flask'}
]

chart.add('', plot_dicts)
chart.render_to_file('bar_description.svg')
