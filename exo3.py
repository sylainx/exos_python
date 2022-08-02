text = input('veuillez saisir une phrase: ')
lenText = len(text)
print("Le nombre d'occurrence est : {}".format(lenText))

occurrrence = input('veuillez entrer une occurrence a rechercher: ')

if (text.isupper()):
    print(text.upper())
elif(text.isupper()):
    print(text.capitalize())
else:
    print("Enter a valid sentence")
