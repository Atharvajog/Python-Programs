import csv
import json
import re
def reader(filepath):
    a=[]
    with open(filepath,'r',encoding='utf-8-sig', newline='') as csvfile:
        csvobj=csv.DictReader(csvfile)
        for row in csvobj:
            a.append(row)
    return a

def convertjson(a):
    data=json.dumps(a)
    return data

def regular(data):
    pattern = re.compile(r'"name":\s*"anish"')
    matches = pattern.finditer(data)
    for match in matches:
        print(f"Match found at position {match.start()}: {match.group()}")

if __name__=="__main__":
    a=reader("abc.csv")
    print(a)
    b=convertjson(a)
    print(b)
    print(regular(b))
           