from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.deletion import CASCADE

# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    address = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user.username




class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=15, null=True)
    description = models.TextField(max_length=255, blank=True)
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    ratting = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=15, null=True)
    facebook_page = models.CharField(max_length=50, null=True) 
    status = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    cat_name = models.CharField(max_length=50, null=True, default='Cat')

    def __str__(self):
        return self.cat_name


class Post(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    image = models.FileField()
    location = models.CharField(max_length=100, null=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=50, null=True)
    prev_price = models.DecimalField(max_digits=8, decimal_places=2)
    new_price = models.DecimalField(max_digits=8, decimal_places=2)
    creation_date = models.DateField()

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    title = models.CharField(max_length=150, null=True)
    ordered_date = models.DateField(default=timezone.now)
    total_sub_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.title

class Order(models.Model):
    ORDER_STATUS = (
        ('Cancelled', 'Cancelled'),
        ('Pending', 'Pending'),
        ('Packed', 'Packed'),
        ('On The Way', 'On The Way'),
        ('Delivered', 'Delivered')
    )

    DELIVERY_TYPE = {
        ('payment1', 'payment1'),
        ('payment2', 'payment2'),
        ('payment3', 'payment3'),
    }

    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    phone_no = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_sub_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    delivery_type = models.CharField(max_length=20, choices=DELIVERY_TYPE, default='payment3')
    ordered_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Pending')
    delivery_date = models.DateField(default=timezone.now)
    transaction_id = models.CharField(max_length=50, null=True)
    rand_order_id = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.first_name + " " + self.last_name



class Foundation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=15, null=True)
    description = models.TextField(max_length=255, blank=True)
    address = models.CharField(max_length=100)
    image = models.FileField(null=True)
    code_no = models.CharField(max_length=15, null=True)
    Doe=models.CharField(max_length=15, null=True)
    type = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.user.username



class Foundation_Post(models.Model):
    foundation = models.ForeignKey(Foundation, on_delete=models.CASCADE)
    title=models.TextField(max_length=100)
    description = models.TextField(max_length=255)
    items=models.TextField(max_length=100)
    quantity=models.TextField(max_length=100)
    contact=models.TextField(max_length=100)
    area=models.TextField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    creation_date = models.DateField()
    status = models.CharField(max_length=20, null=True)
    contact_no = models.CharField(max_length=15, null=True)
    fname=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title



class CustomerPost(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.TextField(max_length=100)
    description = models.TextField(max_length=255, null=True)
    quantity=models.TextField(max_length=100, null=True)
    area=models.TextField(max_length=100, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    creation_date = models.DateField()
    status = models.CharField(max_length=20, null=True)
    contact = models.CharField(max_length=15, null=True)
    image = models.FileField()
    foundation = models.ForeignKey(Foundation, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title



class Delivery_Man(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    ratting = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    type = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
