import csv

with open ("C:/Users/Aprendiz/Documents/GARCIA/.vs/GARCIA/employees.csv") as principal:
     data=csv.reader(principal)
     salarios=[]
     for x in data:
        print(x[7])
   salarios.append(x)
        

