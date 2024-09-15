import os
from glob import glob
import pandas as pd

# Definiere den Pfad und die Dateierweiterung
PATH = "new"
EXT = "*.csv"

# Finde alle CSV-Dateien im angegebenen Verzeichnis
all_csv_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]
print("Gefundene CSV-Dateien:", all_csv_files)

# Durchlaufe jede gefundene CSV-Datei
for file in all_csv_files:
    csv_file_path = file
    # Lese die CSV-Datei in ein DataFrame
    data = pd.read_csv(csv_file_path)
    
    # Zeige die Daten an
    print(f"Inhalt der Datei {csv_file_path}:")
    print(data)
    
    # Durchlaufe jede Zeile im DataFrame und drucke sie
    for index, zeile in data.iterrows():
        print(f"Zeile {index}: {zeile.to_dict()}")
