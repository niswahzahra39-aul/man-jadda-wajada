import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("Data Visualization")

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)

import os
import pandas as pd

file_path = os.path.join(os.path.dirname(__file__), "..", "data", "DataSaham.csv")
df = pd.read_csv(file_path)

st.write(df.head())