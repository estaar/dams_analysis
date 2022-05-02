# Import the needed packages

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from scipy import signal


# Read All the Datafiles to pandas Dataframes.
df_kap_arr = pd.read_csv(r'River Profile.csv')

# Reindex the river profile to start draw upstream instead of downstream
df_kap_arr = df_kap_arr.reindex(index=df_kap_arr.index[::-1])

df_kds = pd.read_csv('Dam Site Cross-section.csv')
df_ksw = pd.read_csv('Weir Cross-section.csv')

# Add the Graphs and Sub Plots
fig = make_subplots(rows=3, cols=1, subplot_titles=('River Profile', 'Dam Site Cross-section', 'Weir Site Crosssection'), row_heights=[0.7, 0.15, 0.15])
x=df_kap_arr.Distance
y=signal.savgol_filter(df_kap_arr.Z,13, 3)
custom_data = np.stack((df_kap_arr.POINT_Y, df_kap_arr.POINT_X, df_kap_arr.Long, df_kap_arr.Lat, ), axis=-1)
fig.add_trace(go.Scatter(
    x=[4381,],
    y=[1800,],
    mode="markers+text",
    name="Markers and Text",
    marker=dict(size=12),
    text=["Kaps Dam Wall",],
    textposition="bottom right"
))

fig.add_trace(go.Scatter(
    x=[3081,],
    y=[1774,],
    mode="markers+text",
    name="Tarmac Road",
    marker=dict(size=12),
    text=["Tarmac Road",],
    textposition="bottom right"
))

fig.add_trace(go.Scatter(
    x=[2038,],
    y=[1757,],
    mode="markers+text",
    name="Tarmac Road",
    marker=dict(size=12),
    text=["Arr Dam Wall",],
    textposition="top left"
))

hov = 'Distance: %{x}m'+'<br>Elevation: %{y}m ' + '<br>Easting(X): %{customdata[0]}'+ '<br>Northing(Y): %{customdata[1]}'+ '<br>Longitude: %{customdata[2]}'+ '<br>Latitude: %{customdata[3]}'
fig.add_trace(
    go.Scatter(x=x, y=y, customdata=custom_data, hovertemplate=hov, mode='lines', name='River Profile', line=dict(color='#0000FF')), row=1, col=1)
fig.add_annotation(text="Proposed Weir Site", x=2420, y=1759, arrowhead=1, showarrow=True, row=1, col=1)
fig.add_vrect(x0=2430, x1=2434, fillcolor="Red", opacity=0.5, layer='below', line_width=0, row=1, col=1)
fig.add_annotation(text="Proposed Dam Site", x=4276, y=1794, arrowhead=1, showarrow=True, row=1, col=1, yshift=25)
fig.add_vrect(x0=4271, x1=4275, fillcolor="Red", opacity=0.5, layer='below', line_width=0, row=1, col=1)
fig.update_xaxes(title_text='Distance from Main River (M)', row=1, col=1)
fig.update_yaxes(title_text='Elevation(M)', row=1, col=1)

fig.add_trace(go.Scatter(x=df_kds.Distance, y=signal.savgol_filter(df_kds.Elevation,53, 3), mode='lines', name='Dam Site Cross-section'), row=2, col=1)
fig.update_xaxes(title_text='Distance Across River Valley (M)', row=2, col=1)
fig.update_yaxes(title_text='Elevation(M)', row=2, col=1)

fig.add_trace(go.Scatter(x=df_ksw.Distance, y=signal.savgol_filter(df_ksw.Elevation,53,3), mode='lines', name='Weir Cross-section',), row=3, col=1)
fig.update_xaxes(title_text='Distance Across River Valley (M)', row=3, col=1)
fig.update_yaxes(title_text='Elevation(M)', row=3, col=1)


# Update and Save the figure
fig.update_layout(height=2000)
fig.update_layout(showlegend=False)
fig.write_html('index.html')



