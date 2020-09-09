
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
    def __init__(self):
        self.toll_charge = {
            'Sedan': 1.0,
            'SUV': 2.0,
            'Truck': 3.0,
            'Sports car': 5.0}        
    
    def collect_toll(self, vehicle):
       self.vehicle = vehicle
       print('In collect_toll: kind={0}, toll_charge={1}'.format(self.vehicle.kind,
                                                                 self.toll_charge[self.vehicle.kind]))
        
