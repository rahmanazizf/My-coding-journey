class Shinobi:
    def __init__(self, name, age, ultimate_jutsu, rank):
        self.name = name
        self.age = age
        self.ultimate_jutsu = ultimate_jutsu
        self.rank = rank
        self.allies = []
        self.enemies = []
        self.health = 10
        self.chakra = 10
        self.is_god_of_shinobi = False

    def be_ally(self, other_shinobi):
        self.allies.append(other_shinobi.name)
        print("We're now allies, {name}! Let's beat Akatsuki".format(name = other_shinobi.name.split()[0]))
    def attack(self, other_shinobi):
        if self.rank <= other_shinobi.rank:
            other_shinobi.health = other_shinobi.health - 1
            print("{char}: Take this!!! {ult}!!!".format(char = self.name, ult = self.ultimate_jutsu))
            print("{char2}: AAAAARGH".format(char2 = other_shinobi.name))
        else:
            print("I have to ask for assistance! {name} is too strong for me.".format(name = other_shinobi.name))
    def increase_chakra(self):
        if self.is_god_of_shinobi:
            self.chakra += 5
            print("chakra increased by 5")
        else:
            print("you are unable to increase your chakra, you have to practice more to be a great shinobi")
    def __repr__(self):
        desc = "{name} is a shinobi from hidden leaf village. {name}'s ultimate jutsu is {jutsu} which can be his most powerful power to beat {name}'s opponent.\n".format(name = self.name, jutsu = self.ultimate_jutsu)
        desc += "health = {health}.\n".format(health = self.health)
        desc += "chakra = {chakra}.\n".format(chakra = self.chakra)
        return desc


#create object of hokage, the most powerful shinobi in hidden leaf village
#this char should includes special attribute like prohibited jutsu due its danger
class Akatsuki:
    def __init__(self, name, age, ultimate_jutsu, secret_jutsu):
        self.name = name
        self.age = age
        self.ultimate_jutsu = ultimate_jutsu
        self.rank = 1
        self.allies = []
        self.enemies = []
        self.health = 10
        self.chakra = 10
        self.is_god_of_shinobi = False
        self.secret_jutsu = secret_jutsu
    def attack(self, other_shinobi):
        if self.rank < other_shinobi.rank:
            print("This world shall taste pain! {ult}".format(ult=self.ultimate_jutsu))
            print("{others_name}'s health reduced by 1".format(others_name = other_shinobi.name))
            other_shinobi.health = other_shinobi.health - 1
        else:
            print("You are a worthy opponent. I have no choices but to use my secret jutsu. {secret}!!!".format(secret = self.secret_jutsu))
            other_shinobi.chakra = other_shinobi.chakra - 1
            print("{others_name}'s chakra decreased by 1".format(others_name=other_shinobi.name))
    def kill(self, other_shinobi):
        other_shinobi.health = other_shinobi.health - other_shinobi.health
        print("{name}'s health dropped to 0. {name} died.".format(name = other_shinobi.name))
    def revive_ally(self, ally):
        if ally.health == 0:
            print("{name} has revived {other_shinobi}'s. Health increased by 10".format(name = self.name, other_shinobi=ally.name))
            ally.health += 10
        else:
            print("{allyname} is still alive".format(allyname = ally.name))
    def __repr__(self):
        desc = "{name} was a strong shinobi. {name} betrayed his country after commited unforgivable crime and stealing secret jutsu."
        return desc

        



naruto = Shinobi(name="Naruto Uzumaki", age = 20, rank=1, ultimate_jutsu="rasengan")
nagato = Akatsuki(name="Nagato", age=30, ultimate_jutsu="Shinra tensei", secret_jutsu='Chibaku tensei')
for _ in range(5):
    naruto.attack(nagato)
print("nagato health", nagato.health)
nagato.kill(naruto)
print(naruto)
