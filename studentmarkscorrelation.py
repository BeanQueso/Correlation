import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    icecreamSale = []
    coldDrinkSale = []

    with open(data_path) as csv_files:
        reader = csv.DictReader(csv_files)
        for row in reader:
            icecreamSale.append(float(row['Marks In Percentage']))
            coldDrinkSale.append(float(row['Days Present']))

    return{'x':icecreamSale, 'y':coldDrinkSale}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print("correlation between student marks in percentage and days present is ", correlation[0,1])

def setup():
    data_path = 'S-MData.csv'
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

setup()