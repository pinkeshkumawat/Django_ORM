from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# user table is already imported from import

class page(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    #user = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    '''
    OneToOneField means only 1 user can create 1 page and 1 page can only be created by 1 user
    CASCADE means if we delete User who created a page then it will delete the page also but,
    if we delete the page created by any user then only page is going to be deleted user will still be in DB
    
    PROTECT means we can't delete the user if he created any page but user will be deleted if he hasn't created the page,
    or the page created by user is deleted
    '''
    page_name = models.CharField(max_length=20)
