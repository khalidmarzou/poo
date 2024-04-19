#EX1 :
    #Ecrire En python une clesse <<Rectangle>> ayant deux variables <<a>> et <<b>>
    #et une fonction membre <<surface()>> qui retournera la surface du rectangle.

#Definition du classe :
""""
class Rectangle :
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b
    def surface(self):
        s = self.a * self.b
        return s
#Instanciation classe --> Objet :
Rectangle1 = Rectangle(10,2)
print(f"La surface est : {Rectangle1.surface()}")

#EX2 :
class Somme :
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
    def som(self):
        sommeN = self.n1 + self.n2
        return sommeN
#L'instanciation :
somme1 = Somme()
somme1.n1 = int(input("Saisir le nembre 1 : "))
somme1.n2 = int(input("Saisir le nembre 2 : "))
#Afichage :
print(f"La somme du {somme1.n1} et {somme1.n2} est : {somme1.som()}")
"""
"""
Ex3:
implementez la classe <<Etudiant>> avec les membres suivants:
nom : string
note1, note2 : float
calc_moy() : calcule la note moyenne
afficher() : affiche le nom et la note moyenne
Demandez a l'utilisateur d'entrer le nom et les notes d'un étudiant.
et affiche leur nom et la note moyenne. """

#meriem.onzy@ofppt.ma

#Solution EX3 :
""""class Etudiant :
    def __init__(self):
        self.nom = str(input("Saisir Le nom d'etudiant : "))
        self.note1 = float(input("Saisir la premiere note : "))
        self.note2 = float(input("Saisir la deuxieme note : "))
    def calc_moy(self):
        moy = (self.note1 + self.note2) / 2
        return moy
    def afficher(self):
        print(f"nom : {self.nom} __ note Moyenne : {self.calc_moy()}")

etudiant1 = Etudiant()
etudiant1.afficher()
"""
class Etudiant:
    def __init__(self):
        self.nom = str(input("saisir le nom : "))
        self.notes = []
        self.n = int(input("saisir le nembre des notes : "))
        self.total = 0
        self.moy = 0
    def collect_notes(self):
        for i in range (self.n):
            self.notes.append(float(input(f"entre la note {i+1} : ")))
            self.total += self.notes(i)
        self.moy = self.total/self.n
        return self.moy
    def afichage(self):
        print(f"nom : {self.nom} ___ note moyenne {self.collect_notes()}")

Etudiant1 = Etudiant()
Etudiant1.afichage()