import csv
import package
# HashTable Class using chaining.
packageFilename = 'C:/Users/derek/Dropbox/c950/C950/Project/WGUPS_Package_File.csv'


class ChainingHashTable:
    # Constructor
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #update key if it is already in the bucket
        for key_v in bucket_list:
            if key_v[0] == key:
                key_v[1] = item
                return True
        #if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_v in bucket_list:
            # print (key_value)
            if key_v[0] == key:
                return key_v[1]  # value
        return None

    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for key_v in bucket_list:
            # print (key_value)
            if key_v[0] == key:
                bucket_list.remove([key_v[0], key_v[1]])
#Reads package data, creates a package object and then inserts into package hashtable data structure
#Big O(N)
def loadPackageData(filename):
    with open(filename) as csvFile:
        packageData = csv.reader(csvFile, delimiter=',')
        # skip header
        next(packageData)

        # for row in packageData:
        # print(row)
        packageHash = ChainingHashTable()
        for row in packageData:
            packageID = int(row[0])
            # print(packageID)
            address = row[1]
            # print(address)
            city = row[2]
            state = row[3]
            zip = row[4]
            deliveryDeadline = row[5]
            massKilo = row[6]
            specialNotes = row[7]
            deliveryStatus = 'AT_THE_HUB'

            p = package.Package(packageID, address, city, state, zip, deliveryDeadline, massKilo, specialNotes, deliveryStatus)

            packageHash.insert(packageID, p)
    return packageHash


#Package Hashtable
packageHashtable = loadPackageData(packageFilename)