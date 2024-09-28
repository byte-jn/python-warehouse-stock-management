import random
import csv
from datetime import datetime, timezone

def listAlphabet(): return [chr(i) for i in range(ord("A"), ord("Z") + 1)]  # Eine Liste erzeugen, in der alle Buchstaben gespeichert werden
def replace(data):  # Doppelpunkte durch Punkte ersetzen, damit es keinen Fehler gibt
    if isinstance(data, str):
        data = (data.replace(":", "."))
    elif isinstance(data, dict):
        for key, value in data.items():
            data[key] = replace(value)
    elif isinstance(data, list):
        for i in range(len(data)):
            data[i] = replace(data[i])
    return data

def randomcode(length):  # Generiert eine zufällige Zahl für die product_id
    tempnumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    temp = ""
    for i in range(0, length):
        temp += random.choice(tempnumbers)
    return temp

for i in range(2):  # Erzeugt die Dateien

    # Erzeugt den Inhalt mithilfe der Funktion randomcode
    filecontent = [
        ["product_id", "quantity"],
        [f"{random.choice(listAlphabet())}{randomcode(3)}", randomcode(3)],
        [f"{random.choice(listAlphabet())}{randomcode(3)}", randomcode(3)],
        [f"{random.choice(listAlphabet())}{randomcode(3)}", randomcode(3)]
    ]

    # Erzeugt den Namen der Datei mit verschiedenen zufälligen Eigenschaften
    file_name = f'new/{datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%dT%H.%M.%S")}+00.00-{random.choice(["CH", "DE", "AT"])}-stock.csv'
    
    # Schreibt alles in die CSV-Datei
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(filecontent)
