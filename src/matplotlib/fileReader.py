import pandas as pd

def ReadCsv(fileName):
    csvData = pd.read_csv(fileName)
    return(csvData)