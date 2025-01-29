from django.db import models

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length=30, blank=False, default='user')
  password = models.CharField(max_length=30, blank=False)
  first_name = models.CharField(max_length=50, blank=False)
  last_name = models.CharField(max_length=50, blank=False)
  phone_number = models.IntegerField(blank=False)
  created_at = models.DateTimeField(auto_now=True)
  modified_at = models.DateTimeField(auto_now_add=True)

  owner = models.ForeignKey('auth.User', related_name='users', on_delete=models.CASCADE)

class UserAddress(models.Model):
  user_id = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=False,
    blank=False
  )
  address_line1 = models.CharField(max_length=50)
  address_line2 = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  postal_code = models.CharField(max_length=10)
  country = models.CharField(max_length=50)
  mobile_number = models.CharField(max_length=15)

class UserPayment(models.Model):
  user_id = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=False,
    blank=False
  )

  PAYMENT_TYPES = {
    'CR': 'Credit',
    'DB': 'Debit',
    'DG': 'Digital'
  }
  
  payment_type = models.CharField(
    max_length=2,
    choices=PAYMENT_TYPES,
  )

  PROVIDER_LIST = {
    'PPL': 'PayPal',
    'BDO': 'BDO',
    'GCH': 'GCash',
    'MTC': 'MasterCard'
  }
  
  provider = models.CharField(
    max_length=3,
    choices=PROVIDER_LIST,
  )

  account_no = models.CharField(max_length=50)