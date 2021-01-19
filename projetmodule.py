import sys
import random
import json

myfile= input("Veuillez saisir le nom de la fichier ")
nombremax= int(input("Saisir nombre max de personnes par groupe: "))
with open(myfile,'r', encoding="utf-8") as i:
    
    lines = i.readlines()

finalliste = []
longueurgroupe=len(lines)
nombrebygroup=longueurgroupe//nombremax

if longueurgroupe%nombremax!=0:
    nombrebygroup += 1

print("Nombre de groupe: ", nombrebygroup)

i=0
while i < nombrebygroup:
    liste=[]
    t=0
    while t<nombremax:
        try:
            personnedansgroupe=random.choice(lines)
            # print(personnedansgroupe)
            liste.append(personnedansgroupe.split())
            lines.remove(personnedansgroupe)
        except:
            break
        t+=1
    finalliste.append(liste)
    i += 1    


    # print(liste)

for liste in finalliste:
    resultat_final = liste
    print(resultat_final)
    

    with open("projet.json", "a") as n:
        json.dump(resultat_final,n)



























