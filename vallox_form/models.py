from django.db import models


class Customer(models.Model):
    customer_name = models.CharField('First name', max_length=100)
    customer_surname = models.CharField('Second name', max_length=100)
    customer_phone = models.IntegerField(null=True, blank=True)
    customer_email = models.EmailField('E-mail')
    
    OBJECT_TYPE = (
        ('cottege', 'Cottage'), 
        ('apartment', 'Apartment'),
    )     
    
    category = models.CharField(choices=OBJECT_TYPE, max_length=15)
    body = models.TextField('Customer whishes')
    

    def __str__(self):
        return self.customer_surname

    
    def get_absolute_url(self):
        return f'/task/{self.id}'  
