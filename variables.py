#EXERCICES - JOUR 2

#EXERCICES: niveau 1

#1)Création du dossier Day_2 et du fichier variables.py 

#2) Jour 2: 30 Days of Python Programming

#3 - 4 - 5 - 6 - 7) Les variables
prenom = "Freeman"
nom_de_famille = "SEGUE"
nom_complet = prenom + " " + nom_de_famille
pays = "TOGO"
municipale = "Lomé" 
an = 2007
est_Married = False
is_True = True
IS_light_on = True

#8) Déclaration variable multiple sur une seule ligne
x, y, quartier = 5.4, 10, "Tokoin"


#EXERCICES - niveau 2
#1) Vérification du type de données des variables
print(type(prenom))          # str
print(type(nom_de_famille))  # str
print(type(nom_complet))     # str
print(type(pays))            # str
print(type(municipale))      # str
print(type(an))              # int
print(type(est_Married))     # bool
print(type(is_True))         # bool
print(type(IS_light_on))     # bool
print(type(x))               # float
print(type(y))               # int
print(type(quartier))        # str

#2) Trouver la longueur de la chaîne de caractères
print(len(prenom))          # Longueur de la chaîne 'prenom'

#3) Comparaison entre la longueur de prenom et nom_de_famille
print(len(prenom) == len(nom_de_famille))  # Vérifie si les longueurs sont égales
print(len(prenom) != len(nom_de_famille))  # Vérifie si les longueurs sont différentes
print(len(prenom) < len(nom_de_famille))   # Vérifie si la longueur de 'prenom' est inférieure à celle de 'nom_de_famille'
print(len(prenom) > len(nom_de_famille))   # Vérifie si la longueur de 'prenom' est supérieure à celle de 'nom_de_famille'

#4) Déclaration de variables pour stocker des entiers
num_one = 5
num_two = 4

#5 - 6 - 7 - 8 - 9 - 10 - 11) Calcul de la somme, différence, produit, division et reste de la division

sum_result = num_one + num_two
diff_result = num_one - num_two
prod_result = num_one * num_two
div_result = num_one / num_two
reste = num_one % num_two 
quotient = num_one // num_two

# Affichage des résultats
print("Somme:", sum_result)          # Affiche la somme
print("Différence:", diff_result)    # Affiche la différence
print("Produit:", prod_result)        # Affiche le produit
print("Division:", div_result)        # Affiche la division
print("Reste de la division:", reste)  # Affiche le reste de la division
print("Quotient:", quotient)          # Affiche le quotient

#12)soit un cercle de rayon 30
#i)Calcul de l'aire d'un triangle
rayon = 30
pi = 3.14
area_of_circle = rayon * rayon * pi
print("Aire du triangle:", area_of_circle)  # Affiche l'aire du triangle

#ii)Calcul de la circonférence du cercle
circum_of_circle = 2 * pi * rayon
print("Circonférence du cercle:", circum_of_circle)  # Affiche la circonférence du cercle

#iii)Prenon le rayon comme entrée utilisateur et calculons la zone du cercle
rayon_utilisateur = float(input("Entrez le rayon du cercle: "))
area_of_circle_user = rayon_utilisateur * rayon_utilisateur * pi
print("Aire du cercle avec rayon utilisateur:", area_of_circle_user)  # Affiche l'aire du cercle avec le rayon entré par l'utilisateur


#13)Utilisation de input pour obtenir le nom, le prénom, le pays et l'âge de l'utilisateur 
nom_utilisateur = input("Entrez votre nom: ")
prenom_utilisateur = input("Entrez votre prénom: ")
pays_utilisateur = input("Entrez votre pays: ")
age_utilisateur = int(input("Entrez votre âge: "))

# Affichage des informations de l'utilisateur
print("Nom:", nom_utilisateur)          # Affiche le nom de l'utilisateur
print("Prénom:", prenom_utilisateur)    # Affiche le prénom de l'utilisateur
print("Pays:", pays_utilisateur)        # Affiche le pays de l'utilisateur
print("Âge:", age_utilisateur)          # Affiche l'âge de l'utilisateur

#14) Execution de help("keywords") dans Python Shell ou dans mon fichier Python pour voir les mots-clés réservés
#J'éxécute la commande dans le shell Python

