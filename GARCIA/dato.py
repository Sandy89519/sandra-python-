with open ("C:/Users/Aprendiz/Documents/GARCIA/.vs/GARCIA/data.txt",'rt', encoding = 'UTF-8') as dic:
    con=0
    tam=dic.readlines()
    while con<len(tam):
        lista=tam[con].split(',')
        print (lista[0])
        con+=1