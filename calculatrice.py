import math

class Calculatrice:
    def __init__(self):
        self.operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
        }

    def add_operation(self, symbole, fonction):
        self.operations[symbole] = fonction

    def calculate(self, num1, operation, num2=None):
        if not isinstance(num1, (int, float)):
            raise TypeError("Le premier argument doit être un nombre.")

        if num2 is not None and not isinstance(num2, (int, float)):
            raise TypeError("Le deuxième argument doit être un nombre.")

        if operation not in self.operations:
            raise ValueError("Opération invalide.")

        try:
            return self.operations[operation](num1, num2)
        except Exception as e:
            print(f"Erreur : {e}")
            raise


# Fonctions avancées
def puissance(a, b):
    return a ** b

def racine_carree(a, _):
    if a < 0:
        raise ValueError("Impossible de calculer la racine carrée d'un nombre négatif.")
    return math.sqrt(a)

def logarithme(a, _):
    if a <= 0:
        raise ValueError("Le logarithme est défini uniquement pour les nombres positifs.")
    return math.log(a)


# Programme principal
calculatrice = Calculatrice()

# Ajout des opérations avancées
calculatrice.add_operation("^", puissance)
calculatrice.add_operation("sqrt", racine_carree)
calculatrice.add_operation("log", logarithme)

while True:
    print("\nOpérations disponibles : +, -, *, /, ^, sqrt, log")
    operation = input("Choisissez une opération (ou q pour quitter) : ")

    if operation.lower() == "q":
        print("Au revoir !")
        break

    try:
        num1 = float(input("Entrez le premier nombre : "))

        if operation in ["sqrt", "log"]:
            resultat = calculatrice.calculate(num1, operation)
        else:
            num2 = float(input("Entrez le deuxième nombre : "))
            resultat = calculatrice.calculate(num1, operation, num2)

        print("Résultat :", resultat)

    except ValueError as ve:
        print("Erreur :", ve)

    except TypeError as te:
        print("Erreur :", te)

    except ZeroDivisionError:
        print("Erreur : division par zéro impossible.")