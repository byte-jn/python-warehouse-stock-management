import os, shutil, re
from glob import glob
import pandas as pd

# The directory specifications
Path = "new"
updatedPath = "processed"
stockext = "*stock.csv"

# Search for all files in the directory
all_stock_file = [file
                 for path, subdir, files in os.walk(Path)
                 for file in glob(os.path.join(path, stockext))]

# Directory of the database
data = pd.read_csv("databasestock.csv")

# Processing all files one by one
for file in all_stock_file:
    # Read the file
    temp = pd.read_csv(file)

    # Read the filename
    dateiname = os.path.basename(file)

    # Search for the country code
    pattern = r'-([A-Z]{2})-stock\.csv'
    match = re.search(pattern, dateiname)
    if match:
        ctry = match.group(1)
        temp["country"] = ctry  # Write the country code

    for i, row in temp.iterrows():  # Merging the files
        match = (data['product_id'] == row['product_id']) & (data['country'] == row['country'])  # Compare what is equal
        if match.any():  # If they are equal, overwrite it
            data.loc[match, 'quantity'] = row['quantity']
        else:  # If they are not equal, write it into a new row
            data = pd.concat([data, temp.iloc[[i]]], ignore_index=True)

    # After processing, move files to the "processed" directory
    shutil.move(file, updatedPath)

# At the end, save it in databasestock
data.to_csv("databasestock.csv", mode="w", index=False)
