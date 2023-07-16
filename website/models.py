from django.db import models
          
# Create your models here.
# database models do not depends upon which database you are using which database you are using
# it will create it for you
# after creating this u have to migrate it to your database
# which can be done using terminal window 
# step 1 makemigrations
#step 2 migrate

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address =  models.CharField(max_length=100)
    city =  models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    zipcode =  models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

	