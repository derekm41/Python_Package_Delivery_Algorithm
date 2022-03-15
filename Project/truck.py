from datetime import datetime, timedelta, time
import hashTable
import distance

#Truck class
class Truck:
    def __init__(self):
        self.truck_packages = []
        self.start_time = None
        self.end_time = None
        self.end_mileage = 0

    #function to remove/deliver package from truck
    def deliver_package(self, package):
        self.truck_packages.remove(package)

#global variables to be used to track time.
date = datetime.today()
start_time = datetime(year=date.year, month=date.month, day=date.day, hour=8, minute=0)
delayed_start_time = datetime(year=date.year, month=date.month, day=date.day, hour=9, minute=0)

#Create Truck class objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

#Manually load trucks with package ids
truck1.truck_packages = [40,24,34,29,30,31,1,4,2,7,33,11,23,10,37]
truck2.truck_packages = [3,18,36,38,6,25,28,32,9,26,17]
truck3.truck_packages = [14,15,19,20,21,13,16,27,35,39,22,12,8,5]

#Update which truck each package is on.
#Big O(1)
for packageID in truck1.truck_packages:
    parcel = hashTable.packageHashtable.search(packageID)
    parcel.truckload = 1
    hashTable.packageHashtable.insert(packageID, parcel)
# Big O(1)
for packageID in truck2.truck_packages:
    parcel = hashTable.packageHashtable.search(packageID)
    parcel.truckload = 2
    hashTable.packageHashtable.insert(packageID, parcel)
#Big O(1)
for packageID in truck3.truck_packages:
    parcel = hashTable.packageHashtable.search(packageID)
    parcel.truckload = 3
    hashTable.packageHashtable.insert(packageID, parcel)


#Greedy package delivery algorithm.
#Handles finding nearest package delivery as well as supporting delivery actions.
#Big O(N)
def truckDeliverPackages(truck, starttime):
    #Save the start time to the Truck object's start time.
    truck.start_time = starttime
    start_address = 'HUB'
    next_from_address = ''
    miles_tracker = 0
    time_tracker = ''

    #Get the closest package distance from start address (HUB)
    closest_package_ID, miles = distance.minDistanceFrom(start_address, truck.truck_packages)

    # set delivery status to in route for all packages
    # Big O(N)
    for packageID in truck.truck_packages:
        pack = hashTable.packageHashtable.search(packageID)
        pack.set_Delivery_Status("IN_ROUTE", None)
        #print(pack.get_Delivery_Status())

    # distance/mph
    # track time in a usable format
    #get time into total minutes to then use timedelta to add to time_tracker
    ftimeunformatted = round(miles / 18, 2)
    fminutes = ftimeunformatted * 60
    ftime_to_add = timedelta(minutes=fminutes)
    #add time to time tracker
    time_tracker = truck.start_time + ftime_to_add
    #add miles to miles tracker
    miles_tracker += miles

    #Store next address for next package
    next_from_address = hashTable.packageHashtable.search(closest_package_ID).get_Address()

    #deliver package by updated deliverystatus in the hashtable and remove from truck_packages
    pack = hashTable.packageHashtable.search(closest_package_ID)
    #Update Package delivery status includes time delivered
    pack.set_Delivery_Status("DELIVERED", time_tracker)
    #Update package hashtable
    hashTable.packageHashtable.insert(closest_package_ID, pack)
    #remove from truck_packages list
    truck.deliver_package(closest_package_ID)

    #Repeat and continue with the rest of packages in truck packages list.
    # Big O(N)
    while len(truck.truck_packages) > 0:
        closest_next_package_ID, nextmiles = distance.minDistanceFrom(next_from_address, truck.truck_packages)

        #distance/mph
        #time in a usable format

        timeunformatted = round(nextmiles/18, 2)
        minutes = timeunformatted*60
        time_to_add = timedelta(minutes=minutes)
        time_tracker = time_tracker + time_to_add
        #add miles to tracker
        miles_tracker += nextmiles
        #deliver package
        packageDelivered = hashTable.packageHashtable.search(closest_next_package_ID)
        packageDelivered.set_Delivery_Status("DELIVERED", time_tracker)
        hashTable.packageHashtable.insert(closest_next_package_ID, packageDelivered)
        next_from_address = hashTable.packageHashtable.search(closest_next_package_ID).get_Address()
        truck.deliver_package(closest_next_package_ID)
    #update truck mileage
    truck.end_mileage = round(miles_tracker,2)
    truck.end_time = time_tracker

    return round(miles_tracker, 2)


#call truckDeliverPackages() function to initiate deliveries.
truck1_miles = truckDeliverPackages(truck1, start_time)
truck3_miles = truckDeliverPackages(truck3, start_time)
truck2_miles= truckDeliverPackages(truck2, truck3.end_time)

















