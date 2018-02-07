# HW3 problem 1
# Sean Maroongroge


class Patient:
    """master class"""
    def __init__(self, name):
        self.name = name
    def discharge(self, name):
        pass


class EmergencyPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
    def discharge (self):
        """this just prints the text"""
        print("Discharged " + self.name + ", an " + self.__class__.__name__)


class HospitalizedPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
    def discharge (self):
        """this just prints the text"""
        print("Discharged " + self.name + ", a " + self.__class__.__name__)




class Hospital:
    def __init__(self, patients, cost):
        self.patients = patients   #patients is a running patient list in hospital
        self.cost = cost

    def admit(self, patients):
        self.patients.append(patients)


    def discharge_all(self):
        for thisPatient in self.patients:
            if isinstance(thisPatient, EmergencyPatient):  #why cant i use "type"?
                self.cost += 1000
            elif isinstance(thisPatient, HospitalizedPatient):
                self.cost += 2000
            thisPatient.discharge()
            # self.patients.remove(thisPatient) # if you put this here, it skips every other one
        self.patients = []

    def get_total_cost(self):
        return self.cost

#why are all my patient types considered instances?
#for thisPatient in myHospital.patients:
 # print(thisPatient, type(thisPatient))   #all are type instance

#for i in range(len(myHospital.patients)):
 #   print(myHospital.patients[i], type(myHospital.patients[i]))

 # print(type(Patient1))

#alternate code for discharge all...not as elegant
#   def discharge_all(self):
#       for i in range(len(self.patients)):
#           print(self.patients[0].name)
#           if isinstance(self.patients[0], EmergencyPatient):
#               self.cost += 1000
#           elif isinstance(self.patients[0], HospitalizedPatient):
#               self.cost += 2000
#           self.patients[0].discharge()
#           self.patients.remove(self.patients[0])






#Test: create the patients we will use for the test
Patient1 = EmergencyPatient("Albert")
Patient2 = EmergencyPatient("Bob")
Patient3 = HospitalizedPatient("Candy")
Patient4 = HospitalizedPatient("Dylan")
Patient5 = HospitalizedPatient("Ethel")



# Test: creating a hospital and filling it with patients
myHospital = Hospital([], 0)

myHospital.admit(Patient1)
myHospital.admit(Patient2)
myHospital.admit(Patient3)
myHospital.admit(Patient4)
myHospital.admit(Patient5)


#why can't I use print(myHospital.patients.name)? it is a list, so cant use .name modifier
#print(myHospital.patients)

myHospital.discharge_all()
print("The total cost is ", myHospital.get_total_cost())
