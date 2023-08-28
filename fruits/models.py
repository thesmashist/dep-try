# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Fruitdata(models.Model):
    fruitkey = models.AutoField(db_column='FruitKey', primary_key=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='Timestamp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fishname = models.CharField(db_column='FishName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f1_id = models.IntegerField(db_column='F1_ID', blank=True, null=True)  # Field name made lowercase.
    f2_id = models.IntegerField(db_column='F2_ID', blank=True, null=True)  # Field name made lowercase.
    f1_points = models.FloatField(db_column='F1_Points', blank=True, null=True)  # Field name made lowercase.
    f2_points = models.FloatField(db_column='F2_Points', blank=True, null=True)  # Field name made lowercase.
    f_time = models.DateTimeField(db_column='F_TIME', blank=True, null=True)  # Field name made lowercase.
    attendee_1_id = models.IntegerField(db_column='Attendee_1_ID', blank=True, null=True)  # Field name made lowercase.
    attendee_2_id = models.IntegerField(db_column='Attendee_2_ID', blank=True, null=True)  # Field name made lowercase.
    a1_points = models.FloatField(db_column='A1_Points', blank=True, null=True)  # Field name made lowercase.
    a2_points = models.FloatField(db_column='A2_Points', blank=True, null=True)  # Field name made lowercase.
    m_time = models.DateTimeField(db_column='M_TIME', blank=True, null=True)  # Field name made lowercase.
    pp1_id = models.IntegerField(db_column='PP1_ID', blank=True, null=True)  # Field name made lowercase.
    pp2_id = models.IntegerField(db_column='PP2_ID', blank=True, null=True)  # Field name made lowercase.
    pp1_points = models.FloatField(db_column='PP1_Points', blank=True, null=True)  # Field name made lowercase.
    pp2_points = models.FloatField(db_column='PP2_Points', blank=True, null=True)  # Field name made lowercase.
    pp_time = models.DateTimeField(db_column='PP_TIME', blank=True, null=True)  # Field name made lowercase.
    l1_id = models.IntegerField(db_column='L1_ID', blank=True, null=True)  # Field name made lowercase.
    l2_id = models.IntegerField(db_column='L2_ID', blank=True, null=True)  # Field name made lowercase.
    l1_points = models.FloatField(db_column='L1_Points', blank=True, null=True)  # Field name made lowercase.
    l2_points = models.FloatField(db_column='L2_Points', blank=True, null=True)  # Field name made lowercase.
    p_time = models.DateTimeField(db_column='P_TIME', blank=True, null=True)  # Field name made lowercase.
    fishuser = models.TextField(db_column='FishUser', blank=True, null=True)  # Field name made lowercase.
    fishphone = models.BigIntegerField(db_column='FishPhone', blank=True, null=True)  # Field name made lowercase.
    church = models.TextField(db_column='Church', blank=True, null=True)  # Field name made lowercase.
    fishing_zone = models.TextField(db_column='Fishing_Zone', blank=True, null=True)  # Field name made lowercase.
    visa = models.TextField(db_column='Visa', blank=True, null=True)  # Field name made lowercase.
    ev_concept = models.TextField(db_column='EV_Concept', blank=True, null=True)  # Field name made lowercase.
    evplatform = models.TextField(db_column='EVPlatform', blank=True, null=True)  # Field name made lowercase.
    evonlineoffline = models.TextField(db_column='EVOnlineOffline', blank=True, null=True)  # Field name made lowercase.
    birthday = models.CharField(db_column='Birthday', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    environment = models.TextField(db_column='Environment', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    stage_f = models.CharField(db_column='Stage_F', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage_m = models.CharField(db_column='Stage_M', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage_p = models.CharField(db_column='Stage_P', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bbt_id = models.IntegerField(db_column='BBT_ID', blank=True, null=True)  # Field name made lowercase.
    pls = models.CharField(db_column='PLS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    clad = models.CharField(db_column='CLAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage_pp = models.CharField(db_column='Stage_PP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stage = models.CharField(db_column='Stage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fruitstatus = models.CharField(db_column='FruitStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    holidayplan = models.TextField(db_column='HolidayPlan', blank=True, null=True)  # Field name made lowercase.
    denomination = models.TextField(db_column='Denomination', blank=True, null=True)  # Field name made lowercase.
    nationality = models.TextField(db_column='Nationality', blank=True, null=True)  # Field name made lowercase.
    residence = models.TextField(db_column='Residence', blank=True, null=True)  # Field name made lowercase.
    visanotes = models.TextField(db_column='VisaNotes', blank=True, null=True)  # Field name made lowercase.
    holidaynotes = models.TextField(db_column='HolidayNotes', blank=True, null=True)  # Field name made lowercase.
    locked = models.CharField(db_column='Locked', max_length=50, blank=True, null=True)  # Field name made lowercase.
    proceedable = models.CharField(db_column='Proceedable', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unlockdate = models.DateTimeField(db_column='UnlockDate', blank=True, null=True)  # Field name made lowercase.
    unlockable = models.CharField(db_column='Unlockable', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mine = models.CharField(db_column='Mine', max_length=50, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    social_ig = models.CharField(db_column='Social_IG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    social_fb = models.CharField(db_column='Social_FB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    randid = models.IntegerField(db_column='RandID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FruitData'