# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bbdata(models.Model):
    bbid = models.AutoField(db_column='BBID', primary_key=True)  # Field name made lowercase.
    fruitkey = models.IntegerField(db_column='FruitKey', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    fruitname = models.CharField(db_column='FruitName', max_length=50)  # Field name made lowercase.
    l1_id = models.IntegerField(db_column='L1_ID')  # Field name made lowercase.
    l2_id = models.IntegerField(db_column='L2_ID', blank=True, null=True)  # Field name made lowercase.
    bbt_id = models.IntegerField(db_column='BBT_ID', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    completed = models.BooleanField(db_column='Completed', blank=True, null=True)  # Field name made lowercase.
    due_date = models.DateTimeField(db_column='Due_Date', blank=True, null=True)  # Field name made lowercase.
    last_topic = models.TextField(db_column='Last_Topic', blank=True, null=True)  # Field name made lowercase.
    stat_abbr = models.CharField(db_column='Stat_Abbr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=50, blank=True, null=True)  # Field name made lowercase.
    l2points = models.FloatField(db_column='L2Points', blank=True, null=True)  # Field name made lowercase.
    l1points = models.FloatField(db_column='L1Points', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BBData'


class Fallendata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fruitkey = models.IntegerField(db_column='FruitKey', blank=True, null=True)  # Field name made lowercase.
    bbtid = models.IntegerField(db_column='BBTID', blank=True, null=True)  # Field name made lowercase.
    allreasons = models.TextField(db_column='AllReasons', blank=True, null=True)  # Field name made lowercase.
    sfaenvmain = models.TextField(db_column='sFaEnvMain', blank=True, null=True)  # Field name made lowercase.
    mainreasondetails = models.TextField(db_column='MainReasonDetails', blank=True, null=True)  # Field name made lowercase.
    schedulereasons = models.TextField(db_column='ScheduleReasons', blank=True, null=True)  # Field name made lowercase.
    schedulemain = models.TextField(db_column='ScheduleMain', blank=True, null=True)  # Field name made lowercase.
    environmentreasons = models.TextField(db_column='EnvironmentReasons', blank=True, null=True)  # Field name made lowercase.
    environmentmain = models.TextField(db_column='EnvironmentMain', blank=True, null=True)  # Field name made lowercase.
    interestreasons = models.TextField(db_column='InterestReasons', blank=True, null=True)  # Field name made lowercase.
    disagreereasons = models.TextField(db_column='DisagreeReasons', blank=True, null=True)  # Field name made lowercase.
    mentalcondition = models.TextField(db_column='MentalCondition', blank=True, null=True)  # Field name made lowercase.
    migrationtype = models.TextField(db_column='MigrationType', blank=True, null=True)  # Field name made lowercase.
    migrationreason = models.TextField(db_column='MigrationReason', blank=True, null=True)  # Field name made lowercase.
    wrongintention = models.TextField(db_column='WrongIntention', blank=True, null=True)  # Field name made lowercase.
    financialreasons = models.TextField(db_column='FinancialReasons', blank=True, null=True)  # Field name made lowercase.
    visaduration = models.TextField(db_column='VisaDuration', blank=True, null=True)  # Field name made lowercase.
    understanding = models.TextField(db_column='Understanding', blank=True, null=True)  # Field name made lowercase.
    sexialityorientation = models.TextField(db_column='SexialityOrientation', blank=True, null=True)  # Field name made lowercase.
    unknowndata = models.TextField(db_column='UnknownData', blank=True, null=True)  # Field name made lowercase.
    fallenreportdate = models.TextField(db_column='FallenReportDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FallenData'


class Fbasicdata(models.Model):
    fruitkey = models.IntegerField(db_column='FruitKey', primary_key=True)  # Field name made lowercase.
    fishname = models.TextField(db_column='FishName')  # Field name made lowercase.
    fishphone = models.IntegerField(db_column='FishPhone', blank=True, null=True)  # Field name made lowercase.
    fishuser = models.TextField(db_column='FishUser', blank=True, null=True)  # Field name made lowercase.
    evplatform = models.TextField(db_column='EVPlatform', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    fruitstatus = models.TextField(db_column='FruitStatus', blank=True, null=True)  # Field name made lowercase.
    currleaf1 = models.IntegerField(db_column='CurrLeaf1', blank=True, null=True)  # Field name made lowercase.
    currleaf2 = models.IntegerField(db_column='CurrLeaf2', blank=True, null=True)  # Field name made lowercase.
    bbt = models.IntegerField(db_column='BBT', blank=True, null=True)  # Field name made lowercase.
    points1 = models.FloatField(db_column='Points1', blank=True, null=True)  # Field name made lowercase.
    points2 = models.FloatField(db_column='Points2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FBasicData'

class BBReport(models.Model):
    reportid = models.AutoField(db_column='ReportId', primary_key=True)  # Field name made lowercase.
    reportdate = models.CharField(db_column='ReportDate', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    classdate = models.CharField(db_column='ClassDate', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    fruitkey = models.IntegerField(db_column='FruitKey')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='CreatedBy')  # Field name made lowercase.
    topic = models.CharField(db_column='Topic', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    beforeclass = models.CharField(db_column='BeforeClass', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    duringclass = models.CharField(db_column='DuringClass', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    afterclass = models.CharField(db_column='AfterClass', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    general = models.CharField(db_column='General', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    obedience = models.CharField(db_column='Obedience', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    friendcircumstances = models.CharField(db_column='FriendCircumstances', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    nextclassdate = models.DateTimeField(db_column='NextClassDate', blank=True, null=True)  # Field name made lowercase.
    attendee_1 = models.TextField(db_column='Attendee_1', blank=True, null=True)  # Field name made lowercase.
    attendee_2 = models.TextField(db_column='Attendee_2', blank=True, null=True)  # Field name made lowercase.
    additionalinfo = models.TextField(db_column='AdditionalInfo', blank=True, null=True)  # Field name made lowercase.
    reaction = models.TextField(db_column='Reaction', blank=True, null=True)  # Field name made lowercase.
    attitude = models.TextField(db_column='Attitude', blank=True, null=True)  # Field name made lowercase.
    environment = models.TextField(db_column='Environment', blank=True, null=True)  # Field name made lowercase.
    bbt_feedback = models.TextField(db_column='BBT_Feedback', blank=True, null=True)  # Field name made lowercase.
    label = models.TextField(db_column='Label', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Report'

