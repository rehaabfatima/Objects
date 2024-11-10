class Parrot:
    species="bird"

    def __init__ (self,name,age):
        self.name=name
        self.age=age
        

blu= Parrot("blu",10)
woo=Parrot("woo",16)

print("blu is a {}".format(blu.species))
print("woo is also a {}".format(woo.species))

print("{} is a bird its age is {}".format(blu.name,blu.age))
print("{} is a bird its age is {}".format(woo.name,woo.age))
