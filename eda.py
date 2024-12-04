from stats_2 import *
import streamlit as st
import seaborn as sb
import matplotlib.pyplot as mp
import matplotlib
import numpy as np


df = player_stats()
data = df[["W", "NBA_FANTASY_PTS", "REB", "TOV", "STL", "PTS", "FG_PCT", "PTS_RANK"]]
matplotlib.use("TkAgg", force=True)
sb.heatmap(data.select_dtypes(include=np.number).corr(), annot=True)
mp.show()
