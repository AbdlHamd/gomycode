class vente:
    def __init__(self, produit: str, quantite: int, prix_unitaire: float, date: str, client: str):
        self.produit = produit
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire
        self.date = date
        self.client = client

    def total(self) -> float:
        return self.quantite * self.prix_unitaire

    def __repr__(self):
        return f"Vente(produit={self.produit}, quantite={self.quantite}, {self.total} FCFA, client={self.client})"