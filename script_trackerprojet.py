#Application suivi de dépense avec la list comprehension
from datetime import date 
import csv 

filemane='suivi_depense.csv' 
date=date.today()
date=date.strftime('%d/%m/%Y')
Depense=[]
stop =False

with open(filemane,'a',newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Date","Depense"])
    while not stop:
        d=int(input("Quelles sont vos dépenses de la journée? (Tapez 0 pour cloturer la saisie)"))
        if d==0:
            stop=True 
        else:
            writer.writerow([date,d])
        Depense.append(d)
file.close() 
print("Voici la liste de vos dépenses",Depense) 
print("La somme de vos dépenses est de",sum(Depense))
