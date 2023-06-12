from django.db import models
from django.core.validators import EmailValidator
from django.db.models import UniqueConstraint

# Create your models here.


class BaseUser(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    date_of_birth = models.DateField()


    class Meta:
        abstract = True


class Buyer(BaseUser):
    buyer_id = models.AutoField(primary_key=True)
    

    def __str__(self):
        return str(self.name)

class Seller(BaseUser):
    seller_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    establishment_year = models.DateField()
    address_proof = models.ImageField(upload_to='seller/address_proof') # TODO: blob type
    bank_account_no = models.CharField(max_length=100)
    bank_ifsc_code = models.CharField(max_length=100)
    highest_qualification = models.CharField(max_length=100, null=True)
    
    document_personal = models.ImageField(upload_to='seller/document_personal') # TODO: blob type
    document_business_license = models.ImageField(upload_to='seller/document_business_license') # TODO: blob type
    document_passbook = models.ImageField(upload_to='seller/document_passbook') # TODO: blob type
    

    def __str__(self):
        return str(self.name)
    
class Transporter(BaseUser):
    transport_manager_id = models.AutoField(primary_key=True)
    poc_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_address = models.TextField()
    hub_address = models.TextField()
    gstin = models.CharField(max_length=100)
    cin = models.CharField(max_length=100)
    company_vehicles = models.IntegerField()
    company_drivers = models.IntegerField()
    company_labors = models.IntegerField()
    license = models.ImageField(upload_to='transporter/license') # TODO: blob type
    bank_account_no = models.CharField(max_length=100)
    bank_ifsc_code = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)
    
class Item(models.Model):
    item_id = models.AutoField(primary_key=True) # TODO: format
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    harvest_date = models.DateField()
    bag_type = models.CharField(max_length=10)
    total_stock = models.IntegerField()
    minimum_order = models.IntegerField()
    price_per_kg = models.FloatField()
    publish_date = models.DateField()
    pickup_address = models.TextField()

    
    
class Order(models.Model):
    
    PAYMENT_STATUS_CHOICES = [
        ('Initiated', 'Initiated'),
        ('Completed', 'Completed'),
        ('Waiting for Seller', 'Waiting for Seller'),
        #('Refunded', 'Refunded'),
    ]
    
    order_id = models.AutoField(primary_key=True)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE) # TODO: CASCADE or not
    transport_manager_id = models.ForeignKey(Transporter, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS_CHOICES, default='Initiated')
    
    
    """def initiate_payment(self):
        # Set payment_status as 'Initiated'
        self.payment_status = 'Initiated'
        self.save()

    def complete_payment(self):
        # Set payment_status as 'Waiting for Seller'
        self.payment_status = 'Waiting for Seller'
        self.save()

    def accept_order(self):
        # Set payment_status as 'Completed'
        self.payment_status = 'Completed'
        self.save()"""

class RefundOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)
    
class PickupAddress(models.Model):
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    address = models.TextField()
    
class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    transport_manager_id = models.ForeignKey(Transporter, on_delete=models.CASCADE)
    stock = models.IntegerField()
    
    class Meta:
        constraints = [UniqueConstraint(fields=['category', 'transport_manager_id'], name='unique_vehicle')]