#1)concaténation de chaînes de caractères
chaine1 = "Trente" + " " + "jours" + " " + "de" + "Python"

print(chaine1)

#2)
chaine2 = "Codage" + " " + "pour" + " " + "tous"
print(chaine2)

#3)
societe = "Codage pour tous"
print(societe)
print(len(societe))
print(societe.upper())
print(societe.lower())
print(societe.capitalize())
print(societe.title())
print(societe.swapcase())
print(societe.split()[0])
print(societe.lower().index("codage"))
print(societe.replace("codage", "Python"))
print(societe.replace("tous", "tout le monde"))
print(societe.split(' '))

chaine3 = "Facebook" + "," + "Google" + "," + "Microsoft" + "," + "Apple" + "," + "IBM" + "," + "Oracle" + "," + "Amazon"
print(chaine3)
print(chaine2.split()[0])
print(chaine2.split()[-1])
print(chaine2[10])

#Création d'acronymes
acronyme = " ".join([mot[0].upper() for mot in chaine2.split()])


