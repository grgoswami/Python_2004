import os
os.chdir(r'/home/gopi/Python_202004/source')
import toll_booth as tb

# Vehicle is a class
# v0, v1, v2, v3 are all objects
v0 = tb.Vehicle("ABC 123", 'Sedan', 'Toyota Camry', 'Grey')
v1 = tb.Vehicle("XYZ 123", 'SUV', 'Ford Explorer', 'White')
v2 = tb.Vehicle("MNO 456", 'Truck', 'Ford 150', 'Red')
v3 = tb.Vehicle("LMN 789", 'Sports car', 'Lamborghini Aventador', 'Green')

v0.describe()
v1.describe()
v2.describe()
v3.describe()

list_of_vehicles = [v0, v1, v2, v3]
for vh in list_of_vehicles:
    vh.describe()
    
print(v0.kind)
print(v0.make)
print(v3.color)
    
tb0 = tb.TollBooth()
tb0.collect_toll(v0)
tb0.collect_toll(v1)
tb0.collect_toll(v0)
tb0.collect_toll(v2)
tb0.collect_toll(v3)
tb0.collect_toll(v0)

list_of_vehicles = [v0, v1, v2, v3, v0, v2, v1, v3, v0]
for vh in list_of_vehicles:
    tb0.collect_toll(vh)
    
    







