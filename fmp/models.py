from django.db import models
from django.db import connection

class Evseason(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    seasonname = models.CharField(db_column='SeasonName', max_length=255)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVSeason'