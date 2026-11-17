from django.db import models
class Employee(models.Model):
    GENDER_OPTIONS = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    employee_fname = models.CharField(max_length=50, verbose_name="First name")
    employee_lname = models.CharField(max_length=50, verbose_name="Last name")
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)
    phone = models.CharField(max_length=20)
    hire_date = models.DateField()
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)




class Store(models.Model):
    store_name = models.CharField(max_length=50, verbose_name="Store name")
    store_location = models.CharField(max_length=100, null=True, default="N/A")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

   

class Asset(models.Model):
    asset_name = models.CharField(max_length=50, verbose_name="Asset name")
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    stock_quantity = models.IntegerField(default=0)
    re_order_level = models.IntegerField(default=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE , null=True, blank=True)



class Stock(models.Model):
    stock_date = models.DateField()
    supplier = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    received_by = models.CharField(max_length=50)

    


class StockItem(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    





class Requisition(models.Model):
    STATE_OPTIONS = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Issued", "Issued"),
    ]
    requisition_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    requisition_state = models.CharField(max_length=20, choices=STATE_OPTIONS, default="Pending")
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    

class RequisitionItem(models.Model):
    STATUS_OPTIONS = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Issued", "Issued"),
    ]
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default="Pending")



# Create your models here.
