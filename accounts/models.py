#models
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    class Meta:
        db_table = "employee"

class Customer(models.Model):
    PAYMENTSTATUS = (
        ('Cleared', 'Cleared'),
    )

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    invoice_number = models.IntegerField(null=True)
    payment_status = models.CharField(max_length=200, null=True, choices=PAYMENTSTATUS)
    image = models.ImageField(upload_to='allcustomer/', null=True, blank=True)



    def __str__(self):
        return self.name



class Tag(models.Model):
        name = models.CharField(max_length=200, null=True)

        def __str__(self):
            return self.name

class ProductForCustomer(models.Model):
        CATEGORY2 = (
                ('Dine in', 'Dine in'),
                ('Take out', 'Take out'),

         )

        name = models.CharField(max_length=200, null=True)
        price = models.FloatField(null=True)
        category = models.CharField(max_length=200, null=True, choices=CATEGORY2)
        description = models.CharField(max_length=200, null=True, blank=True)
        date_created = models.DateTimeField(auto_now_add=True, null=True)
        tags = models.ManyToManyField(Tag)
        image = models.ImageField(upload_to='products/', null=True, blank=True)

        def __str__(self):
                return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
    )
    DELIVEREDSTATUS = (
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(ProductForCustomer, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, blank=True)
    delivered_status = models.CharField(max_length=200, null=True, choices=DELIVEREDSTATUS, blank=True)

    def __str__(self):
        return self.product.name

