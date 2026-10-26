class Car:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def update_mileage(self, mileage):
        self.mileage = mileage

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Mileage:", self.mileage)


c = Car("Toyota", "Innova", 15)

c.display()

c.update_mileage(20)

print("After updating mileage:")
c.display()