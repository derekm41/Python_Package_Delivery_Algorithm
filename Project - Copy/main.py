#Derek Mclaws 000769889
import datetime
import package
import truck
import hashTable

## Big-O(N)
def allPackageData(timeofday):
    #format time to use for comparision
    #does not handle standard time vs military datetime. Will not function correctly when input is after 12:59pm standard time
    sep_time = timeofday.split(':')
    check_time = datetime.datetime(year=truck.date.year, month=truck.date.month, day=truck.date.day, hour=int(sep_time[0]), minute=int(sep_time[1]))
    #create a list of packages to use for comparision
    packages = []
    #Big-O(1)
    for packageID in range(1, 41):
        p = hashTable.packageHashtable.search(packageID)
        #print(p)
        packages.append(p)
    #get correct truck for comparision
    print('Package status as of %s' % (check_time.time()))
    # Big-O(N) Grows as packages grows.
    for package in packages:
        whichtruck = package.truckload
        correct_truck = ''
        if whichtruck == 1:
            correct_truck = truck.truck1
        elif whichtruck == 2:
            correct_truck = truck.truck2
        elif whichtruck == 3:
            correct_truck = truck.truck3
    #compare delivery status with truck start time, delivered time, and the given time.

        if package.deliveredAt < check_time:
            print('Package %s status: Delivered at %s' %(package.packageID, package.deliveredAt.time()))
        elif correct_truck.start_time < check_time < package.deliveredAt:
            print('Package %s status: In Route' %(package.packageID))
        elif check_time < correct_truck.start_time:
            print('Package %s status: At the Hub' %(package.packageID))


# Big-O(1)
def truckMileage():
    truck1mileage = truck.truck1.end_mileage
    truck2mileage = truck.truck2.end_mileage
    truck3mileage = truck.truck3.end_mileage
    alltruckmileage = truck1mileage+truck2mileage+truck3mileage
    print('Truck 1 Mileage: %s\n'
          'Truck 2 Mileage: %s\n'
          'Truck 3 Mileage: %s\n'
          'Total Truck Mileage : %s' %(truck1mileage, truck2mileage, truck3mileage, alltruckmileage))
# Big-O(1)
def individualPackage(ID):
    p = hashTable.packageHashtable.search(int(ID))
    p.lookupPrint()

# Big-O(1)
def lookupPackageInfo():
    lookupMenu = input('Select an option.\n'
                       '[1] All packages for a given time.\n'
                       '[2] Individual package for a given time.\n'
                       '[3] Main Menu.\n')
    if lookupMenu == '1':
        time_input = input('Please enter a time as hh:mm\n')
        allPackageData(time_input)
        next = input('Enter another time. hh:mm\n'
                     'Press 1 to return to menu\n')
        if next == '1':
            ui()
        else:
            allPackageData(next)
    elif lookupMenu == '2':
        id = input('Type Package ID: ')
        individualPackage(id)
        next = input('Press 1 to return to menu\n'
                     'Press 0 to exit program.\n')
        if next == '1':
            ui()
    elif lookupMenu == '3':
        ui()


# Big-O(1)
def ui():
    #Main menu
    main_menu = input("Please select an option.\n"
                      "[1] Lookup Truck Total Mileage\n"
                      "[2] Lookup Package Information \n"
                      "[0] Exit Program \n")

    if main_menu == '1':
        truckMileage()
        return_to_menu = input("Press 1 to return to menu or 0 to exit program.")
        if return_to_menu == '1':
            ui()

    elif main_menu == '2':
        lookupPackageInfo()

ui()




