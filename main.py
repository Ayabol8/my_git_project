class Car:
      def __init__(self, *, brand: str, model: str, price: int) -> None:
            self.brand = brand
            self.model = model
            self.price = price
            self.discount = self.discount

      def __str__(self):
            print(f"Car: {self.brand}, model: {self.model}, price: {self.price}")


car1 = Car(brand="Audi", model="RS7", price=150000)
print(car1)