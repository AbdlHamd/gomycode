import numpy as np

def get_student_name(index):
    """Retourne un nom par défaut pour un étudiant"""
    return f"Etudiant_{index + 1}"

def calculate_grade(percentage):
    """Calcule la mention en fonction du pourcentage"""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"

def main():
    print("=" * 70)
    print("PROGRAMME DE CALCUL DES NOTES DES ETUDIANTS")
    print("=" * 70)
    
    try:
        num_students = int(input("Entrez le nombre d'etudiants: "))
        num_subjects = int(input("Entrez le nombre de matieres: "))
        
        if num_students <= 0 or num_subjects <= 0:
            print("Erreur: Le nombre d'etudiants et de matieres doit etre positif.")
            return
        
        print("\n" + "-" * 70)
        print("SAISIE DES NOTES")
        print("-" * 70)
        
        grades = np.zeros((num_students, num_subjects), dtype=float)
        
        for i in range(num_students):
            print(f"\nEtudiant {i + 1}:")
            for j in range(num_subjects):
                while True:
                    try:
                        note = float(input(f"  Note pour la matiere {j + 1} (sur 100): "))
                        if 0 <= note <= 100:
                            grades[i, j] = note
                            break
                        else:
                            print("  Erreur: La note doit etre comprise entre 0 et 100.")
                    except ValueError:
                        print("  Erreur: Veuillez entrer un nombre valide.")
        
        total_marks = np.sum(grades, axis=1)
        
        max_possible = num_subjects * 100
        percentages = (total_marks / max_possible) * 100
        
        grades_list = []
        for percentage in percentages:
            grades_list.append(calculate_grade(percentage))
        
        print("\n" + "=" * 70)
        print("RESULTATS DES ETUDIANTS")
        print("=" * 70)
        
        print(f"\n{'Etudiant':<20} {'Total':<12} {'Pourcentage':<15} {'Mention':<10}")
        print("-" * 70)
        
        for i in range(num_students):
            name = get_student_name(i)
            print(f"{name:<20} {total_marks[i]:<12.2f} {percentages[i]:<15.2f} {grades_list[i]:<10}")
        
       
        
    except ValueError:
        print("Erreur: Veuillez entrer des nombres valides.")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

if __name__ == "__main__":
    main()