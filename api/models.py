from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'SYS_USER'
        
    username = models.CharField(max_length=50, null=False, unique=False)
    password = models.CharField(max_length=50, null=False, unique=False)
    group = models.CharField(max_length=50, null=True)
    permission = models.CharField(max_length=50, null=True)

    
class UserInfo(models.Model):
    class Meta:
        db_table = 'SYS_USER_INFO'

    user = models.OneToOneField(to='User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    age = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=50, null=True)
    id_card = models.CharField(max_length=50, null=True)
    create_time = models.CharField(max_length=50, null=True)
    update_time = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=50, null=True)

class Token(models.Model):
    class Meta:
        db_table = 'SYS_TOKEN'

    user = models.OneToOneField(to='User', on_delete=models.CASCADE)
    time = models.CharField(max_length=50, null=True)
    token = models.CharField(max_length=50, null=True)