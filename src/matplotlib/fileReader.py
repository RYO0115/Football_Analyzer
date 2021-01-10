import pandas as pd

def ReadCsvWithPD(fileName):
    csvData = pd.read_csv(fileName)
    return(csvData)

def ReadCsvWithPDIndex(fileName):
    csvData = ReadCsvWithPD(fileName)
    csvData.index = csvData["index"]
    csvData.pop("index")
    return(csvData)