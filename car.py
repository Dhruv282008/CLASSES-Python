class Car():
    def __init__(self, color, model, number, company, speedLimit):
        self.color = color
        self.model = model
        self.number = number
        self.company = company
        self.speedLimit = speedLimit

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped") 

    def getmodel(self, insurance):
        print(self.model + insurance)
 
car = Car("blue", "2002, 1975", 1234, "BMW", 200)
car.start()
car.getmodel("Certified")

audi = Car("white", "Q7", 1234, "Audi", 250)
audi.getmodel("Certified")