import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
student_df = df.loc[df['student_id'] == "TRL_xsl", "TRL_abc", "TRL_xyz", "TRL_zet"]
print(student_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Scatter(
    size=student_df.groupby("level")["attempt"].mean(),
    x=['TRL_xsl', 'TRL_abc', 'TRL_xyz', 'TRL_zet'],
    y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
))
fig.show()
