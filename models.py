from django.db import models

class FlowObj(models.Model):
    nameLong = models.CharField(max_length=10)
    nameShort = models.CharField(max_length=50)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
class Account(models.Model):
    ACC_TYPES = [
        (0, "Checking"),
        (1, "Savings"),
        (2, "Other"),
    ]
    flowID = models.ForeignKey(FlowObj, on_delete=models.CASCADE)
    typeOf = models.IntegerField(choices=ACC_TYPES)
    
class Debit(models.Model):
    DEBIT_TYPES = [
        (0, "Home"),
        (1, "Auto"),
        (2, "School"),
        (3, "Utility"),
        (4, "Insurance"),
        (5, "Credit Card"),
        (6, "Other"),
    ]
    flowID = models.ForeignKey(FlowObj, on_delete=models.CASCADE)
    accoID = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    typeOf = models.IntegerField(choices=DEBIT_TYPES)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    due = models.DateField()
    
class Credit(models.Model):
    CREDIT_TYPES = [
        (0, "Income"),
        (1, "Bonus"),
        (2, "Other"),
    ]
    flowID = models.ForeignKey(FlowObj, on_delete=models.CASCADE)
    accoID = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    typeOf = models.IntegerField(choices=CREDIT_TYPES)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField()
    
class Frequency(models.Model):
    FREQ_TYPES = [
        (0, "Monthly"),
        (1, "Weekly"),
        (2, "Bi-Monthly"),
        (3, "Bi-weekly"),
        (4, "Other"),
    ]
    flowID = models.ForeignKey(FlowObj, on_delete=models.CASCADE)
    typeOf = models.IntegerField(choices=FREQ_TYPES)
    args = models.CharField(max_length=25)
    