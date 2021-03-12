import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd 
import csv

def random_set_of_means(counter):
    datafile = pd.read_csv("data.csv")
    data =datafile["Math_score"].tolist()
    dataset = []
    for i in range (0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    datafile= mean_list
    fig = ff.create_distplot([datafile], ["mean"], show_hist=False)
    ffig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
    fig.show()


def Standard_deviation ():
    meanlist= []
    meanlist[0] = "mean"
    for i in range (0,1000):
        set_of_means = random_set_of_means(100)
        mean_list.append(set_of_means)
    std_deviation=statistics.stdev(mean_list)
    print( "Standard Deviation of sampling mean :- ", std_deviation)
    show_fig(mean_list)

Standard_deviation()
