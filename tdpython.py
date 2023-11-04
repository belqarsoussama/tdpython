# ********td1*********
# EX1
a = input("Saisir une valeur : ")  

a = int(a)

b = a + 1

print(b)
#EX2
age = int(input("Entrez votre âge : "))

taille = float(input("Entrez votre taille en mètres : "))

message = "Vous avez {} ans et vous mesurez {:.2f} m.".format(age, taille)

print(message)
#Ex3

distance_km = float(input("Entrez la distance en kilomètres : "))

temps_minutes = float(input("Entrez le temps en minutes : "))

distance_m = distance_km * 1000

temps_s = temps_minutes * 60

vitesse_ms = distance_m / temps_s

print("La vitesse est de {:.2f} mètres par seconde.".format(vitesse_ms))
#Ex4
secondes = int(input("Entrez un nombre de secondes : "))

heures = secondes // 3600  
secondes_restantes = secondes % 3600
minutes = secondes_restantes // 60  
secondes_final = secondes_restantes % 60

print(f"{secondes} secondes = {heures}h {minutes}min {secondes_final}sec")
#Ex5
nombre = int(input("Entrez un nombre : "))

if nombre % 2 == 0:
    print("Ce nombre est pair")
elif nombre % 2 != 0 and nombre % 3 == 0:
    print("Ce nombre est impair, mais est multiple de 3")
else:
    print("Ce nombre n'est ni pair ni multiple de 3")
#Ex6
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

if (nombre1 > 0 and nombre2 > 0) or (nombre1 < 0 and nombre2 < 0):
    print("Le produit serait positif.")
else:
    print("Le produit serait négatif.")
 #EX7
    
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

operation = input("Entrez l'opération (+, -, *, /) : ")

if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    if nombre2 != 0:
        resultat = nombre1 / nombre2
    else:
        resultat = "Division par zéro impossible"
else:
    resultat = "Opération non valide"

print(f"Résultat : {resultat}")
Ce programme demande à l'utilisateur de saisir deux nombres et une opération, puis effectue l'opération choisie.

Exercice 8 : Moyenne des notes et validation
python
Copy code
total_notes = 0
total_coefficients = 0

for i in range(1, 5):
    note = float(input(f"Note {i} : "))
    coefficient = float(input(f"Coefficient {i} : "))
    
    total_notes += note * coefficient
    total_coefficients += coefficient

moyenne = total_notes / total_coefficients

print(f"Moyenne des 4 notes : {moyenne}")

if moyenne >= 10:
    print("Semestre validé")
elif 7 <= moyenne < 10:
    print("Rattrapage")
else:
    print("Semestre non validé")
#EX8

total_notes = 0
total_coefficients = 0

for i in range(1, 5):
    note = float(input(f"Note {i} : "))
    coefficient = float(input(f"Coefficient {i} : "))
    
    total_notes += note * coefficient
    total_coefficients += coefficient

moyenne = total_notes / total_coefficients

print(f"Moyenne des 4 notes : {moyenne}")

if moyenne >= 10:
    print("Semestre validé")
elif 7 <= moyenne < 10:
    print("Rattrapage")
else:
    print("Semestre non validé")
#EX10 
login = input("Entrez le login : ")
mot_de_passe = input("Entrez le mot de passe : ")

if login == "admin" and mot_de_passe == "admin":
    message = "Bienvenue ! Vous êtes connecté en tant qu'administrateur."
else:
    message = "Le login ou le mot de passe saisi est incorrect."

print(message)
Ce programme demande à l'utilisateur de saisir un login et un mot de passe, puis vérifie s'ils correspondent aux valeurs attendues. Si c'est le cas, il affiche un message de bienvenue en tant qu'administrateur. Sinon, il affiche un message informant l'utilisateur que le login ou le mot de passe saisi est incorrect.

#Ex11
poids = float(input("Entrez votre poids en kilogrammes : "))
taille = float(input("Entrez votre taille en mètres : "))

imc = poids / (taille ** 2)

interpretation = ""
if imc > 40:
    interpretation = "Obésité morbide ou massive"
elif 35 <= imc <= 40:
    interpretation = "Obésité sévère"
elif 30 <= imc < 35:
    interpretation = "Obésité modérée"
elif 25 <= imc < 30:
    interpretation = "Surpoids"
elif 18.5 <= imc < 25:
    interpretation = "Corpulence normale"
elif 16.5 <= imc < 18.5:
    interpretation = "Maigreur"
else:
    interpretation = "Famine"

print(f"Votre IMC est de {imc:.2f}, ce qui correspond à : {interpretation}")
#Ex12
grade = input("Entrez le grade de l'employé (A, B, C, D ou E) : ").upper()
heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))

tarif_horaire = 0
prime = 0

if grade == 'A':
    tarif_horaire = 200
    prime = (heures_travaillees // 20) * 1000
elif grade == 'B':
    tarif_horaire = 150
    prime = (heures_travaillees // 20) * 800
elif grade == 'C':
    tarif_horaire = 120
    prime = (heures_travaillees // 15) * 500
elif grade == 'D':
    tarif_horaire = 100
    prime = (heures_travaillees // 15) * 350
elif grade == 'E':
    tarif_horaire = 80
    prime = (heures_travaillees // 10) * 100

salaire = (tarif_horaire * heures_travaillees) + prime

print(f"Le salaire de l'employé est de {salaire} DH.")





















