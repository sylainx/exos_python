recrutements = {
    "programmation": {
        "John Doe": 429,
        "John Pierre": 229,

    },
    "reseaux": {
        "Avril Paul": 271,
        "Appolon Pierre": 129,
    },
    "base_de_donnees": {
        "Tilus Paul": 313,
        "Jerry Poston": 829,
    }
}


def get_participant():
    print("- Programmation")
    for key, val in recrutements["programmation"].items():
        print("\t* {} a obtenu {} pts".format(key, val))

    print("- Reseaux")
    for key, val in recrutements["reseaux"].items():
        print("\t* {} a obtenu {} pts".format(key, val))

    print("- Base de donnees")
    for key, val in recrutements["base_de_donnees"].items():
        print("\t* {} a obtenu {} pts".format(key, val))


def get_participant_by_category(category):
    if category == 1:
        print("\n- Programmation")
        for key, val in recrutements["programmation"].items():
            print("\t* {} a obtenu {} pts".format(key, val))
    elif category == 2:
        print("\n- Reseaux")
        for key, val in recrutements["reseaux"].items():
            print("\t* {} a obtenu {} pts".format(key, val))
    elif category == 3:
        print("\n- Base de donnees")
        for key, val in recrutements["base_de_donnees"].items():
            print("\t* {} a obtenu {} pts".format(key, val))


def get_category_x_more_participant():
    categoryName = ""
    maxValue = 0
    for key, value in recrutements.items():
        if maxValue < len(value.keys()):
            categoryName = key
            maxValue = len(value.keys())
    return categoryName


def get_laureat_everywhere():
    participantName = ""
    maxValue = 0
    for k, y in recrutements.items():
        for key, val in y.items():
            if maxValue < val:
                participantName = key
                maxValue = val

    return [participantName, maxValue]


def get_laureat_by_category(category):
    participantName = ""
    maxValue = 0
    for k, y in recrutements[category].items():
        if maxValue < y:
            participantName = k
            maxValue = y

    return [participantName, maxValue]


def show_sous_menu(command):
    match command:
        case 1:
            print("\n________| Nouveau participant |________\n")
            print("Quel est son domaine?\n ")
            print("1- Programmation")
            print("2- Réseau")
            print("3- Base de données")
            print("0- Retour")
            inputSousMenu = input("R- ")
            if inputSousMenu.isdigit():
                sousMenuInt = int(inputSousMenu)
                if sousMenuInt < 0 or sousMenuInt > 3:
                    print("Incorrect! Le nombre doit etre entre 0 et 3")
                else:
                    if sousMenuInt == 0:
                        print("\nRetour au menu principal \n")
                    if sousMenuInt == 1:
                        create_participant(sousMenuInt)

        case 2:
            print("\n________| Afficher les participants |________\n")
            # afficher toutes les participants
            get_participant()

            temp = input("")
        case 3:

            inputSousMenu = ""
            sousMenuInt = 0
            while True:
                print("\n________| Participants par categorie |________\n")
                print("Quel est son domaine?\n ")
                print("1- Programmation")
                print("2- Réseau")
                print("3- Base de données")
                print("0- Retour")
                inputSousMenu = input("R- ")
                if inputSousMenu.isdigit():
                    sousMenuInt = int(inputSousMenu)
                    if sousMenuInt < 0 or sousMenuInt > 3:
                        print("Incorrect! Le nombre doit etre entre 0 et 3")
                    else:
                        if sousMenuInt == 0:
                            print("\nRetour au menu principal \n")
                            break
                        if sousMenuInt == 1:
                            get_participant_by_category(1)

                        if sousMenuInt == 2:
                            get_participant_by_category(2)
                        if sousMenuInt == 3:
                            get_participant_by_category(3)

                        temp = input("")  # important

            temp = input("")  # important

        case 4:
            print("\n________| Domaine avec plus de participants |________\n")
            print("Le domaine avec le plus de participant est: {}".format(
                get_category_x_more_participant()))
            temp = input("")  # important

        case 5:
            print("\n________| Laureat des laureats |________\n")
            # afficher toutes les participants
            laureatDesLaureats = get_laureat_everywhere()
            print(
                f"Le laureat des laureats est: {laureatDesLaureats[0]} avec {laureatDesLaureats[1]} pts")
            temp = input("")

        case 6:

            inputSousMenu = ""
            sousMenuInt = 0
            laureatCategory=""
            
            while True:
                print("\n________| Laureat d'un domain |________\n")
                print("Quel est son domaine?\n ")
                print("1- Programmation")
                print("2- Réseau")
                print("3- Base de données")
                print("0- Retour")
                inputSousMenu = input("R- ")
                if inputSousMenu.isdigit():
                    sousMenuInt = int(inputSousMenu)
                    if sousMenuInt < 0 or sousMenuInt > 3:
                        print("Incorrect! Le nombre doit etre entre 0 et 3")
                    else:
                        if sousMenuInt == 0:
                            print("\nRetour au menu principal \n")
                            break
                        if sousMenuInt == 1:
                            laureatCategory=get_laureat_by_category("programmation")
                        elif sousMenuInt == 2:
                            laureatCategory=get_laureat_by_category("reseaux")
                        elif sousMenuInt == 3:
                            laureatCategory= get_laureat_by_category("base_de_donnees")

                        print("Le laureat pour {} est: {} avec {} pts".format("ttt",laureatCategory[0], laureatCategory[1]))
                        temp = input("")  # important

            temp = input("")  # important

            temp = input("")

        case other:
            print("Incorrect: ")
            temp = input("")


def create_participant(category):
    nom = input("Entrer son nom: ")
    note = int(input("Entrer sa note( 500 max): "))
    if note < 0 or note > 500:
        print("La Note doit etre entre 0 et 500")
    else:
        if category == 1:
            recrutements["programmation"][nom] = note
        elif category == 2:
            recrutements["reseaux"][nom] = note
        elif category == 3:
            recrutements["base_de_donnees"][nom] = note
        else:
            print("Incorrect")


# =================   M A I N   P R O J E C T   ===============

openLoop = True
inputMenu = " "
p = 0
while openLoop:
    print("\n\n________| MENU PRINCIPAL |________\n")
    print("1- Enregistrer un participant")
    print("2- Afficher tous les participants")
    print("3- Afficher les participants par domaine")
    print("4- Afficher domaine ayant le plus de participant")
    print("5- Afficher le lauréat des lauréats du concours")
    print("6- Affichez le nom complet et la note obtenue du lauréat d’un domaine")
    print("7- Affichez les 5 premiers lauréats du concours sur les 3 domaines")
    print("8- Supprimer les 5 participants qui obtiennent les notes les plus basses du concours")
    print("0- Quitter")
    inputMenu = input("R-: ")
    if inputMenu.isdigit():
        p = int(inputMenu)
        if p < 0 or p > 8:
            print("Incorrect! Le nombre doit etre entre 0 et 8")
        else:
            if p == 0:
                print("\n\n M E R C I    &   A U R E V O I R   !\n\n")
                openLoop = False
                break
            show_sous_menu(p)
    else:
        print("Incorrect! Entrer un nombre correct")
