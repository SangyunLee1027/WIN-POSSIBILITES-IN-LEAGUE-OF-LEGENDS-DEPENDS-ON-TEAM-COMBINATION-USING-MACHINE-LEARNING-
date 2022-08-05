import pandas as pd
import csv

nn = pd.read_csv("./Data/Nicknames.csv")
list = list(nn["Nickname"])
if len(list) != 0:
    print(len(list))