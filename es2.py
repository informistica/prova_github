tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        ("marzo", ("elettrico", 290)), 
        ("marzo", ("gas", 130))
        # Aggiungi altri mesi e consumi
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 290)), 
        ("marzo", ("gas", 130))
        # Aggiungi altri mesi e consumi
    ]),
    ("Bergamo", [
        ("gennaio", ("elettrico", 270)),
        ("gennaio", ("gas", 120)),
        ("febbraio", ("elettrico", 265)),
        ("febbraio", ("gas", 150)),
        ("marzo", ("elettrico", 300)), 
        ("marzo", ("gas", 140))
        # Aggiungi altri mesi e consumi
    ])
)

def analizzaConsumiEnergetici(citta, risorsa): 
    mediaRisorsa=0
    cont=0
    #mediaRisorsa
    for nomeCitta, dati in tupla_consumi_energetici: 
        if(citta==nomeCitta):
            #print(nomeCitta)
            #print(dati)
            for mesi, tipo in dati: 
                #print("mesi: ",mesi)
                #print("tipo: ",tipo)
                if(risorsa==tipo[0]):
                    mediaRisorsa+=tipo[1]
                    cont+=1
    #maxRisorsa
    for nomeCitta, dati in tupla_consumi_energetici: 
        max=0
        for mesi, tipo in dati: 
            if(tipo[1]>max):
                max=tipo[1]
    #meseMaxRisorsa
    for nomeCitta, dati in tupla_consumi_energetici: 
        meseMax=[]
        for mesi, tipo in dati: 
            if(max==tipo[1]):
            
                meseMax=mesi
    if(mediaRisorsa==0 and max==0 and meseMax==[]):
        print("Città inesistente")
    else:
        return (mediaRisorsa/cont, max, meseMax)


citta=str(input("inserisci città di cui vuoi visualizzare la media, il massimo delle risorse e il mese massimo di risorsa: "))
risorsa=str(input("inserisci risorsa: "))
print(analizzaConsumiEnergetici(citta, risorsa))