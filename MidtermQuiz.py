class DistanceConversion:
    def __init__(self, meter):
        self.meter = meter
        import math
        self.per = math.pi

    def centimeter(self):
        return self.meter*100

    def kilometer(self):
        return self.meter/1000

    def inches(self):
        return self.meter * 39.37

    def display(self):
        print("Meter to Centimeter:", self.centimeter())
        print("Meter to Kilometer:", self.kilometer())
        print("Meter to Inches:", self.inches)


convert = DistanceConversion(float(input("Please enter the value of meter: ")))
convert.display()
