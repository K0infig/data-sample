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




def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)


std_dev = statistics.stdev(mean_list)
sampleMean = statistics.mean(mean_list)

print("mean: "+ str(sampleMean))
print("standard deviation : "+str(std_dev))

fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
fig.show()

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
# print("std1",first_std_deviation_start, first_std_deviation_end)
# print("std2",second_std_deviation_start, second_std_deviation_end)
# print("std3",third_std_deviation_start,third_std_deviation_end)

## plotting the graph with traces
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("mean of sample3:- ",mean_of_sample3)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


