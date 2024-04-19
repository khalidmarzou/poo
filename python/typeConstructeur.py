#Constructeur par defaut :
class Stagiaire :
    def __init__(self):
        self.nom : ""
        self.prenom : ""
        self.age : 0
#Constructeur Parametres :
class Centre :
    def __init__(self,num,n,l):
        self.numero = num
        self.nom = n
        self.location = l

S1 = Stagiaire()
S1.nom = "marzoug"
S1.prenom = "khalid"
S1.age = 24

print(S1.nom)

C1 = Centre(12,"ISFO","Casablanca")

print(C1.nom)