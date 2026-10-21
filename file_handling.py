import numpy as np

# Ouvrir le fichier CSV
file = open("Loan_prediction_dataset.csv", "r")

# Charger les données
data = np.genfromtxt(
    file,
    delimiter=",",
    skip_header=1,
    usecols=8  # colonne LoanAmount (à ajuster si nécessaire)
)

# Supprimer les valeurs manquantes (NaN)
data = data[~np.isnan(data)]

# Calculs statistiques
moyenne = np.mean(data)
mediane = np.median(data)
ecart_type = np.std(data)

# Affichage des résultats
print("Moyenne du montant des prêts :", moyenne)
print("Médiane du montant des prêts :", mediane)
print("Écart-type du montant des prêts :", ecart_type)

# Fermer le fichier
file.close()