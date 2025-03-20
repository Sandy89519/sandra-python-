import csv 
import json

with open("vs/GARCIA/JAVA/customers.csv","r", newline="",encoding="utf-8") as elcsv:
    readercsv=csv.DictReader(elcsv)
    #print(tyoe(readercsv))
    datacsv=[fila for fila  in readercsv]
#print(readercsv)
#print(datacsv)

with open("vs/GARCIA/JAVA/pati.json",'w',encoding="utf-8") as eljson:
    json.dump(datacsv,eljson, indent=4)