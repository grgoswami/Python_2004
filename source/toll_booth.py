
class Vehicle:
    def __init__(self, license_plate, kind, make, color):
        self.license_plate = license_plate
        self.kind = kind
        self.make = make
        self.color = color
        
    def describe(self):
        print('This vehicle: license_plate={0}, kind={1}, make={2}, color={3}'.format(self.license_plate,
            self.kind, self.make, self.color))    

class TollBooth:
    pass

