# bank_account.py

class Account:
    
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print(f"ERREUR: Le montant du depot doit etre positif (Montant: {amount})")
            return False
        
        self.balance += amount
        print(f"Depot de {amount:.2f} EUR effectue sur le compte {self.account_number}")
        print(f"   Nouveau solde: {self.balance:.2f} EUR")
        return True
    
    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print(f"ERREUR: Le montant du retrait doit etre positif (Montant: {amount})")
            return False
        
        if self.balance >= amount:
            self.balance -= amount
            print(f"Retrait de {amount:.2f} EUR effectue sur le compte {self.account_number}")
            print(f"   Nouveau solde: {self.balance:.2f} EUR")
            return True
        else:
            print(f"Solde insuffisant pour un retrait de {amount:.2f} EUR")
            print(f"   Solde actuel: {self.balance:.2f} EUR")
            return False
    
    def check_balance(self) -> float:
        print(f"Compte {self.account_number} - Titulaire: {self.account_holder}")
        print(f"   Solde actuel: {self.balance:.2f} EUR")
        return self.balance
    
    def __str__(self) -> str:
        return f"Compte #{self.account_number} | Titulaire: {self.account_holder} | Solde: {self.balance:.2f} EUR"


def run_tests():
    print("=" * 60)
    print("SIMULATEUR DE COMPTE BANCAIRE")
    print("=" * 60)
    
    print("\nTEST 1: Operations de base sur un compte")
    print("-" * 40)
    
    mon_compte = Account("FR123456789", "Jean Dupont", 1000.0)
    print(f"Compte cree: {mon_compte}")
    
    print("\n--- Depot de 500 EUR ---")
    mon_compte.deposit(500.0)
    
    print("\n--- Retrait de 300 EUR ---")
    mon_compte.withdraw(300.0)
    
    print("\n--- Verification du solde ---")
    mon_compte.check_balance()
    
    print("\n--- Tentative de retrait de 2000 EUR (solde insuffisant) ---")
    mon_compte.withdraw(2000.0)
    
    print("\n" + "=" * 60)
    print("TEST 2: Compte avec solde initial a zero")
    print("-" * 40)
    
    compte_zero = Account("FR987654321", "Marie Martin", 0.0)
    print(f"Compte cree: {compte_zero}")
    
    print("\n--- Depot de 100 EUR ---")
    compte_zero.deposit(100.0)
    
    print("\n--- Retrait de 50 EUR ---")
    compte_zero.withdraw(50.0)
    
    print("\n--- Tentative de retrait de 100 EUR (solde insuffisant) ---")
    compte_zero.withdraw(100.0)
    
    print("\n" + "=" * 60)
    print("TEST 3: Transactions sur plusieurs comptes")
    print("-" * 40)
    
    compte1 = Account("FR111222333", "Alice Petit", 2000.0)
    compte2 = Account("FR444555666", "Bob Durand", 500.0)
    
    print(f"Compte 1: {compte1}")
    print(f"Compte 2: {compte2}")
    
    print("\n--- Depot de 1000 EUR sur le compte 1 ---")
    compte1.deposit(1000.0)
    
    print("\n--- Retrait de 200 EUR du compte 2 ---")
    compte2.withdraw(200.0)
    
    print("\n--- Verification des soldes finaux ---")
    compte1.check_balance()
    compte2.check_balance()
    
    print("\n" + "=" * 60)
    print("TEST 4: Cas limites")
    print("-" * 40)
    
    compte_limite = Account("FR999888777", "Testeur", 50.0)
    
    print("\n--- Depot de 0 EUR (devrait echouer) ---")
    compte_limite.deposit(0.0)
    
    print("\n--- Retrait de 0 EUR (devrait echouer) ---")
    compte_limite.withdraw(0.0)
    
    print("\n--- Retrait du solde exact (50 EUR) ---")
    compte_limite.withdraw(50.0)
    
    print("\n--- Verification finale ---")
    compte_limite.check_balance()
    
    print("\n" + "=" * 60)
    print("TEST 5: Affichage des informations du compte")
    print("-" * 40)
    
    compte_affichage = Account("FR000111222", "Sophie Legrand", 1500.75)
    print("\nAffichage avec __str__:")
    print(compte_affichage)
    
    print("\n" + "=" * 60)
    print("TOUS LES TESTS TERMINES")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()