import pandas as pd
import plotly_express as px

df=pd.read_csv("csv files\Copy+of+data+-+data.csv")
scatterPlot=px.scatter(df,x="date",y="cases",color="country")
scatterPlot.show()