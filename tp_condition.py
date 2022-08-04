import math

# Function to show MIN and MAX element


def min_max_element(tab):
    min = tab[0]
    max = tab[0]
    for i in tab:
        # minimum
        if min > i:
            min = i
        # maximum
        if max < i:
            max = i
    return [min, max]
# End min_max_func


# Function to show fact on  element
def factElement(el):
    fact = 1
    if el == 0:
        fact = 1
    elif fact > 0:
        for i in range(el):
            fact = fact * (i+1)
    else:
        fact = 0

    return fact


# Function to show square root of one element

def racineCarreeElement(el):
    print("Racine carree de {} est: {}".format(el, math.sqrt(el) ))
    # return math.sqrt(el)

# Function to show power of  element


def powerOfElement(val, p):
    somme = 0
    for i in val:
        nombreEleveAlaPuissance = pow(i, p)
        print("{}^{} = {}".format(i, p, nombreEleveAlaPuissance))
        somme = somme + nombreEleveAlaPuissance

    print("\nLa somme des elements eleve a la puissance est: {}\n". format(somme))


#


def sumElements(tab):
    sum = 0
    for i in tab:
        sum = sum + i

    return sum


qte = int(input("entrer la qte a saisir: "))
val = []
if qte >= 4 and qte <= 15:
    i = 0
    while i < qte:
        val.append(int(input("Entrer l'element[{}]: ".format(i+1))))
        i = i + 1

    print("============ QUESTION 1 ===============")
    min_and_max = min_max_element(val)
    print("min = {} \nmax = {}".format(min_and_max[0], min_and_max[1]))

    print("============ QUESTION 2 ===============")
    for i in val:
        if 3%i == 0 and 5%i == 0 and i%2 == 0 and i > 0:
            resultFactorial = factElement(i)
            print("{}! = {}".format(i, resultFactorial))

    print("============ QUESTION 3 ===============")
    for i in range(len(val)):
        if i >=2  and i <=4:
            racineCarreeElement(val[i])

    print("============ QUESTION 4 ===============")
    openLoop = True
    inputPow = ''
    p = 0
    while openLoop:
        inputPow = input("Entrer le nombre a elever(2 ou 3): ")
        if inputPow.isdigit():
            p = int(inputPow)
            if p != 2 and p != 3:
                print("Incorrect! Vous devez tapez 2 ou 3")
            else:
                openLoop = False
                powerOfElement(val, p)
                break
        else:
            print("Incorrect! Choisissez puissance 2 ou 3")

else:
    print("Incorrect")
