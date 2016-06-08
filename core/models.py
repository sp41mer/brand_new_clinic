from django.contrib.auth.models import User
from django.db import models

from core.choices import *
from enchiridions.enc_models import *


class TreatmentMethod(models.Model):
    la = models.CharField()

class ServiceDetails(models.Model):
    la = models.CharField



