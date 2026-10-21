import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1. Charger le dataset
df = pd.read_csv("client_train.csv")

# Afficher les 10 premières lignes
client_0_bills = df.head(10)

print(client_0_bills)

# 2. Type de données de client_0_bills
print(type(client_0_bills))

# 3. Informations générales du dataset
print(df.info())

# 4. Recherche des valeurs manquantes
print(df.isnull().sum())

# 5. Traitement des valeurs manquantes
# Pour les colonnes numériques : remplacer par la médiane
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Pour les colonnes catégorielles : remplacer par le mode
categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Vérification
print(df.isnull().sum())

# 6. Analyse descriptive
print(df.describe())

# 7. Sélection des factures du client train_Client_0

# Méthode 1
client0 = df[df["client_id"] == "train_Client_0"]

# Méthode 2
client0_loc = df.loc[df["client_id"] == "train_Client_0"]

print(client0)
print(client0_loc)

# 8. Transformation de counter_type en numérique

label_encoder = LabelEncoder()

df["counter_type"] = label_encoder.fit_transform(df["counter_type"])

print(df["counter_type"].head())

# 9. Suppression de la colonne counter_statue

df.drop("counter_statue", axis=1, inplace=True)

print(df.head())