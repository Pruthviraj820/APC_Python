class Monster:
    def __init__(self,health,energy):
        self.health=health
        self.energy=energy

class Shark(Monster):
    def __init__(self,health,energy,swim_speed):
        self.swim_speed=swim_speed
        super().__init__(health,energy)


class Bird(Monster):
    def __init__(self, health, energy,flying_speed):
        self.flying_speed=flying_speed
        super().__init__(health, energy)

s=Shark(8,95,170)
b=Bird(9,78,156)

print(s.health,s.energy,s.swim_speed)
print(b.health,b.energy,b.flying_speed)