class employe:
 def __init__(self, name,age):
  self.name = name
  self.age =age

 def details(self):
  print("the name is ",self.name)
  print("the age is ",self.age)
   
class developer(employe):
 degree = ""
 
 def showmoredetails(self):
  
  print("the degree is ",self.degree)

  
e1 = employe("waleed iqbal",23)
e1.details()

e2 = developer("saad ullah",23)
e2.degree = "computer science"
e2.details()
e2.showmoredetails() 


     
  
