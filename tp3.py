//Ex1
def somme(m, n):
    total = 0
    for i in range(m, n + 1):
        total += i
    return total
//Ex2 Fonctions pour les équations du second degré
def delta(a, b, c):
    return b**2 - 4*a*c

def NombreRacine(a, b, c):
    d = delta(a, b, c)
    if d > 0:
        return 2
    elif d == 0:
        return 1
    else:
        return 0

def AfficheNombreRacine(a, b, c):
    num_racines = NombreRacine(a, b, c)
    if num_racines == 2:
        print("Il y a deux solutions.")
    elif num_racines == 1:
        print("Il y a une solution.")
    else:
        print("Il n'y a pas de solution réelle.")

def Racine1(a, b, c):
    d = delta(a, b, c)
    if d >= 0:
        return (-b + d**0.5) / (2*a)

def Racine2(a, b, c):
    d = delta(a, b, c)
    if d >= 0:
        return (-b - d**0.5) / (2*a)
//Fonction conversion_temps pour convertir un horaire en secondes :
def conversion_temps(h, m, s):
    return h * 3600 + m * 60 + s
//Calcul du temps écoulé entre deux horaires en secondes :
def temps_ecoule(h1, m1, s1, h2, m2, s2):
    temps1 = conversion_temps(h1, m1, s1)
    temps2 = conversion_temps(h2, m2, s2)
    return abs(temps2 - temps1)
//Fonction conversion_distance pour convertir une distance en mètres :
def conversion_distance(km, m, cm):
    return km * 1000 + m + cm / 100
//Fonction vitesse pour calculer la vitesse en m/s en utilisant les fonctions de conversion de temps et de distance :
def vitesse(distance_km, distance_m, distance_cm, heures, minutes, secondes):
    distance_meters = conversion_distance(distance_km, distance_m, distance_cm)
    temps_secondes = conversion_temps(heures, minutes, secondes)
    if temps_secondes != 0:
        return distance_meters / temps_secondes
    else:
        return None  # Pour éviter la division par zéro
