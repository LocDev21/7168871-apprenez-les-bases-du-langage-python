nombres=input("saisissez une liste de nombres séparés par des virgules: ")
liste=nombres.split(,)
for i in liste:
  nombres_entier=int(nombres)
  liste_entiers.append(nombres_entier)
somme=0
for i in liste_entiers:
  somme=i+somme
print("somme")
moyenne=0
for i  in liste_entiers:
  moyenne=somme/len(liste_entiers)
print("moyenne")
moy_sup=0
for i in liste_entiers:
  if nombre>moyenne:
    moy_sup=moy_sup+1
print(f"le nombre de nombres supérieurs a la moyenne est: {moy_sup}")

  
  
  

