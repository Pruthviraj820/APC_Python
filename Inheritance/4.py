class Monster:
    def __init__(self,health,energy):
        self.health=health
        self.energy=energy

class Shark(Monster):
    def __init__(self,health,energy,speed):
        self.speed=speed
        super().__init__(health,energy)
        
s=Shark(9,95,90)
