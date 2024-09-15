import os
from glob import glob
import pandas as pd

Path = "new"
stockext = "*stock.csv"
deliveryext = "*delivery.csv"

all_stock_file = [file
                 for path, subdir, files in os.walk(Path)
                 for file in glob(os.path.join(path, stockext))]

all_delivery_file = [file
                 for path, subdir, files in os.walk(Path)
                 for file in glob(os.path.join(path, deliveryext))]

for file in all_stock_file:
    print("Stock Data")
    data = pd.read_csv(file)

    print(file)
    print(data)

for file in all_delivery_file:
    print("Delivery Data")
    data = pd.read_csv(file)
    
    print(file)
    print(data)