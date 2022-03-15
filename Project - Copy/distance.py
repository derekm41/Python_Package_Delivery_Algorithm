import csv
import hashTable


distanceFilename ='WGUPS_ Distance_Table.csv'
distanceList = []
addressList = []

#Read in addresses and distance data from CSV file.
#Big O(N^2)
def loadDistanceData(filename):

    #I now have two lists: One with address and distance data and another with address data.
    with open(filename) as csvFile:
        #remove the \n newline
        cleaned = (line.replace('\n', ' ') for line in csvFile)
        distanceData = csv.reader(cleaned, delimiter=',')
        next(distanceData)
        for row in distanceData:
            address = row[1]
            if address == " HUB":
                stripped_hub = address.strip()
                addressList.append(stripped_hub)
            else:
                size = len(address)
                mod_address = address[:size - 7].strip()
                addressList.append(mod_address)
            tempList = []
            for j in range(2, 29):
                distance = row[j]
                if distance == ' ':
                    break
                tempList.append(distance)

            distanceList.append(tempList)
    #print(addressList)
#Finds the distance(miles) between two address using the indexes of row and column.
#Big O(1)
def distanceBetween(address1, address2):
    try:
        distance = distanceList[addressList.index(address1)][addressList.index(address2)]
        if distance == '':
            distance = distanceList[addressList.index(address2)][addressList.index(address1)]
    except:
        distance = distanceList[addressList.index(address2)][addressList.index(address1)]

    return distance
#Finds the smallest distance from a address.
#Big O(N)
def minDistanceFrom(fromAddress, truckPackages):
    min_distance_package = 100
    min_distance_package_id = 0
    min_package_address = ''
    package_info = ''


    for packageID in truckPackages:
        #get the package address from package ID
        #print(packageID)
        pack = hashTable.packageHashtable.search(packageID)
        package_address = pack.get_Address()
        #print(package_address)

        #Find min distance to next package.
        package_distance = float(distanceBetween(fromAddress, package_address))
        #print(package_distance)
        #compare to find the smallest
        if package_distance < min_distance_package:
            #miles
            min_distance_package = package_distance
            #package ID
            min_distance_package_id = packageID
            #package address
            min_package_address = package_address
            #package object
            package_info = pack


    # return package ID and minimum distance
    return min_distance_package_id, min_distance_package

   #loop through addresses and distance to find smallest distance to fromAddress
loadDistanceData(distanceFilename)




