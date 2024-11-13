from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def get_info(self):
        pass
class BenzSUV(Car):
    def drive(self):
        print("Driving a Benz SUV")

    def get_info(self):
        return "Benz SUV"

class BenzCoupe(Car):
    def drive(self):
        print("Driving a Benz Coupe")

    def get_info(self):
        return "Benz Coupe"

class BmwSUV(Car):
    def drive(self):
        print("Driving a BMW SUV")

    def get_info(self):
        return "BMW SUV"

class BmwCoupe(Car):
    def drive(self):
        print("Driving a BMW Coupe")

    def get_info(self):
        return "BMW Coupe"
class CarFactory(ABC):
    @abstractmethod
    def create_suv(self) -> Car:
        pass

    @abstractmethod
    def create_coupe(self) -> Car:
        pass
class BenzFactory(CarFactory):
    def create_suv(self) -> Car:
        return BenzSUV()

    def create_coupe(self) -> Car:
        return BenzCoupe()

class BmwFactory(CarFactory):
    def create_suv(self) -> Car:
        return BmwSUV()

    def create_coupe(self) -> Car:
        return BmwCoupe()
def main():
    brand = input("Enter car brand (Benz/BMW): ").strip().lower()

    if brand == "benz":
        factory = BenzFactory()
    elif brand == "bmw":
        factory = BmwFactory()
    else:
        print("Unsupported brand")
        return

    suv = factory.create_suv()
    coupe = factory.create_coupe()

    print(f"Created: {suv.get_info()}")
    suv.drive()

    print(f"Created: {coupe.get_info()}")
    coupe.drive()

if __name__ == "__main__":
    main()
