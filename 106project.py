import plotly.express as px
import csv
import numpy as np

def getData(data_path):
    Coffee = []
    sleep = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
           Coffee.append(float(row["Coffee"]))
           sleep.append(float(row["sleep"]))
    return{"x":Coffee,"y":sleep}    


def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])

    print("correlation between coffee and sleep is ",correlation[0,1])

def setUp():
    data_path = "sleep hours.csv"
    data_source = getData(data_path)
    findCorrelation(data_source)

setUp()