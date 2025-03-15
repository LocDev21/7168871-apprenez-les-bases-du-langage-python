nombre1= input("saisir un entier: ")
nombre2= input("saisir un entier: ")
if not nombre1.isnumeric() and not nombre2.isnumeric():
  print("nombre1 et nombre2 sont des nombres")
  systemExit("Fin du programme")
else:
  nombre1=int(nombre1)
  nombre2=int(nombre2)
operation=input("choisir l'operation a effectuer ['+','-','*' ou '/']: ")
if operation not in ['+','-','*','/']:
  print("l'operation doit etre parmi cette liste ['+','-','*' ou '/']")
  raise systemExit("Fin du programme")
match operation:
  case "+":
    resultat=nombre1+nombre2
  case "-":
    resultat=nombre1-nombre2
  case "*":
    resultat=nombre1*nombre2
  case "/":
    if nombre2==0:
      print("Le second nombre doit etre superieur a 0")
      systemExit("Fin du programme")
    else:
      resultat=round(nombre1/nombre2,2)
print(f("Le resultat de l'operation est : {round(resultat,2)}")
