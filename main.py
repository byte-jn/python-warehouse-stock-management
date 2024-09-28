import os, shutil, re
from glob import glob
import pandas as pd

# Die Verzeichnisangaben
Path = "new"
updatedPath = "processed"
stockext = "*stock.csv"

# Suchen aller Dateien in dem Verzeichnis
all_stock_file = [file
                 for path, subdir, files in os.walk(Path)
                 for file in glob(os.path.join(path, stockext))]

# Verzeichnis der Datenbank
data = pd.read_csv("databasestock.csv")

# Verarbeitung aller Dateien nacheinander
for file in all_stock_file:
    # Datei wird ausgelesen
    temp = pd.read_csv(file)

    # Dateiname wird ausgelesen
    dateiname = os.path.basename(file)

    # Suche nach dem Länderkürzel
    pattern = r'-([A-Z]{2})-stock\.csv'
    match = re.search(pattern, dateiname)
    if match:
        ctry = match.group(1)
        temp["country"] = ctry  # Länderkürzel schreiben

    for i, row in temp.iterrows():  # Zusammenführung der Dateien
        match = (data['product_id'] == row['product_id']) & (data['country'] == row['country'])  # Vergleicht, was gleich ist
        if match.any():  # Wenn es gleich ist, wird es überschrieben
            data.loc[match, 'quantity'] = row['quantity']
        else:  # Wenn es nicht gleich ist, wird es in eine neue Zeile geschrieben
            data = pd.concat([data, temp.iloc[[i]]], ignore_index=True)

    # Dateien werden nach Bearbeitung in das "processed"-Verzeichnis verschoben
    shutil.move(file, updatedPath)

# Am Ende wird es in databasestock gespeichert
data.to_csv("databasestock.csv", mode="w", index=False)
