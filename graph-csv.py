import pandas as pd
import plotly.express as px
import csv
import operator
import ntpath
import matplotlib.pyplot as plt
import numpy as np


filename1='/Users/geerd/data/cases/helmond/drive test/4G network test helmond/latencies-2.csv'


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

with open(filename1) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    dates1 = []
    latencies1 = []
    firsttimestamp = 0
    for index, row in enumerate(readCSV):
        if (index == 0):
            firsttimestamp = row[0]
        latency = row[1]
        date = int(row[0] - firsttimestamp)
        dates1.append(date)
        latencies1.append(latency)


# with open(filename2) as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
#     dates2 = []
#     latencies2 = []
#     firsttimestamp = 0
#     sortedlist = sorted(readCSV, key=operator.itemgetter(0), reverse=False)
#     for index, row in enumerate(sortedlist):
#         if (index == 0):
#             firsttimestamp = row[0]
#         latency = row[1]
#         date = int(row[0] - firsttimestamp)

#         dates2.append(date)
#         latencies2.append(latency)

# with open(filename3) as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
#     dates3 = []
#     latencies3 = []
#     firsttimestamp = 0
#     sortedlist = sorted(readCSV, key=operator.itemgetter(0), reverse=False)
#     for index, row in enumerate(sortedlist):
#         if (index == 0):
#             firsttimestamp = row[0]
#         latency = row[1]
#         date = int(row[0] - firsttimestamp)

#         dates3.append(date)
#         latencies3.append(latency)

# numitems = min(len(latencies1), len(latencies2), len(latencies3))

df = pd.DataFrame(
    {
        # "timestamp": dates,
        "latency": latencies1
    }
)

# histdata = {
#         # "timestamp": dates,
#         path_leaf(filename1): latencies1,
#         path_leaf(filename2): latencies2,
#         path_leaf(filename3): latencies3
#     }

# plt.hist(histdata,histtype='step', rwidth='float',  bins=100)


# df.head()
# df.plot(x="timestamp", y="latency")
# df.plot.hist(histtype='step', rwidth='float', density=True, stacked=True, bins=100)
df.plot.hist(histtype='step', rwidth='float', bins=100)
plt.xticks(np.arange(0, 200, 10))
plt.show()
# fig = px.line(df, x = 'timestamp', y = 'latency', title=path_leaf(filename))
# fig.show()
