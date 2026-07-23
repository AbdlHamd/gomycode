def calculatrice(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur: La division par zero n'est pas possible."

Choix = "y"

while Choix.lower() != "n":
    
    num1 = float(input("Entrez le premier nombre: "))
    num2 = float(input("Entrez le deuxième nombre: "))
    operation = input("Entrez l'opération (+, -, *, /): ")
    if operation not in ["+", "-", "*", "/"]:
        print("Opération invalide. Veuillez réessayer.")
        continue

    resultat = calculatrice(num1, num2, operation)
    print(f"Résultat: {resultat}")
    

    Choix = input("Voulez-vous effectuer une autre opération? (y/n): ")