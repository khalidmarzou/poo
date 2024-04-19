class Salarie:
    tauxCs = 0.23
    def __init__(self,matricule = 0,nom = "",prenom = "",salaire = float(0)):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
    def __str__(self):
        return f"Matricule : {self.matricule} Nom et Prenom {self.nom} - {self.prenom} Salaire de Base : {self.salaire} TauxCs : {self.tauxCs} SalaireNET : {self.calculerSalaireNet()}"
    def calculerSalaireNet(self):
        salaireNet = self.salaire - (self.salaire * self.tauxCs)
        return salaireNet

if __name__ == '__main__':
    firstSalarie = Salarie(56898,'MARZOUG','KHALID',7000.51) #firsSalaire est de type Salarie()
    secondSalarie = Salarie(56899,'SIDQUI','ZAKARIA',9000.7)
    print(f"{firstSalarie}\n{secondSalarie}")