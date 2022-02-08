import csv
import numpy as np 
def getDataSource(data_path):
    marks_in_percentage = []
    daysPresent=[]
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader :
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"])) 
    return {
        "x":marks_in_percentage,"y":daysPresent
    }
def corelation(datasource):
    c=np.corrcoef(datasource["x"],datasource["y"])
    print("corellation coefficient n=between marks in percentage and days present is ",c[0,1])

def setup():
    data_path="Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    corelation(datasource) 

setup() 