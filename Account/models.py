from django.db import models


class Right(models.Model):
    authName = models.CharField(max_length=100)
    level = models.CharField(max_length=10)
    pid = models.IntegerField()
    path = models.CharField(max_length=100)
    children = models.ManyToManyField('self')


class Role(models.Model):
    roleName = models.CharField(max_length=100)
    roleDesc = models.CharField(max_length=100)
    children = models.ManyToManyField(Right)


class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)
    mobile = models.CharField(max_length=11)
    email = models.CharField(max_length=200)
    role_name = models.ForeignKey(Role, related_name='role_name', blank=True, null=True, on_delete=models.CASCADE)
    mg_state = models.BooleanField(default=True)
    type = models.CharField(max_length=200, default='custom')

    class Meta:
        db_table = 'user'


class Menu(models.Model):
    authName = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    children = models.ManyToManyField('self', blank=True)


class Category(models.Model):
    type_choices = (
        ('0', ''),
        ('1', '第一层分类'),
        ('2', '第二层分类'),
        ('3', '第三层分类')
    )
    level = models.CharField(choices=type_choices, default='0', max_length=12)
    name = models.CharField(max_length=100)
    children = models.ManyToManyField('self', blank=True)
    deleted = models.BooleanField(default=False)

