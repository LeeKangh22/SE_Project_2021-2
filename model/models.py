from django.db import models


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class MenuTimer(models.Model):
    id = models.IntegerField(primary_key=True)
    menu = models.ForeignKey(Menu, models.DO_NOTHING, blank=True, null=True)
    start_time = models.ForeignKey('OrderTimer', models.DO_NOTHING, db_column='start_time', blank=True, null=True)    
    end_time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_timer'


class MenuToStock(models.Model):
    menu = models.ForeignKey(Menu, models.DO_NOTHING, blank=True, null=True)
    stock = models.ForeignKey('Stock', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_to_stock'


class OrderTimer(models.Model):
    id = models.IntegerField(primary_key=True)
    start_time = models.CharField(unique=True, max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_timer'


class Orders(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    menu = models.ForeignKey(Menu, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    staff_id = models.CharField(max_length=10, blank=True, null=True)
    staff_pw = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    phone_num = models.CharField(max_length=11, blank=True, null=True)
    order = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class Stock(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'


class Tables(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tables'