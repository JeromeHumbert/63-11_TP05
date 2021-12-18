import os

lettres_autorisees: str = "abcdefghijklmnopqrstuvxyzéêèëàâäîïöôûü"
chemin: str = os.path.abspath("./textes")
if os.path.exists(chemin):
    files = [f for f in os.listdir(chemin) if f.endswith('.txt')]
    #Insérer votre code ici. Je vous encourage à faire des fonctions ;) 
else:
    print("Chemin inexistant : %s" % chemin)
