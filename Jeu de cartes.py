"""
Demande à l'user l'animal restant dans le tuple parmis la liste.
Insérer l'animal dans la liste d'affichage finale, puis comparer de gauche à droite (si plus grand, stop boucle car bon endroit.).
"""

from random import randint 

animauxoriginal = [("La cigogne", 27), ("Le sanglier", 15), ("Le saumon atlantique", 5), ("Le lama", 20), ("L'écureuil", 6)]
animaux = animauxoriginal.copy()
def jeu(animaux):
    """
    Cette fonction permet au jeu de fonctionner sur plusieurs tours et de renvoyer des scores
    """
    cardline = []
    anidepart = randint(1,len(animaux)) - 1
    cardline.append(animaux[anidepart])
    print(cardline)
    del(animaux[anidepart])
    while animaux != [] :
        
        tri(animaux,cardline)
        


def tri(animaux,cardline):
    """
    Cette fonction trie et ajoute un animal que l'utilisateur à décidé à la cardline
    """
    choix = user_input(animaux)                        #Nombre entre 1 et 5
    animal = animaux[choix - 1]              #Définit la variable animal              
    for compteur in range(len(animaux)):                                 #Parcourt la liste animaux
        if animal[1] > animaux[compteur][1]:                        # Si l'élément espérance de vie de l'animal est supérieure à l'élément espérence de vie de l'animal dans la liste animaux 
            cardline.insert(compteur, animal)                       
        elif compteur+1 == len(animaux):
            cardline.append(animal)                          #Ajoute l'animal à la cardline
            del(animaux[choix -1])                            #Supprime l'animal de la liste d'animaux
    print(cardline)
    return animaux,cardline

def user_input(animaux):
    """
    Cette fonction gère l'input utilisateur de manière récursive jusqu'à ce que l'utilisateur rentre un nombre correct
    Entree : Choix de l'animal dans la liste
    Sortie : tuple (animal)                                     
    """
    print("Voici les animaux disponibles")
    compteur_ani = 1                            #La variable compteur_ani et la boucle for servent uniquement à l'affichage
    for anim in animaux:
        print(compteur_ani,anim[0])
        compteur_ani += 1
    choix = int(input("Renseigner l'animal choisit grâce au nombre qui lui est associé"))
    if not(1 <= choix <= len(animaux) + 1):                                     #Si choix n'est pas un nombre entre 1 et la longueur maximale de la liste animaux incluses, on rentre dans la boucle
        print("Ce n'est pas l'un des animaux")
        user_input(animaux)                                          #Rappel de la fonction user_input
    else:
        return choix                #Renvoie la variable choix 
        
jeu(animaux)


#Problèmes actuels : -Il faudrait utiliser une boucle while au lieu d'une boucle for dans la fonction tri(), sinon ajout de l'animal 3x ou plus dans la cardline