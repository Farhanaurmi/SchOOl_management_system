class salary():
    def salary(self,rank):
        self.rank=rank
        self.salary=self.rank*2000
        return self.salary    
    
class student():
    def __init__(self, name, age, id):
        self.name=name
        self.age=age
        self.id=id
    def waver(self,cgpa):
        self.cgpa=cgpa
        self.wav=self.cgpa*45
        return self.wav
    
class teacher(salary):
    def __init__(self, name, age, id):
        self.name=name
        self.age=age
        self.id=id

class office(salary):
    def __init__(self, name, age, id):
        self.name=name
        self.age=age
        self.id=id
    


class user(student, teacher, office):
    def __init__(self,name,age,id):
        if id==1:
            student.__init__(self, name, age, id)
        if id==2:
            teacher.__init__(self, name, age, id)
        if id==3:
            office.__init__(self, name, age, id)
            
person1=user('muju',19,1)
n=person1.waver(3.99)

person2=user('tanmoy',23,2)
i=person2.salary(3)
person3=user('urmi',22,3)
j=person3.salary(4)
print(f'||Name||  {person1.name}\n||Age||  {person1.age}\n||ID||  {person1.id}\n||Waver||  {person1.wav}\n')
print(f'||Name||  {person2.name}\n||Age||  {person2.age}\n||ID||  {person2.id}\n||Salary||  {person2.salary}\n')
print(f'||Name||  {person3.name}\n||Age||  {person3.age}\n||ID||  {person3.id}\n||Salary||  {person3.salary}\n')