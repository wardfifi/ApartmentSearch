#Apartment.py

class Apartment:
    def __init__(self, rent = 0, metersFromUCSB = 0, condition = ""):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition
    
    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}"\
                .format(self.rent, self.metersFromUCSB, self.condition)
    
    def __lt__(self,rhs): 
        conditionList = ["excellent", "average", "bad"]
        if self.rent == rhs.rent:
            if self.metersFromUCSB == rhs.metersFromUCSB:
                return conditionList.index(self.condition) < conditionList.index(rhs.condition)
            else:
                return self.metersFromUCSB < rhs.metersFromUCSB
        else:
            return self.rent < rhs.rent

    def __gt__(self,rhs):
        conditionList = ["excellent", "average", "bad"]
        if self.rent == rhs.rent:
            if self.metersFromUCSB == rhs.metersFromUCSB:
                return conditionList.index(self.condition) > conditionList.index(rhs.condition)
            else:
                return self.metersFromUCSB > rhs.metersFromUCSB
        else:
            return self.rent > rhs.rent
        
    def __eq__(self, rhs):
        conditionList = ["excellent", "average", "bad"]
        if self.rent == rhs.rent and conditionList.index(self.condition) == conditionList.index(rhs.condition):
            return True
        else:
            return False
