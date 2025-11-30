from django.db import models

class AppUser(models.Model):
    
    tg_id = models.BigIntegerField('User TG_ID', unique=True)
    tg_firstname = models.CharField('User TG_firstname', max_length=255, blank=True, default="")
    tg_lastname = models.CharField('User TG_lastname', max_length=255, blank=True, default="")
    tg_username = models.CharField('User TG_username', max_length=255, unique=True, blank=True, null=True)
    username = models.CharField('Application username', max_length=255, blank=True, default="")
    mgr_lvl = models.IntegerField('User mgr level', default=0)    
    reg_date = models.IntegerField('User registration date (Unixtime)', default=0)
    tg_referer_id = models.BigIntegerField('Referer TG_ID', default=0)
    tg_referer_concatname = models.CharField('Referer telegram concated name (firstname + lastname)', max_length=255, blank=True, default="")
    language = models.CharField('User interface language (tg)', max_length=5, default="en")

    last_activity = models.IntegerField('User last activity (Unixtime)', default=0)    
    instance_id = models.CharField('Instance ID', max_length=255, blank=True, default="")
    sid = models.CharField('Socket SID', max_length=255, blank=True, default="")    
    
    credits = models.BigIntegerField('Coins', default=0)
    tab_updates = models.JSONField('Tab updates', blank=True, default=list)
    active = models.BooleanField(default=True)

    business_id = models.IntegerField('Business ID', default=0)
    business_role = models.IntegerField('Business Role (1 - owner; 2- stuff)', default=0)
    
    contacts_allowed = models.JSONField('Contact list ALLOWED', blank=True, default=list)
    contacts_incoming = models.JSONField('Contact list INCOMING', blank=True, default=list)
    contacts_outcoming = models.JSONField('Contact list OUTCOMING', blank=True, default=list)

    class Meta:
        db_table = 'app_users'

    def __str__(self):
        return str(self.tg_id)