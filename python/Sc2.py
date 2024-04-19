class Compte :
    taux = 1.2
    numCompte = 0
    def __init__(self, solde = 0):
        Compte.numCompte += 1
        self.nom = str(input("Saisir Votre Nom : "))
        self.prenom = str(input("Saisir Votre Prenom : "))
        self.__solde = solde
    def __str__(self):
        return f"Prenom : {self.prenom} Nom : {self.nom} Num Compte : {self.numCompte} Taux : {self.taux}"
    def getBalance (self):
        print(f"Nom et prenom : {self.nom, self.prenom} __num Compte : {self.numCompte} __ Solde actuel : {self.__solde}")
    def deposer (self):
        ajouter = float(input("Saisir le Montant ajouter : "))
        self.__solde += ajouter
        self.getBalance()
    def retirer (self):
        moins = float(input("Saisir le Montant retirer : "))
        if moins <= self.__solde:
            self.__solde -= moins
        else:
            print("Solde Insufisant")
        self.getBalance()
    def ajouter_interet (self):
        self.__solde = self.__solde * self.taux
        self.getBalance()
if __name__ == "__main__":
    c1 = Compte()
    c1.getBalance()
    c1.deposer()
    c1.retirer()
    c1.ajouter_interet()
    print(c1)