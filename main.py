import os
from glob import glob
import pandas as pd

Path = "new"
stockext = "*stock.csv"

all_stock_file = [file
                 for path, subdir, files in os.walk(Path)
                 for file in glob(os.path.join(path, stockext))]

data = pd.read_csv("databasestock.csv")
data['quantity'] = 0

for file in all_stock_file:
    temp = pd.read_csv(file)
    data = pd.concat([temp,data], ignore_index=True)


data.to_csv("databasestock.csv",mode="w",index=False)
