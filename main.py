import random

# =========================
# GÉNÉRATION MOT DE PASSE
# =========================
def generer_mdp(longueur, maj, min, chiffres, symboles):
    caracteres = ""

    if maj:
        caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if min:
        caracteres += "abcdefghijklmnopqrstuvwxyz"
    if chiffres:
        caracteres += "0123456789"
    if symboles:
        caracteres += "!@#$%^&*()_-+=<>?/"

    if caracteres == "":
        raise ValueError("Au moins un type de caractère doit être sélectionné.")

    mot_de_passe = ""
    for _ in range(longueur):
        mot_de_passe += random.choice(caracteres)

    return mot_de_passe

print("Générateur de mot de passe")

longueur = int(input("Longueur du mot de passe (8-128): "))
maj = input("Inclure des majuscules ? (o/n): ").lower() == 'o'
min = input("Inclure des minuscules ? (o/n): ").lower() == 'o'
chiffres = input("Inclure des chiffres ? (o/n): ").lower() == 'o'
symboles = input("Inclure des symboles ? (o/n): ").lower() == 'o'

try:
    mot_de_passe = generer_mdp(longueur, maj, min, chiffres, symboles)
    print("Mot de passe généré :", mot_de_passe)
except ValueError as e:
    print("Erreur :", e)

# =========================
# FIN GÉNÉRATION MOT DE PASSE
# =========================