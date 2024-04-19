#Les liste en POO :
#villes = ['Casa','Rabat','Salé','Tangier']
"""
revision :
    .append() : ajouter
    .pop() : delete the last element
    .insert(index,new element)
    .del : delete the list
    .clear()
    .count()
"""
#print(villes)
#Ex Augmentation du Salaire :
from datetime import date
class Employe :
    def __init__(self,matricule, nom, prenom, dateNaissance, dateEmbouche, salaire):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance
        self.dateEmbouche = dateEmbouche
        self.salaire = salaire
    def __str__ (self):
        return f"matricule : {self.matricule} nom : {self.nom} prenom : {self.prenom} date de naissance : {self.dateNaissance} date Embouche : {self.dateEmbouche} salaire : {self.salaire}"
    def calcAge(self) :
        dateNaissanceList = [self.dateNaissance.year, self.dateNaissance.month, self.dateNaissance.day]
        todayDate = [date.today().year, date.today().month, date.today().day]
        age = todayDate[0] - dateNaissanceList[0]
        return age
    def calcEnciennete (self) :
        dateEmboucheList = [self.dateEmbouche.year, self.dateEmbouche.month, self.dateEmbouche.day]
        todayDate = [date.today().year, date.today().month, date.today().day]
        enciennete = todayDate[0] - dateEmboucheList[0]
        return enciennete
    def augmentationSalaire (self) :
        if self.calcEnciennete() < 5 :
            self.salaire += (self.salaire * 2) / 100
        elif self.calcEnciennete() < 10 :
            self.salaire += (self.salaire * 5) / 100
        else:
            self.salaire += (self.salaire * 10) / 100
        return self.salaire
    def affichage(self):
        print(f"Age : {self.calcAge()} ans __ Enciennete : {self.calcEnciennete()} ans __ Salaire : {self.augmentationSalaire()} £")
e1 = Employe(12345,"MARZOUG","KHALID",date(1999,10,26), date(2020,2,13), 6700.56)
e1.affichage()
print(e1)