class SpaceCraft:
    def __init__(self,name, fuel):
        self.name = name
        self.fuel = fuel
    def travel(self):
        print(self.name, "is travelling")    

class CargoShip(SpaceCraft):
    def __init__(self,name, fuel, cargo_weight):
        super().__init__(name, fuel)
        self.cargo_weight = cargo_weight

    def travel(self):
        print("Name :",self.name)
        print("Fuel :",self.fuel)
        print("Cargo Weight :",self.cargo_weight)
        print("Cargo ship is travelling")
        print()


class ResearchShip(SpaceCraft):
    def __init__(self,name, fuel, research_equipment):
        super().__init__(name, fuel)
        self.research_equipment = research_equipment

    def travel(self):
        print("Name :",self.name)
        print("Fuel :",self.fuel)
        print("Research equipment :",self.research_equipment)
        print("Research ship is travelling")
     
ships = [
    CargoShip("CargoShips",100,500),
    ResearchShip("ResearchShips",80,"telescope")
]
for ship in ships:
    ship.travel()