import pandas as pd
import csv

data = pd.read_csv("Project130/FinalData.csv")


del data["Star_name"]

data = data.dropna()

data.to_csv("Project130/data.csv")