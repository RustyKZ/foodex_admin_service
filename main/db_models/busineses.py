from django.db import models

class Supplier(models.Model):
    
    owner_tg_id = models.BigIntegerField('User TG_ID', default=0)
    name = models.CharField('Business name', max_length=255, blank=True, default="")
    description = models.CharField('Business description', max_length=255, blank=True, default="")
    avatar_name = models.CharField('Avatar path', max_length=255, blank=True, default="")
    reg_date = models.IntegerField('Business registration date (Unixtime)', default=0)

    tg_referals = models.JSONField('Referals list', blank=True, default=list)

    staff = models.JSONField('Staff TG IDs', blank=True, default=list)
    active_orders = models.JSONField('Active orders IDs', blank=True, default=list)
    closed_orders = models.JSONField('Closed orders IDs', blank=True, default=list)

    contacts_allowed = models.JSONField('Contact list ALLOWED', blank=True, default=list)
    contacts_incoming = models.JSONField('Contact list INCOMING', blank=True, default=list)
    contacts_outcoming = models.JSONField('Contact list OUTCOMING', blank=True, default=list)

    tariff = models.IntegerField('Tariff type', default=0)
    end_tariff_date = models.IntegerField('End tariff date (Unixtime)', default=0)

    language = models.CharField('User interface language (tg)', max_length=5, default="en")

    class Meta:
        db_table = 'suppliers'

    def __str__(self):
        return str(self.id)


class SupplierTranslation(models.Model):
    supplier_id = models.IntegerField('Supplier ID', default=0)
    language = models.CharField('User interface language (tg)', max_length=5, default="en")
    
    name = models.CharField('Business name', max_length=255, blank=True, default="")
    description = models.CharField('Business description', max_length=255, blank=True, default="")    
    
    class Meta:
        db_table = 'suppliers_translation'

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    
    owner_tg_id = models.BigIntegerField('User TG_ID', default=0)
    name = models.CharField('Business name', max_length=255, blank=True, default="")
    description = models.CharField('Business description', max_length=255, blank=True, default="")
    avatar_name = models.CharField('Avatar path', max_length=255, blank=True, default="")
    reg_date = models.IntegerField('Business registration date (Unixtime)', default=0)    

    tg_referals = models.JSONField('Referals list', blank=True, default=list)

    staff = models.JSONField('Staff TG IDs', blank=True, default=list)
    active_orders = models.JSONField('Active orders IDs', blank=True, default=list)
    closed_orders = models.JSONField('Closed orders IDs', blank=True, default=list)

    contacts_allowed = models.JSONField('Contact list ALLOWED', blank=True, default=list)
    contacts_incoming = models.JSONField('Contact list INCOMING', blank=True, default=list)
    contacts_outcoming = models.JSONField('Contact list OUTCOMING', blank=True, default=list)
    
    tariff = models.IntegerField('Tariff type', default=0)
    end_tariff_date = models.IntegerField('End tariff date (Unixtime)', default=0)

    language = models.CharField('User interface language (tg)', max_length=5, default="en")

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return str(self.id)
    

class CustomerTranslation(models.Model):
    customer_id = models.IntegerField('Supplier ID', default=0)
    language = models.CharField('User interface language (tg)', max_length=5, default="en")
    
    name = models.CharField('Business name', max_length=255, blank=True, default="")
    description = models.CharField('Business description', max_length=255, blank=True, default="")    
    
    class Meta:
        db_table = 'customer_translation'

    def __str__(self):
        return str(self.id)