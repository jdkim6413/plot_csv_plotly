import numpy as np
import os
import pandas as pd
import plotly.express as px
from datetime import datetime


csv_file_name = "BR7_BandA_delete.csv"
cut_off = True


def parser(x):
    print(datetime.strptime(x, "%Y-%m-%d %H:%M"))
    return datetime.strptime(x, "%Y-%m-%d %H:%M")


# skiprows=range(1, 305281)
plot_df = pd.read_csv(csv_file_name, header=0, parse_dates=['Time'], index_col='Time', date_parser=parser)

if cut_off:
    plot_df = plot_df.head(10000)

# plot_df = plot_df.replace('Bad', 0)

fig1 = px.line(plot_df.astype(float), x=plot_df.index, y=plot_df.columns[:], line_shape='linear')

fig1.update_xaxes(title_text='Time')
fig1.update_traces(hovertemplate=None)
fig1.update_layout({'legend_title_text': ''}, hovermode="x unified")
fig1.show()

fig1.write_html(csv_file_name + '.html')