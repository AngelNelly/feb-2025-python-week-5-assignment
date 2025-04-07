class AngelNelly:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health


    
    def attack(self):
        print(f"{self.name} is attacking with {self.power}!")

    def heal(self):
        self.health += 10
        print(f"{self.name} is healing! Health is now {self.health}.")



hero1 = AngelNelly("Captain Code", "Super Coding", 100)



hero1.attack()
hero1.heal()






class FlyingAngel(AngelNelly):
    def __init__(self, name, power, health, wing_span):
        super().__init__(name, power, health)
        self.wing_span = wing_span


    
    def fly(self):
        print(f"{self.name} is flying with wings of {self.wing_span} meters!")



flying_hero = FlyingAngel("Sky Soar", "Super Flight", 100, 15)

flying_hero.attack()
flying_hero.fly()




