from django.db import models

# Create your models here.


# Company Details
class CompanyDetails(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length =50)
    city = models.CharField(max_length = 20)
    dlno = models.CharField(max_length =20)
    gst = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    phoneno = models.CharField(max_length = 13)
    
    
# Manufacturers
class Manufacturers(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=10, default=name)
    
    def __str__(self):
        return self.alias
    
#Products
class Products(models.Model):
    name = models.CharField(max_length=30)
    volume = models.CharField(max_length=10)
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} {self.volume} {self.manufacturer}'
    class Meta:
        ordering = ['name']
    
    
class Stock(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    batch = models.CharField(max_length=20)
    expiry = models.DateField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return f'Name: {self.product.name}, Expiry: {self.expiry}, Qty_Avl: {self.quantity}'
    
    class Meta:
        ordering = ['-expiry','product']

    
class Party(models.Model):
    name = models.CharField(max_length=30)
    addressLine_1 = models.TextField(max_length=50)
    addressLine_2 = models.TextField(max_length=50, null=True, blank=True)
    addressLine_3 = models.TextField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    gstid = models.CharField(max_length=20)
    dlno = models.CharField(max_length=40)
    mbno = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.name
    

class Invoice(models.Model):
    invoicenumber = models.CharField(max_length=10)
    date = models.DateField()
    costumer = models.ForeignKey(Party, on_delete=models.CASCADE)
    gstrate = models.IntegerField(default=0)
    typeofinv = models.BooleanField(default=False)
    
    def __str__(self):
        return self.invoicenumber
    
    
class Entry(models.Model):
    inv = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Stock, on_delete=models.CASCADE)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    ptr = models.DecimalField(max_digits=10, decimal_places=2)
    pts = models.DecimalField(default=None, null=True, blank=True,max_digits=10, decimal_places=2)
    qty = models.IntegerField()
    bonus = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Invoice: {self.inv}'
    

class SaveEntries(models.Model):
    invoiceno = models.IntegerField()
    sno = models.IntegerField()
    description = models.CharField(max_length=20)
    pack = models.CharField(max_length=10,default=0)
    mfg = models.CharField(max_length=20)
    batchNo = models.CharField(max_length=10)
    expiry = models.CharField(max_length=15)
    mrp = models.CharField(max_length=8)
    ptr = models.CharField(max_length=8)
    pts = models.CharField(max_length=8,default=None)
    qty = models.IntegerField()
    bonus = models.IntegerField()
    amount = models.CharField(max_length=10)
    
    def __str__(self):
        return f'Saved Entry Invoice No: {self.invoiceno}'
    
    class Meta:
        ordering = ['sno']
    
    
class SavedInvoice(models.Model):
    invoicenumber = models.IntegerField()
    name = models.CharField(max_length=20)
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20, null=True, blank=True)
    address3 = models.CharField(max_length=20, null=True, blank=True)
    mbno=models.CharField(max_length=20,default='')
    city = models.CharField(max_length=20)
    date = models.DateField(null=True, blank=True)
    gstid = models.CharField(max_length=20)
    dlno = models.CharField(max_length=20)
    gst = models.IntegerField()
    paid = models.BooleanField(default=False)
    rate = models.BooleanField(default=False)
    def __str__(self):
        return f'Saved Invoice No: {self.invoicenumber}, Rate:{self.rate}'
    
    
    
class RateEntry(models.Model):
    inv = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Stock, on_delete=models.CASCADE)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField()
    
    def __str__(self):
        return f'Rate Invoice, No: {self.inv.invoicenumber}'
    
    
    
    
class SaveRateEntries(models.Model):
    invoiceno = models.IntegerField()
    sno = models.IntegerField()
    description = models.CharField(max_length=20)
    pack = models.CharField(max_length=10,default=0)
    mfg = models.CharField(max_length=20)
    batchNo = models.CharField(max_length=10)
    expiry = models.CharField(max_length=15)
    mrp = models.CharField(max_length=8)
    rate = models.CharField(max_length=8,default=None)
    qty = models.IntegerField()
    amount = models.CharField(max_length=10)
    
    def __str__(self):
        return f'Saved Entry Invoice No: {self.invoiceno}'
    
    class Meta:
        ordering = ['sno']
    