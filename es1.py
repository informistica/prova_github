tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)
# (squadra di casa, squadra ospite, punteggio della squadra di casa, punteggio della squadra ospite)

def mediaGolPartite(tupla_partite): 
    sommaOspite=0
    sommaCasa=0
    cont=0

    for (squadraCasa, squadraOspite, punteggioCasa, punteggioOspite) in tupla_partite: 
       sommaOspite+=punteggioOspite
       sommaCasa+=punteggioCasa
       cont+=2
    return((sommaOspite+sommaCasa)/cont)

def mediaGolSquadra(tupla_partite, squadra):
    sommaOspite=0
    sommaCasa=0
    cont=0
    for (squadraCasa, squadraOspite, punteggioCasa, punteggioOspite) in tupla_partite: 
        if(squadra==squadraCasa or squadra==squadraOspite): 
            sommaOspite+=punteggioOspite
            sommaCasa+=punteggioCasa
            cont+=2
    return((sommaOspite+sommaCasa)/cont)

def partitaConPiuGol(tupla_partite): 
    
    max=0
    punteggioCasaMax=0
    punteggioOspiteMax=0
    squadraCasaMax=0
    squadraOspiteMax=0
    
    for (squadraCasa, squadraOspite, punteggioCasa, punteggioOspite) in tupla_partite: 
        if(punteggioCasa+punteggioOspite>max):
            max= punteggioOspite+punteggioCasa
            punteggioCasaMax=punteggioCasa
            punteggioOspiteMax=punteggioOspite
    for (squadraCasa, squadraOspite, punteggioCasa, punteggioOspite) in tupla_partite: 
        if(max==punteggioOspite+punteggioCasa):
            squadraCasaMax=squadraCasa
            squadraOspiteMax=squadraOspite
    return(squadraCasaMax, squadraOspiteMax, punteggioCasaMax, punteggioOspiteMax)
        
def partitaConMenoGol(tupla_partite): 

    min=10000
    punteggioCasaMin=0
    punteggioOspiteMin=0
    squadraCasaMin=0
    squadraOspiteMin=0

    for (squadraCasa, squadraOspite, punteggioCasa, punteggioOspite) in tupla_partite: 
        if(punteggioCasa+punteggioOspite<min):
            min= punteggioOspite+punteggioCasa
            punteggioCasaMin=punteggioCasa
            punteggioOspiteMin=punteggioOspite

    for (squadraCasa, squadraOspite, punteggioCasa, punteggioOspite) in tupla_partite: 
        if(min==punteggioOspite+punteggioCasa):
            squadraCasaMin=squadraCasa
            squadraOspiteMin=squadraOspite
    return(squadraCasaMin, squadraOspiteMin, punteggioCasaMin, punteggioOspiteMin)

def percentualeVittoreSquadra(tupla_partite, squadra): 
    partiteVinte=0
    partiteTotali=5
    for (squadraCasa, squadraOspite, punteggioCasa, punteggioOspite) in tupla_partite: 
        if(squadra==squadraCasa): 
            if(punteggioCasa>punteggioOspite):
                partiteVinte+=1
        elif(squadra==squadraOspite): 
            if(punteggioOspite>punteggioCasa):
                partiteVinte+=1

    return((partiteVinte/partiteTotali)*100)
                

while(True): 
    print("\n 1-Media gol partite; ")
    print("2- Media gol squadra; ")
    print("3- Partita con più gol;")
    print("4- Partita con meno gol; ")
    print("5- Percentuale vittorie squadre;")
    print("6- Per uscire dal programma.")
    scelta=int(input("Fai la tua scelta: "))
    if(scelta<1 or scelta>=6): 
        break
    else: 
        if(scelta==1): 
            #implementazione richiesta 1
            print("Media gol segnati in tutte le partite: ", mediaGolPartite(tupla_partite))

        elif(scelta==2): 
            #implementazione richiesta 2
            squadra=str(input("Inserisci nome squadra di cui vuoi visualizzarne la media dei gol: "))
            if(mediaGolSquadra(tupla_partite, squadra)<=0):
                print("La squadra non esiste!")
            else: 
                print(f"Media gol {squadra}: {mediaGolSquadra(tupla_partite, squadra)}")

        elif(scelta==3):
            #implementazione richiesta 3
            print("Partita con più gol: ", partitaConPiuGol(tupla_partite))

        elif(scelta==4): 
            #implementazione richiesta 4
            print("Partita con meno gol: ", partitaConMenoGol(tupla_partite))

        elif(scelta==5):
            #implementazione richiesta 5
            squadra=str(input("Inserisci nome squadra di cui calcolarne la percentuale di vittorie: "))
            print(percentualeVittoreSquadra(f"{tupla_partite, squadra}%"))

