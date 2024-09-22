import random, csv
from datetime import datetime, timezone

def listAlphabet():return [chr(i) for i in range(ord("A"), ord("Z") + 1)]
def replace(data):#: is replaced by .
    if isinstance(data, str):
        data = (data.replace(":", "."))
    elif isinstance(data, dict):
        for key, value in data.items():
            data[key] = replace(value)
    elif isinstance(data, list):
        for i in range(len(data)):
            data[i] = replace(data[i])
    return data

def randomcode(length):#number code generating
    tempnumbers = ["0","1","2","3","4","5","6","7","8","9"]
    temp = ""
    for i in range(0,length):
            temp += random.choice(tempnumbers)
    return temp

#File content
filecontent = [
    ["product_id", "quantity"],
    [f"{random.choice(listAlphabet())}{randomcode(3)}", randomcode(3)],
    [f"{random.choice(listAlphabet())}{randomcode(3)}", randomcode(3)],
    [f"{random.choice(listAlphabet())}{randomcode(3)}", randomcode(3)]
]

with open(f'new/{replace(datetime.now(timezone.utc).astimezone().isoformat())}-{random.choice(["CH","DE"])}-stock.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(filecontent)