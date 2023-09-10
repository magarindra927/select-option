from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return self.name
    
class Hobby(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return self.f_name   
    

class Play(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)  
    password=models.CharField(max_length=50) 
    address=models.CharField(max_length=50) 
    contact=models.IntegerField()
    profile_picture=models.ImageField(upload_to='images', blank='True')
    citizenship=models.IntegerField()
    age=models.IntegerField()    
    gender=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    occupation=models.CharField(max_length=50)
    about_you=models.TextField()
    

    def __str__(self):
        return self.name    
    
class Cartoon(models.Model):
    name=models.CharField(max_length=50)  
    dob=models.DateField(auto_now=True)      
    f_name=models.CharField(max_length=50)  
    m_name=models.CharField(max_length=50) 
    birth_place=models.CharField(max_length=50)   
    p_address=models.CharField(max_length=50)    
    telephone=models.IntegerField()  
    mobile=models.IntegerField()  
    email=models.EmailField()
    gender=models.CharField(max_length=50)     
    martial_status=models.CharField(max_length=50)  
    nationality=models.CharField(max_length=50)  
    religion=models.CharField(max_length=50)  

    def __str__(self):
        return self.name
    