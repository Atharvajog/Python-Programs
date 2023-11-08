class car:
    wheels=4
    def __init__(self):
        self.colour="blue"
        self.material="iron"

    @classmethod
    def info(cls,self):
        return cls.wheels , self.colour

c1=car()
c2=car()
car.wheels=5
print(c1.colour,c1.material,c1.wheels)
print(c2.colour,c2.material,c2.wheels)
print(car.info(c1))