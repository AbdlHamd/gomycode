# Question 1 : Écrivez un programme Python qui multiplie tous les éléments d'une liste.
# Example list = [2, 3, 6]
# Résultat = 36

def multiplier_liste(liste):
    resultat = 1
    for element in liste:
        resultat *= element
    return resultat

# Test
ma_liste = [2, 3, 6]
print(multiplier_liste(ma_liste))  # 36

# Question 2 : Écrivez un programme Python pour obtenir une liste, triée par ordre 
# croissant du dernier élément de chaque tuple, à partir d'une liste donnée de tuples non vides.
# Liste type : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Résultat attendu : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# Définir une fonction qui retourne le dernier élément du tuple
def dernier_element(tuple_entree):
    return tuple_entree[-1]  # ou tuple_entree[1] pour un tuple de 2 éléments

def trier_par_dernier_element(liste_tuples):
    # Utiliser la fonction nommée comme key
    liste_tuples.sort(key=dernier_element)
    return liste_tuples

# Test
liste = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
resultat = trier_par_dernier_element(liste)
print(resultat)  # [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# Question 3 : Écrivez un programme Python qui combine deux dictionnaires en 
# ajoutant des valeurs pour les clés communes.
# d1 = {'a' : 100, 'b' : 200, 'c':300}
# d2 = {'a' : 300, 'b' : 200, 'd':400}
# Résultat attendu: {'a' : 400, 'b' : 400, 'd' : 400, 'c' : 300}

def combiner_dictionnaires(d1, d2):
    resultat = d1.copy()
    for cle, valeur in d2.items():
        if cle in resultat:
            resultat[cle] += valeur
        else:
            resultat[cle] = valeur
    return resultat

# Test
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
resultat = combiner_dictionnaires(d1, d2)
print(resultat)  # {'a': 400, 'b': 400, 'c': 300, 'd': 400}

# Question 4 : Avec un nombre entier n donné, écrivez un programme pour générer 
# un dictionnaire qui contient (i, i*i) de sorte que soit un nombre entier entre 1 et n 
# (les deux inclus). Le programme doit ensuite imprimer le dictionnaire.
# Supposons que l'entrée suivante soit fournie au programme : 8
# La sortie devrait alors être : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def generer_dictionnaire_carres(n):
    return {i: i*i for i in range(1, n+1)}

# Test
n = 8
resultat = generer_dictionnaire_carres(n)
print(resultat)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Question 5 : Écrivez un programme pour trier un tuple par son élément flottant.
# Par exemple : list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Résultat attendu: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

def trier_par_flottant(liste):
    return sorted(liste, key=lambda x: float(x[1]), reverse=True)

# Test
liste = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
resultat = trier_par_flottant(liste)
print(resultat)  # [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

# Question 6 : Écrivez un programme Python pour créer un ensemble.
# Exemples : {0, 1, 2, 3, 4}
# Écrire un programme Python pour itérer sur des ensembles.
# Écrire un programme Python pour ajouter des membres dans un ensemble et 
# pour retirer des éléments d'un ensemble donné.

# Créer un ensemble
mon_ensemble = {0, 1, 2, 3, 4}
print("Ensemble initial:", mon_ensemble)

# Itérer sur un ensemble
print("\nItération sur l'ensemble:")
for element in mon_ensemble:
    print(element)

# Ajouter un élément
mon_ensemble.add(5)
print("\nAprès add(5):", mon_ensemble)

# Ajouter plusieurs éléments
mon_ensemble.update([6, 7, 8])
print("Après update([6,7,8]):", mon_ensemble)

# Retirer un élément avec remove (lève une erreur si l'élément n'existe pas)
mon_ensemble.remove(5)
print("Après remove(5):", mon_ensemble)

# Retirer un élément avec discard (ne lève pas d'erreur)
mon_ensemble.discard(10)
print("Après discard(10):", mon_ensemble)

# Retirer un élément aléatoire avec pop
if mon_ensemble:
    element = mon_ensemble.pop()
    print(f"Élément retiré avec pop(): {element}")
    print("Après pop():", mon_ensemble)

# Vider l'ensemble
mon_ensemble.clear()
print("Après clear():", mon_ensemble)

# Question 6 : Écrivez un programme Python pour créer un ensemble.
# Exemples : {0, 1, 2, 3, 4}
# Écrire un programme Python pour itérer sur des ensembles.
# Écrire un programme Python pour ajouter des membres dans un ensemble et 
# pour retirer des éléments d'un ensemble donné.

# Créer un ensemble
mon_ensemble = {0, 1, 2, 3, 4}
print("Ensemble initial:", mon_ensemble)

# Itérer sur un ensemble
print("\nItération sur l'ensemble:")
for element in mon_ensemble:
    print(element)

# Ajouter un élément
mon_ensemble.add(5)
print("\nAprès add(5):", mon_ensemble)

# Ajouter plusieurs éléments
mon_ensemble.update([6, 7, 8])
print("Après update([6,7,8]):", mon_ensemble)

# Retirer un élément avec remove (lève une erreur si l'élément n'existe pas)
mon_ensemble.remove(5)
print("Après remove(5):", mon_ensemble)

# Retirer un élément avec discard (ne lève pas d'erreur)
mon_ensemble.discard(10)
print("Après discard(10):", mon_ensemble)

# Retirer un élément aléatoire avec pop
if mon_ensemble:
    element = mon_ensemble.pop()
    print(f"Élément retiré avec pop(): {element}")
    print("Après pop():", mon_ensemble)

# Vider l'ensemble
mon_ensemble.clear()
print("Après clear():", mon_ensemble)