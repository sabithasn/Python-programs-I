import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd 
import csv

datafile = pd.read_csv("studentMarks.csv")
data =datafile["Math_score"].tolist()

fig = ff.create_distplot([data], ["average"], show_hist=False)
fig.show()

population_mean = statistics.mean(data)
std_deviation=statistics.stdev(data)
print( "Mean of population  :- ", mean)
print( "Standard Deviation  of population  :- ", std_deviation)
   
