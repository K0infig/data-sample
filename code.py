import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

tempMean = statistics.mean(data)
tempStandardDev = statistics.stdev(data)

#fig = ff.create_distplot([data],["temp"], show_hist=False)
#fig.add_trace(go.Scatter(x=[tempMean, tempMean], y=[0,0.1], mode='lines', name="MEAN"))
#fig.show()



print("Mean :"+str(tempMean))
print("Standard Deviation: "+ str(tempStandardDev))


def random_set_of_mean(counter):
    dataset =[]

    for i in range(0,100):
        randomIndex = random.randint(0,len(data))
        value = data[randomIndex]
        dataset.append(value)

    sampleMean = statistics.mean(dataset)
    return sampleMean

def make_graph(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.1], mode='lines', name="MEAN"))
    fig.show()


def setup():
    mean_list =[]

    for i in range(0,1000):
        setOfMeans = random_set_of_mean(100)
        mean_list.append(setOfMeans)


    make_graph(mean_list)

    mean = statistics.mean(mean_list)
    
    print("Mean of 1000 sample data: "+str(mean))
    



setup()


def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()



