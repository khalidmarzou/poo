from abc import ABC, abstractmethod

# Question 1 : definition d' abstract Class :
class ObjetPostal(ABC):
    def __init__(self, nom_destinataire, adresse_destinataire, code_postal):
        self.nom_destinataire = nom_destinataire
        self.adresse_destinataire = adresse_destinataire
        self.code_postal = code_postal

    def __str__(self):
        return f"destinataire : {self.nom_destinataire} | adresse : {self.adresse_destinataire} | code Postal : {self.code_postal}"
    
    # abstract method :
    @abstractmethod
    def prix(self):
        pass

# Question 2 :
class Lettre(ObjetPostal):
    def __init__(self, nom_destinataire, adresse_destinataire, code_postal,expedie = False):
        super().__init__(nom_destinataire, adresse_destinataire, code_postal)
        self.expedie = expedie

    def __str__(self):
        return super().__str__() + f"\n Expedié en : {'Urgence' if self.expedie else 'recommandé'} | prix Affranchissement : {self.prix()} \n"
    
    def prix(self):
        prix_affranchissement = 5.5
        if (self.expedie) :
            prix_affranchissement += 6
        else :
            prix_affranchissement += 15

        return prix_affranchissement

#Question 3 :
class Colis(ObjetPostal) :
    def __init__(self, nom_destinataire, adresse_destinataire, code_postal,expedie = False, poid = float(0)):
        super().__init__(nom_destinataire, adresse_destinataire, code_postal)
        self.expedie = expedie
        self.poid = poid
    def __str__(self):
        return super().__str__() + f"\n Expedié en : {'Urgence' if self.expedie else 'recommandé'} | Poid : {self.poid} g | prix Affranchissement : {self.prix()} dhs \n"
    
    def prix(self):
        prix_affranchissement = 8 * (self.poid / 100)
        if (not self.expedie) :
            prix_affranchissement += 30

        return prix_affranchissement

# L'instance :
lettre1 = Lettre("zakaria Sidqui", "Bouskoura",21300,False)
print(lettre1)
colis1 = Colis("khalid","casablanca",20000,True,300)
print(colis1)
error1 = ObjetPostal("test","test",00)
print(error1)