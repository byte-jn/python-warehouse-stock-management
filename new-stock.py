import random
import csv
from datetime import datetime, timezone

def listAlphabet(): return [chr(i) for i in range(ord("A"), ord("Z") + 1)]  # Create a list that stores all letters
def replace(data):  # Replace colons with dots to avoid errors
    if isinstance(data, str):
        data = (data.replace(":", "."))
    elif isinstance(data, dict):
        for key, value in data.items():
            data[key] = replace(value)
    elif isinstance(data, list):
        for i in range(len(data)):
            data[i] = replace(data[i])
    return data

def randomcode(length):  # Generates a random number for the product_id
    tempnumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    temp = ""
    for i in range(0, length):
        temp += random.choice(tempnumbers)
    return temp

for i in range(2):  # Generates the files

    # Creates the content using the randomcode function
    filecontent = [
        ["product_id", "quantity"],
        [f"{random.choice(listAlphabet())}{randomcode(3)}", randomcode(3)],
        [f"{random.choice(listAlphabet())}{randomcode(3)}", randomcode(3)],
        [f"{random.choice(listAlphabet())}{randomcode(3)}", randomcode(3)]
    ]

    # Generates the name of the file with various random properties
    file_name = f'new/{datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%dT%H.%M.%S")}+00.00-{random.choice(["CH", "DE", "AT"])}-stock.csv'
    
    # Writes everything to the CSV file
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(filecontent)
