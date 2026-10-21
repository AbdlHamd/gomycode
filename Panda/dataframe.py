import pandas as pd  

# Création du DataFrame
data = {
    'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
    'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
    'Age': [30, 40, 25, 35, 45, 28],
    'Sexe': ['Homme', 'Femme', 'Homme', 'Femme', 'Homme', 'Femme'],
    'Salaire': [50000, 60000, 45000, 55000, 70000, 55000],
    'Expérience': [3, 7, 2, 5, 10, 4]
}

employee_df = pd.DataFrame(data)

# 1. Sélectionner les 3 premières lignes avec iloc
print("Les 3 premières lignes :")
print(employee_df.iloc[:3])

# 2. Sélectionner les employés du département Marketing avec loc
print("\nEmployés du département Marketing :")
print(employee_df.loc[employee_df['Department'] == 'Marketing'])

# 3. Sélectionner les colonnes Age et Sexe pour les 4 premières lignes
print("\nColonnes Age et Sexe des 4 premières lignes :")
print(employee_df.iloc[:4, [2, 3]])

# 4. Sélectionner les colonnes Salaire et Expérience pour les employés de sexe Homme
print("\nSalaire et Expérience des employés de sexe Homme :")
print(employee_df.loc[employee_df['Sexe'] == 'Homme', ['Salaire', 'Expérience']])
