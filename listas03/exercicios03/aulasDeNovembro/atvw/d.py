from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# d= Dash(app)

df= pd.DataFrame({
    "Fruta" : ["Maça", "Laranja"],
    "Amount": [4,2]
})

fig= px.bar(df, x="Fruta", y="Amount")

# app.layout= html.Div(chil)