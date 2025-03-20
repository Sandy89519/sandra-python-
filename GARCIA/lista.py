lista = [100, "soacha", "A", 2.5, "CIDE"]
print(type(lista))
print(len(lista ))

for i in range (11):
    lista.append(i*10)

print(lista) 

def llenarlista (lista,cantidad):
    lista= []
    num=0
    for i in range(cantidad):
        num=int(input("ingrese numero"))
        lista.append(num)
    return lista

vector =[]
vector = llenarlista(vector,5)
print(vector)




