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


