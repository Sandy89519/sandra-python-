import json,csv

with open ("vs/GARCIA/JAVA/prom.sal.json","r", encoding="utf-8") as eljson:
    data=json.load(eljson)

headers=data[0].keys()
#print(headers)
#print(type(data))

with open ("vs/GARCIA/JAVA/sandra.csv", "w") as elcsv:
    writer=csv.DictWriter(elcsv,headers)
    writer.writeheader()  
    writer.writerows(data)