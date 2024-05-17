class Vehicule:
    couleur = "Bleu"
    total_vehicules = 0
    def __init__(self,max_speed,kilometrage,nb_places):
        self.max_speed = max_speed
        self.kilometrage = kilometrage
        self.nb_places = nb_places
        Vehicule.total_vehicules += 1

    def nombre_de_places(self):
        return self.nb_places

    def __eq__(self, other):
        return self.max_speed == other.max_speed and self.kilometrage == self.kilometrage and self.nb_places == other.nb_places
    def __ne__(self, other):
        return not (self == other)
    def __gt__(self,other):
        return self.nb_places > other.nb_places
    def __lt__(self,other):
        return self.nb_places < other.nb_places
    
    def __str__(self):
        return f"max_speed : {self.max_speed}\nKilometrage : {self.kilometrage}\nNombre de Places : {self.nombre_de_places()}"

class Bus(Vehicule):
    def __init__(self, max_speed, kilometrage, nb_places = 50):
        super().__init__(max_speed, kilometrage,nb_places)

    def nombre_de_places(self):
        return super().nombre_de_places()
    
    def __eq__(self, other):
        return super().__eq__(other)
    def __ne__(self, other):
        return super().__ne__(other)
    def __gt__(self, other):
        return super().__gt__(other)
    def __lt__(self, other):
        return super().__lt__(other)
    
    def __str__(self):
        return super().__str__()

class Voiture(Vehicule):
    def __init__(self, max_speed, kilometrage,nb_places):
        super().__init__(max_speed, kilometrage,nb_places)

    def nombre_de_places(self):
        return super().nombre_de_places()
    
    def __eq__(self, other):
        return super().__eq__(other)
    def __ne__(self, other):
        return super().__ne__(other)
    def __gt__(self, other):
        return super().__gt__(other)
    def __lt__(self, other):
        return super().__lt__(other)
    
    def __str__(self):
        return super().__str__()

if __name__ == "__main__" :
    mon_bus = Bus(80,34_000)
    ma_voiture = Voiture(220,12_000,5)
    
    print(mon_bus)
    print(ma_voiture)

    vehicule1 = Vehicule(220,22_000,5)
    vehicule2 = Vehicule(220,22_000,5)
    vehicule3 = Vehicule(120,12_000,50)

    print(vehicule1 == vehicule2)
    print(vehicule1 != vehicule3)
    print(vehicule1 < vehicule3)

    print(mon_bus == ma_voiture)
    print(Vehicule.total_vehicules)