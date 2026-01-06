class Employee:
    counter = 1  # class variable
    hike = 1.05
    def __init__(self,fname,lname,age,pay,hike_needed):
        self.f = fname  #instance variables
        self.l = lname
        self.age = age
        self.pay = pay
        self.hike_needed = hike_needed
    def printDetails(self):
        print(self.f+" "+self.l," ",self.age," ",self.pay)
    def company_provided_hike(self):
        print(int(self.pay)*Employee.hike) #using instance variable
    def Neededhike(self):
        print(int(self.pay)*self.hike_needed) # using class variable
    def __str__(self):
        return (""+self.f+" "+self.l+" "+str(self.age))
e1 = Employee('Madhuri','Maddukuri',20,50000,2)
e2 = Employee('Lakshmi','Maddukuri',22,100000,3)
e1.printDetails()
print(Employee.counter)
print(e1.counter)
print(e2.counter)
print(e1)
print(e1.f)
print(e1.l)
print(e2)
print(e1.__dict__)
print(e1.company_provided_hike())
print(e1.Neededhike())
print(e2.company_provided_hike())
print(e2.Neededhike())
print(e1)

#Inheritance
class Parent:
    hair_color = "black"
class Child(Parent):
    pass

print(Parent.hair_color)
print(Child.hair_color)