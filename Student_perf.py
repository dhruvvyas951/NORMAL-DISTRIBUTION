import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("Graph Visualization/StudentsPerformance.csv")
reading = df["reading score"].to_list()
mean = sum(reading)/len(reading)
median = statistics.median(reading)
mode = statistics.mode(reading)
std_deviation = statistics.stdev(reading)


first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean + (2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3*std_deviation), mean + (3*std_deviation)


list_of_data_within_1_std_deviation = [result for result in reading if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in reading if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in reading if result > third_std_deviation_start and result < third_std_deviation_end]


print(mean)
print(median)
print(mode)
print(std_deviation)
print("{} % of data lies within one standard deviation".format(len(list_of_data_within_1_std_deviation)* 100.0/ len(reading)))
print("{} % of data lies within second standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(reading)))
print("{} % of data lies within third standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(reading)))


fig = ff.create_distplot([reading], ["Result"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.17], mode = 'lines', name = 'mean'))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0,0.17], mode = 'lines', name = 'standard deviation one'))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0,0.17], mode = 'lines', name = 'standard deviation one'))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0,0.17], mode = 'lines', name = 'standard deviation two'))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0,0.17], mode = 'lines', name = 'standard deviation two'))
fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0,0.17], mode = 'lines', name = 'standard deviation three'))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0,0.17], mode = 'lines', name = 'standard deviation three'))
fig.show()