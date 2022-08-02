val = input("Entrer une valeur: ")

if(val.isdigit()):
  print("{} est un nombre".format(val))
elif(val.isalpha()):
  print("{} est un alphabet".format(val))
else:
  print("{} est alphanumerique".format(val))