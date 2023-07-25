from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True, editable=False)
    user_name = models.CharField(max_length=20, null=False)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=20)
    age = models.IntegerField()

    def _str_(self):
        return "%s %s %s %s %s" % (self.user_id, self.user_name, self.phone_number, self.city, self.age)


class Order(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    created_date = models.DateField()
    updated_date = models.DateField()

    def __str__(self):
        return "%s %s %s %s %s" % (self.order_id, self.user_id, self.status, self.created_date, self.updated_date)


class OrderItem(models.Model):
    orderItem_id = models.AutoField(primary_key=True, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return "%s %s %s %s %s" % (self.orderItem_id, self.order_id, self.item_name, self.quantity, self.price)
