# Chaque action acheter une seul fois
# C'est donc une action complete int
# 500 € par client max

# 1. On calcule le calcul du coup de l'action et on ajoute le pourcentage au bout de 2ans
# 2. On la liste des actions par ordre de rentabilité (prix + pourcentage)

# On créer une liste qui contient des dictionsnaire avec le name,price,profit de chaque action
actions = [
    {
        "name": "action1",
        "price": 20,
        "profit": 5
    },
    {
        "name": "action2",
        "price": 30,
        "profit": 10
    },
    {
        "name": "action3",
        "price": 50,
        "profit": 15
    },
    {
        "name": "action4",
        "price": 70,
        "profit": 20
    },
    {
        "name": "action5",
        "price": 60,
        "profit": 17
    },
    {
        "name": "action6",
        "price": 80,
        "profit": 25
    },
    {
        "name": "action7",
        "price": 22,
        "profit": 7
    },
    {
        "name": "action8",
        "price": 26,
        "profit": 11
    },
    {
        "name": "action9",
        "price": 48,
        "profit": 13
    },
    {
        "name": "action10",
        "price": 34,
        "profit": 27
    },
    {
        "name": "action11",
        "price": 42,
        "profit": 17
    },
    {
        "name": "action12",
        "price": 110,
        "profit": 9
    },
    {
        "name": "action13",
        "price": 38,
        "profit": 23
    },
    {
        "name": "action14",
        "price": 14,
        "profit": 1
    },
    {
        "name": "action15",
        "price": 18,
        "profit": 3
    },
    {
        "name": "action16",
        "price": 8,
        "profit": 8
    },
    {
        "name": "action17",
        "price": 4,
        "profit": 12
    },
    {
        "name": "action18",
        "price": 10,
        "profit": 14
    },
    {
        "name": "action19",
        "price": 24,
        "profit": 21
    },
    {
        "name": "action20",
        "price": 114,
        "profit": 18
    },

]

from itertools import combinations
import csv
import os

# Créer plusieurs portefeuille d'action qui propose des actions avec pour limite 500 et une dont une seul action est achetable
# Pour cela il faudra permuter les actions et créer les listes d'actions.
def create_portefeuille_actions(actions):
    # On créer une liste de toutes les combinaisons possibles limite 500 et une dont une seul action est achetable
    for i in range(1, len(actions)):
        # La fonction combinations permet de créer toutes les combinaisons possibles
        num_combinaisons = 0
        for comb in combinations(actions, i):
            # Pour chaque combinaison on vérifie que le portefeuille que la somme des prix des actions est inférieur à 500
            if verif_portefeuille(comb):
                num_combinaisons += 1
                # on sauvegarde le portefeuille dans un fichier csv
                save_portefeuille_actions(comb, "portefeuille" + str(num_combinaisons) + ".csv")

            else :
                print("Le portefeuille est trop cher")

def verif_portefeuille(portefeuille):
    # On vérifie que la somme des prix des actions est inférieur à 500
    if sum([action["price"] for action in portefeuille]) <= 500:
        # print la somme des prix des actions
        print(sum([action["price"] for action in portefeuille]))
        return True
    else :
        # print la somme des prix des actions
        print(sum([action["price"] for action in portefeuille]))
        return False
    
# On stockent les informations dans un fichier csv
def save_portefeuille_actions(portefeuille_actions, portefeuille_name):
    # On créer un dossier pour stocker les portefeuilles
    os.makedirs("portefeuilles", exist_ok=True)
    # On créer le chemin du fichier
    portefeuille_name = os.path.join("portefeuilles", portefeuille_name)
    # On créer le fichier csv
    with open(portefeuille_name, "w") as csvfile:
        # On créer un objet writer
        writer = csv.writer(csvfile)
        # On écrit les données dans le fichier csv
        writer.writerow(["name", "price", "profit"])
        for action in portefeuille_actions:
            writer.writerow([action["name"], action["price"], action["profit"]])
        
# Eexecute la fonction
create_portefeuille_actions(actions)