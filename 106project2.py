import plotly.express as px
import csv
import numpy as np


def getData(data_path):
    Marks = []
    Days = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks.append(float(row["MarksInPercentage"]))
            Days.append(float(row["DaysPresent"]))
    return{"x":Marks,"y":Days}


def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between marks and days present is ",correlation[0,1])

def setUp():
    data_path = "students marks.csv"
    data_source = getData(data_path)
    findCorrelation(data_source)

setUp()    