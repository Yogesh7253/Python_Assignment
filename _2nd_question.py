class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name : {self.name} \nAge : {self.age}")
    
    def get_info(self):
        print(f"Coat_color : {self.coat_color}")
    
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color,trained):
        super().__init__(name, age, coat_color)
        self.trained = trained
    
    def owner(self):
        print(f"Owner of {self.name} dog is Mr. John.")
        
    def city(self):
        print(f"{self.name} lives in Los Angeles with his owner.")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color,friendly):
        super().__init__(name, age, coat_color)
        self.friendly = friendly

    def height(self):
        print(f"Height of {self.name} is 2 feet.")
    
    def weight(self):
        print(f"Weight of {self.name} is 50kg.")

dog = Dog("Pablo",4,"Black and White")
dog.description()
dog.get_info()

jack = JackRussellTerrier("Skuby",5,"Black","yes")
jack.description()
jack.get_info()
jack.owner()
jack.city()

bull = Bulldog("Tyson",3,"Brown","Yes")
bull.description()
bull.get_info()
bull.height()
bull.weight()






