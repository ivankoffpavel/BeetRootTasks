class Car:
    total_num_of_cars = 0
    def __init__(self,brand,model,year,color):
        self.color = color
        self.year = year
        self.model = model
        self.brand = brand
        self.total_km=0
        Car.total_num_of_cars+=1

    def car_info(self):
        print('The car is:',self.brand)
        print('Model is:',self.model)
        print('Color is:',self.color)
        print('Year is:',self.year)
    def made_km(self,run_km):
        self.total_km+=run_km
        print('Total km:',self.total_km)
    def repaint(self,color):
        self.color = color

Car_1 = Car('Volvo','V50',1998,'Red')
Car_2 = Car('BMW','m5',2005,'Green')
Car_1.car_info()
Car_1.made_km(10000)
print('Total num of cars:',Car.total_num_of_cars)
print(type(Car_1))

