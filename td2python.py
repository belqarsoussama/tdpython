#*****TD2*******
#EX1
a=int (input("donner un nombre"))
n=a+a*a+a*a*a+a*a*a*a
print("{a}+{a}{a}+{a}{a}{a}+{a}{a}{a}{a}={n}")
#Ex2
x = int(input("Donnez un nombre : "))

for i in range(1, x + 1):
    for j in range(1, i + 1):
        print("*", end=" ")  
    print()  
#EX2 2
x = int(input("Donnez un nombre : "))

for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(f"{j}", end=" ")  
    print()  
#Ex3
import random

aleatoire = random.randint(1, 100)
essais = 7

print("******* Nous allons jouer à un petit jeu. Vous devez deviner un nombre entre 1 et 100 en un maximum de 7 essais *******")

for i in range(1, 8):  
    n = int(input(">>> "))

    if n < 1 or n > 100:
        print("Nombre en dehors de l'intervalle.")
    elif n < aleatoire:
        print("Un peu plus grand.")
    elif n > aleatoire:
        print("Un peu plus petit.")
    elif n == aleatoire:
        print(f"Bravo, {aleatoire} est le nombre que j'ai choisi. Vous l'avez deviné en {i} essais.")
        break

    essais -= 1

if essais == 0:
    print(f"J'ai gagné. Le nombre que j'ai choisi était {aleatoire}.")
#Ex4
L = [1, -30, 0, -2, 500, 4, 2, 100]

# Séparer les nombres négatifs et positifs tout en conservant l'ordre
M = [x for x in L if x < 0] + [x for x in L if x >= 0]

print(M)
#Ex5
def inserer_valeur_triee(L, val):
    index = 0
    while index < len(L) and L[index] < val:
        index += 1
    L.insert(index, val)

# Exemple d'utilisation
L = [1, 3, 5, 7, 9]
valeur_a_inserer = 4
inserer_valeur_triee(L, valeur_a_inserer)
print(L)
#EX6
L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]

nombre_a_supprimer = int(input("Entrez le nombre à supprimer : "))
L = [x for x in L if x != nombre_a_supprimer]

print(L)
#EX7
L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]

L_sans_doublons = list(dict.fromkeys(L))

print(L_sans_doublons)
#EX8
L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]

nombre_recherche = int(input("Entrez le nombre à rechercher : "))
occurrences = [i for i, x in enumerate(L) if x == nombre_recherche]

if len(occurrences) > 0:
    print(f"Nombre d'occurrences : {len(occurrences)}")
    print(f"Indices des occurrences : {occurrences}")
else:
    print("Le nombre n'a pas été trouvé dans la liste.")
#EX9
# Taux de conversion
taux_euro_mad = 10.86
taux_mad_euro = 0.092

# Demander la direction de la conversion
conversion_direction = input("Choisissez la direction de la conversion (euro en mad ou mad en euro) : ").lower()

# Initialisation de la liste des valeurs converties
valeurs_converties = []

while True:
    valeur = float(input("Saisissez une valeur (nombre négatif pour arrêter) : "))
    
    if valeur < 0:
        break
    
    if conversion_direction == "euro en mad":
        valeur_convertie = valeur * taux_euro_mad
        valeurs_converties.append(valeur_convertie)
    elif conversion_direction == "mad en euro":
        valeur_convertie = valeur * taux_mad_euro
        valeurs_converties.append(valeur_convertie)
    else:
        print("Direction de conversion non reconnue. Veuillez choisir 'euro en mad' ou 'mad en euro'.")

# Afficher les valeurs converties
print(f"Les valeurs converties en {conversion_direction} sont :")
for valeur in valeurs_converties:
    print(valeur)

#EX10
L1 = [1, 3, 6, 78, 35, 88, 55]
L2 = [12, 24, 35, 24, 88, 120, 155]

# Utilisation de l'opération d'intersection entre ensembles
L3 = list(set(L1) & set(L2))

print(L3)

#EX11
L = [8, 24, 48, 2, 16]

# Utilisation du slicing pour inverser l'ordre des éléments
L_mirror = L[::-1]

print(L_mirror)




