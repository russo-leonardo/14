lista_spesa=["ciao", "come", "stai"]
def aggiungi():
    x=input()
    lista_spesa.append(x)
def visualizza():
    for i in range(len(lista_spesa)):
        print(f"{i+1},{lista_spesa[i]}")
def rimuovi():
    visualizza()
    indice=int(input())
    lista_spesa.pop(indice=-1)
def conta():
    print(len(lista_spesa))
def svuota():
    lista_spesa.clear()


while True:
    scelta=int(input("efasef"))
    if scelta==1:
        print("aggiungi")
        aggiungi()  
    elif scelta==2:
        visualizza()
    elif scelta==3:
        rimuovi()
    elif scelta==4:
        conta() 
    elif scelta==5:
        svuota()
    elif scelta==0:
        break