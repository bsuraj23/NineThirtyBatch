class sample():
      a=10        #static variable
      b=20        #static variable
      def __init__(self):
            c=30         #instance variable
      def display(self):
            d=40          #instance variable
            return self.a+self.b+d
obj=sample()
print(sample.a)
print(sample.b)
sample.a=100
print(sample.a)
print(obj.display())







class student():
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
obj=student()
obj.name="keerthana"
obj.age=20      
obj.rollno=101
print(obj.name,obj.age,obj.rollno)

obj.name="sowmya"
obj.age=21  
obj.rollno=102
print(obj.name,obj.age,obj.rollno)
 a