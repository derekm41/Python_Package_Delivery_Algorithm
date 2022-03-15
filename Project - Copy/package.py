
#package class

class Package:
    def __init__(self, ID, paddress, pcity, pstate, pzip, pdeliveryDeadline, pmassKilo, pspecialNotes, pdeliveryStatus):
        self.packageID = ID
        self.address = paddress
        self.city = pcity
        self. state = pstate
        self.zip = pzip
        self.deliveryDeadline = pdeliveryDeadline
        self.massKilo = pmassKilo
        self.specialNotes = pspecialNotes
        self.deliveryStatus = pdeliveryStatus
        self.deliveredAt = None
        self.truckload = 0
    #string version of attributes
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.packageID, self.address, self.city, self.state, self.zip, self.deliveryDeadline, self.massKilo, self.specialNotes, self.deliveryStatus, self.deliveredAt)
    #Prints information associtated with package parameter
    #Big O(1)
    def lookupPrint(self):
        print('Package ID: %s\n'
              'Street Address: %s\n'
              'City: %s\n'
              'State: %s\n'
              'Zip: %s\n'
              'Delivery Deadline: %s\n'
              'Kilo: %s\n'
              'Special Notes: %s\n'
              'Delivery Status: %s\n'
              'Delivery Time: %s\n' %(self.packageID, self.address, self.city, self.state, self.zip, self.deliveryDeadline, self.massKilo, self.specialNotes, self.deliveryStatus, self.deliveredAt))
    #Returns address
    # Big O(1)
    def get_Address(self):
        return self.address
    #Returns delivery status
    # Big O(1)
    def get_Delivery_Status(self):
        return self.deliveryStatus
    #Sets delivery status and delivery time
    # Big O(1)
    def set_Delivery_Status(self, status, time):
        self.deliveryStatus = status
        self.deliveredAt = time
        return


