from django.contrib.auth.models import User
from core.choices import *
from enchiridions.enc_models import *


class ServiceDetails(models.Model):
    type = models.CharField(choices=SERVICE_TYPE_CHOICE)
    code = models.IntegerField()    # TYPE
    service_name = models.CharField(u'', max_length=100)
    position = models.OneToOneField(PositionModel)



class TreatmentMethod(models.Model):
    la = models.CharField()



